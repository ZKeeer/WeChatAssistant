# !/usr/bin/env python
# -*- encoding:utf-8 -*-
import os
import sqlite3
import time

import itchat

from . import config


class MsgAutoReply:
    def __init__(self):

        if os.path.exists("openautoreply") or os.path.exists("closeautoreply"):
            pass
        else:
            with open("openautoreply", "w") as fw:
                fw.write("")

        self.DB = config.database
        self.table = config.reply_table
        self.reply_rule = {}
        db_connect = sqlite3.connect(self.DB)
        try:
            db_connect.execute("""CREATE TABLE IF NOT EXISTS {} (KEYWORD TEXT NOT NULL, REPLYCONTENT TEXT NOT NULL);""".
                               format(self.table))
        except BaseException as e:
            pass
        finally:
            db_connect.close()
        self.reply_rule = self.GetRule()

    def AutoReply(self, msg):
        self.reply_rule = self.GetRule()

        msg_from = ""
        result = itchat.search_friends(userName=msg['FromUserName'])
        if result:
            if result['RemarkName']:
                msg_from = result['RemarkName']  # 消息发送人备注
            elif result['NickName']:  # 消息发送人昵称
                msg_from = result['NickName']  # 消息发送人昵称
            else:
                msg_from = r"读取好友失败"
        else:
            msg_from = msg.get('ActualNickName', "")


        for k in self.reply_rule.keys():
            try:
                if k in msg['Content'] or k in msg['Text'] or k in msg_from:
                    msg_reply = self.reply_rule.get(k, "我收到消息了，待会儿回复")
                    msg_reply += " [来自ZKeeer微信助手]"
                    time.sleep(0.5)
                    # 发送给好友自动回复内容
                    itchat.send(msg_reply, toUserName=msg['FromUserName'])
                    # 好友消息，自动回复消息备份发送至文件助手
                    # 待完成
                    return
            except BaseException as e:
                continue

    def GetRule(self):
        result_dict = {}
        db_connect = sqlite3.connect(self.DB)
        db_cursor = db_connect.cursor()
        try:
            for item in db_cursor.execute("""SELECT * FROM {};""".format(self.table)).fetchall():
                result_dict.update({item[0]: item[1]})
        except BaseException as e:
            pass
        finally:
            db_cursor.close()
            db_connect.close()
        return result_dict

    def AddRule(self, keyword, content):
        db_connect = sqlite3.connect(self.DB)
        db_cursor = db_connect.cursor()
        try:
            if db_cursor.execute(
                    """SELECT * FROM {} WHERE KEYWORD = '{}';""".format(self.table, keyword)).fetchall():
                db_connect.execute("""UPDATE {} SET REPLYCONTENT = '{}' WHERE KEYWORD = '{}';""".
                                   format(self.table, content, keyword))
            else:
                db_connect.execute(
                    """INSERT INTO {} VALUES ('{}', '{}');""".format(self.table, keyword, content))
            db_connect.commit()
            return "添加自动回复 {}:{} 成功".format(keyword, content)
        except BaseException as e:
            db_connect.rollback()
            return "添加失败，请重试"
        finally:
            db_cursor.close()
            db_connect.close()

    def DeleteRule(self, kw):
        db_connect = sqlite3.connect(self.DB)
        db_cursor = db_connect.cursor()
        try:
            if db_cursor.execute("""SELECT * FROM {} WHERE KEYWORD = '{}';""".format(self.table, kw)).fetchall():
                db_connect.execute("""DELETE FROM {} WHERE KEYWORD = '{}';""".format(self.table, kw))
                db_connect.commit()
                return "删除成功"
            else:
                return "关键词不存在，请重试"
        except BaseException as e:
            db_connect.rollback()
            return "删除失败，请重试"
        finally:
            db_cursor.close()
            db_connect.close()

    def ClearRule(self):
        db_connect = sqlite3.connect(self.DB)
        try:
            db_connect.execute("""DELETE FROM {};""".format(self.table))
            db_connect.commit()
            return "清空自动回复成功"
        except BaseException as e:
            return "清空自动回复失败，请重试"
        finally:
            db_connect.close()

    def OpenAutoReply(self):
        if os.path.exists("openautoreply"):
            return "自动回复已经打开"
        else:
            if not os.path.exists("closeautoreply"):
                with open("closeautoreply", 'w')as fw:
                    pass
            os.rename("closeautoreply", "openautoreply")
            return "自动回复已经打开"

    def CloseAutoReply(self):
        if os.path.exists("closeautoreply"):
            return "自动回复已经关闭"
        else:
            if not os.path.exists("openautoreply"):
                with open("openautoreply", 'w')as fw:
                    pass
            os.rename("openautoreply", "closeautoreply")
            return "自动回复已经关闭"

    def ShowRule(self):
        tmp_dict = self.GetRule()
        reslut = ""
        for k, v in zip(tmp_dict.keys(), tmp_dict.values()):
            reslut += "{}:{}、\n".format(k, v)
        if reslut:
            return reslut
        else:
            return "暂无自动回复内容"

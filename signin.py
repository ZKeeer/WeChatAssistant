# -*-encoding:utf-8-*-
import os
import sqlite3
import time

import itchat

import config


class SignInMPS:
    def __init__(self):
        self.db = config.database
        self.table = config.signin_table
        self.signin_list = {}
        self.Date_path = "./signflag.txt"
        db_connect = sqlite3.connect(self.db)

        try:
            db_connect.execute(
                """CREATE TABLE IF NOT EXISTS {} (MPS TEXT NOT NULL, CONTENT NOT NULL);""".format(self.table))
            db_connect.commit()
        except BaseException as e:
            db_connect.rollback()
        finally:
            db_connect.close()

        if not os.path.exists(self.Date_path):
            with open(self.Date_path, "w") as fw:
                fw.write(str(time.localtime().tm_mday - 1))

    def GetCommand(self):
        """
        从command.txt文件中获取公众号及其对应口令。
        口令格式为：#公众号:口令#
        例如：#招商银行信用卡:签到#
        :return: 返回一个dict类型
        """
        command_dict = {}
        db_connect = sqlite3.connect(self.db)
        db_cursor = db_connect.cursor()
        for item in db_cursor.execute("""SELECT * FROM {};""".format(self.table)).fetchall():
            try:
                command_dict.update({item[0]: item[1]})
            except BaseException as e:
                continue
        db_cursor.close()
        db_connect.close()

        return command_dict

    def IsSigned(self):
        """
        获取上次签到日期,并进行判断当天是否签到了
        :return: True:两次日期相同，已经签到了
        """
        if not os.path.exists(self.Date_path):
            with open(self.Date_path, "w") as fw:
                fw.write(time.strftime("%d", time.localtime()))
            last_date = str((time.localtime().tm_mday - 1))
        else:
            with open(self.Date_path, 'r') as fr:
                last_date = fr.read()

        return (last_date == str(time.localtime().tm_mday))

    def SignIn(self):
        """
        获取当前日期，后期上次签到日期，若一致放弃签到，不同则进行签到
        获取签到口令
        对需要签到的公众号进行签到。
        :return: 无
        """

        if self.IsSigned():
            pass
        else:
            sign_list = self.GetCommand()
            if sign_list:
                for item_key in sign_list.keys():
                    for item_key_mps in itchat.search_mps(name=item_key):
                        if item_key_mps:
                            itchat.send(sign_list.get(item_key, '签到'), toUserName=item_key_mps['UserName'])
        with open(self.Date_path, "w") as fw:
            fw.write(time.strftime("%d", time.localtime()))

    def ShowComd(self):
        t_dict = self.GetCommand()
        result = ""
        try:
            for k,v in zip(t_dict.keys(), t_dict.values()):
                result += "{}:{}、\n".format(k,v)
        except BaseException as e:
            pass
        if result:
            return result
        else:
            return "暂无签到口令"

    def ClearComd(self):
        db_connect = sqlite3.connect(self.db)
        try:
            db_connect.execute("""DELETE FROM {};""".format(self.table))
            db_connect.commit()
            return "清空签到口令成功"
        except BaseException as e:
            db_connect.rollback()
            return "清空签到口令失败"
        finally:
            db_connect.close()

    def AddComd(self, mps, comd):
        db_connect = sqlite3.connect(self.db)
        try:
            db_connect.execute("""INSERT INTO {} VALUES ('{}', '{}')""".format(self.table, mps, comd))
            db_connect.commit()
            return "添加签到口令【{}:{}】成功".format(mps,comd)
        except BaseException as e:
            db_connect.rollback()
            return "添加签到口令【{}:{}】失败".format(mps,comd)
        finally:
            db_connect.close()

    def DeleteComd(self, mps):
        db_connect = sqlite3.connect(self.db)
        db_cursor = db_connect.cursor()
        try:
            if db_cursor.execute("""SELECT * FROM {} WHERE MPS = '{}';""".format(self.table, mps)).fetchall():
                db_connect.execute("""DELETE FROM {} WHERE MPS = '{}';""".format(self.table, mps))
                db_connect.commit()
                return "删除口令【{}】成功".format(mps)
            else:
                return "口令【{}】不存在，请重试".format(mps)
        except BaseException as e:
            db_connect.rollback()
            return "删除口令【{}】失败".format(mps)
        finally:
            db_cursor.close()
            db_connect.close()

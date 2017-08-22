# -*-encoding:utf-8-*-
import os
import random
import re
import shutil
import time

import itchat


class Revocation:
    msg_store = {}

    def __init__(self):
        if not os.path.exists("./Cache/"):
            os.mkdir("./Cache/")
        if not os.path.exists("./Revocation/"):
            os.mkdir("./Revocation/")

    # ClearTimeOutMsg用于清理消息字典，把超时消息清理掉
    # 为减少资源占用，此函数只在有新消息动态时调用
    def ClearTimeOutMsg(self):
        """
        清理msg_store中超时的消息
        :return: 无
        """
        if self.msg_store.__len__() > 0:
            for msgid in list(self.msg_store):  # 由于字典在遍历过程中不能删除元素，故使用此方法
                if time.time() - self.msg_store.get(msgid, None)["msg_time"] > 300.0:  # 超时两分钟
                    item = self.msg_store.pop(msgid)

                    # 可下载类消息，并删除相关文件
                    if item['msg_type'] in ['Picture', 'Recording', 'Video', 'Attachment']:
                        os.remove("./Cache/" + item['msg_content'])

    def GetOldMsg(self, msg):
        """
        从存储的消息中查找撤回到消息
        :param msg: 微信消息
        :return: 无
        """
        old_msg_id = ""
        old_msg = {}
        itchat.search_chatrooms()
        if re.search(r"\!\[CDATA\[.*撤回了一条消息\]\]", msg['Content']):
            if re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']):
                old_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)
            elif re.search("\;msgid\&gt\;(.*?)\&lt", msg['Content']):
                old_msg_id = re.search("\;msgid\&gt\;(.*?)\&lt", msg['Content']).group(1)
            old_msg = self.msg_store.get(old_msg_id, {})
        return old_msg_id, old_msg

    def GetMsgFrom(self, msg):
        """
        获取消息来源：联系人和群名
        :param msg: 微信消息
        :return: 无
        """
        msg_group = r""
        if itchat.search_friends(userName=msg['FromUserName']):
            if itchat.search_friends(userName=msg['FromUserName'])['RemarkName']:
                msg_from = itchat.search_friends(userName=msg['FromUserName'])['RemarkName']  # 消息发送人备注
            elif itchat.search_friends(userName=msg['FromUserName'])['NickName']:  # 消息发送人昵称
                msg_from = itchat.search_friends(userName=msg['FromUserName'])['NickName']  # 消息发送人昵称
            else:
                msg_from = r"读取好友失败"
        else:
            msg_from = msg.get('ActualNickName', "")
            if not msg_from:
                msg_from = itchat.search_friends(userName=msg['FromUserName'])

        if itchat.search_chatrooms(userName=msg['FromUserName']):
            msg_group += r'[ '
            msg_group += itchat.search_chatrooms(userName=msg['FromUserName'])['NickName']
            msg_group += r' ]'
        return msg_from, msg_group

    def SaveMsg(self, msg):
        """
        储存所有接收到的消息，以便撤回时查找
        :param msg: 微信消息
        :return: 无
        """
        msg_id = msg['MsgId']  # 消息ID
        msg_time = msg['CreateTime']  # 消息时间
        msg_from, msg_group = self.GetMsgFrom(msg)  # 消息来源
        msg_type = msg['Type']  # 消息类型
        msg_content = None  # 根据消息类型不同，消息内容不同
        msg_url = None  # 分享类消息有url
        # 图片 语音 附件 视频，可下载消息将内容下载暂存到当前目录
        if msg['Type'] == 'Text':
            msg_content = msg['Text']
        elif msg['Type'] == 'Picture':
            msg_content = msg['FileName']
            msg['Text'](msg['FileName'])
            if os.path.exists("./Cache/{}".format(msg_content)):
                msg_content_modify = msg_content.replace(
                    '.', '-{}.'.format(str(random.choice(range(0, 100)))))
                os.rename(msg_content, msg_content_modify)
                msg_content = msg_content_modify
            shutil.move(msg_content, r"./Cache/")

        elif msg['Type'] == 'Card':
            msg_content = msg['RecommendInfo']['NickName'] + r" 的名片"
        elif msg['Type'] == 'Map':
            x, y, location = \
                re.search("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*",
                          msg['OriContent']).group(1, 2, 3)
            if not location:
                msg_content = r"纬度->" + x.__str__() + " 经度->" + y.__str__()
            else:
                msg_content = r"" + location
        elif msg['Type'] == 'Sharing':
            msg_content = msg['Text']
            msg_url = msg['Url']
        elif msg['Type'] == 'Recording':
            msg_content = msg['FileName']
            msg['Text'](msg['FileName'])
            shutil.move(msg_content, r"./Cache/")
        elif msg['Type'] == 'Attachment':
            msg_content = msg['FileName']
            msg['Text'](msg['FileName'])
            shutil.move(msg_content, r"./Cache/")
        elif msg['Type'] == 'Video':
            msg_content = msg['FileName']
            msg['Text'](msg['FileName'])
            shutil.move(msg_content, r"./Cache/")
        elif msg['Type'] == 'Friends':
            msg_content = msg['Text']

        self.msg_store.update(
            {msg_id: {"msg_from": msg_from, "msg_time": msg_time, "msg_type": msg_type,
                      "msg_content": msg_content, "msg_url": msg_url, "msg_group": msg_group}})

    def GetMsgToSend(self, old_msg, msg_time_to_user):
        msg_send = "{0}{1}{0}{2}".format("="*6, "撤回消息", "\n")

        msg_send += "时间: {0}{1}谁: {2}{1}".format(
            msg_time_to_user, "\n", old_msg.get('msg_from', None))

        if old_msg.get('msg_group', None):
            msg_send += "群组: {}{}".format(old_msg['msg_group'], "\n")

        msg_send += "类型: {0}{1}内容: {2}{1}".format(
            old_msg.get('msg_type', None),
            "\n",
            old_msg.get('msg_content', None)
        )

        if old_msg['msg_type'] == "Sharing":
            msg_send += r"网址: {}{}".format(old_msg.get('msg_url', None), "\n")

        elif old_msg['msg_type'] in ['Picture', 'Recording', 'Video', 'Attachment']:
            msg_send += r"存储: Revocation文件夹中{}命令: 查看文件[{}]".format(
                "\n",
                old_msg.get('msg_content', None)
            )
            shutil.move(r"./Cache/" + old_msg['msg_content'], r"./Revocation/")
        return msg_send

    def Revocation(self, msg):
        """
        监听撤回消息通知
        :param msg: 微信消息
        :return: 无
        """
        mytime = time.localtime()
        msg_time_touser = time.strftime("%Y/%m/%d %H:%M:%S", mytime)

        # 创建可下载消息内容的存放文件夹，并将暂存在当前目录的文件移动到该文件中
        if not os.path.exists("./Revocation/"):
            os.mkdir("./Revocation/")

        msg_id, old_msg = self.GetOldMsg(msg)
        if old_msg:
            msg_send = self.GetMsgToSend(old_msg, msg_time_touser)
            # 将撤回消息的通知以及细节发送到文件助手
            itchat.send(msg_send, toUserName='filehelper')
            self.msg_store.pop(msg_id)

# -*-encoding:utf-8-*-
import re
import time
import itchat
from config import Config


class KeywordListener:
    def __init__(self):
        pass

    def GetMsgFrom(self, msg):
        """
        提取消息中的联系人和群组名
        :param msg: 微信消息
        :return: 联系人，群组名
        """
        msg_group = r""
        if itchat.search_friends(userName=msg['FromUserName']):
            if itchat.search_friends(userName=msg['FromUserName'])['RemarkName']:
                msg_from = itchat.search_friends(userName=msg['FromUserName'])['RemarkName']  # 消息发送人备注
            elif itchat.search_friends(userName=msg['FromUserName'])['NickName']:  # 消息发送人昵称
                msg_from = itchat.search_friends(userName=msg['FromUserName'])['NickName']  # 消息发送人昵称
            else:
                msg_from = r"读取发送消息好友失败"
        else:
            msg_from = msg['ActualNickName']
            if msg['ActualUserName'] == itchat.get_friends()[0]['UserName']:
                return
            if itchat.search_chatrooms(userName=msg['FromUserName']):
                msg_group += r'[ '
                msg_group += itchat.search_chatrooms(userName=msg['FromUserName'])['NickName']
                msg_group += r' ]'
        return msg_from, msg_group

    def GetMsgContent(self, msg):
        """
        获取消息内容
        :param msg:微信消息 
        :return: 获取的消息内容
        """
        msg_content = ""
        msg_url = ""

        if msg['Type'] == 'Text':
            msg_content = msg['Text']

        elif msg['Type'] == 'Card':
            msg_content = msg['RecommendInfo']['NickName'] + r" 的名片"

        elif msg['Type'] == 'Map':
            x, y, location = \
                re.search("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*",
                          msg['OriContent']).group(1, 2, 3)
            if location is None:
                msg_content = r"纬度->" + x.__str__() + " 经度->" + y.__str__()
            else:
                msg_content = r"" + location

        elif msg['Type'] == 'Sharing':
            msg_content = msg['Text']
            msg_url = msg['Url']

        return "%s %s" % (msg_content, msg_url)

    def Listener(self, msg):
        """
        处理收到的消息，判断是否有关键词
        :param msg: 微信消息
        :return: 
        """
        config = Config()
        mytime = time.localtime()
        msg_time = "%s/%s/%s %s:%s:%s" % (
            mytime.tm_year.__str__(), mytime.tm_mon.__str__(), mytime.tm_mday.__str__(), mytime.tm_hour.__str__(),
            mytime.tm_min.__str__(), mytime.tm_sec.__str__())

        isContain = False

        keyword_list = config.GetKeyword()
        for item in keyword_list:
            if item:
                if item in msg.get('Text', "") or item in msg.get('Content', ""):
                    isContain = True
                    break

        if isContain:
            msg_from, msg_group = self.GetMsgFrom(msg)
            msg_content = self.GetMsgContent(msg)

            msg_send = "%s%s%s%s" % ("=" * 4, "Keyword Message", "=" * 5, "\n\n")
            msg_send += "Time: %s%sWho: %s%s" % (msg_time, "\n\n", msg_from, "\n\n")
            if msg_group:
                msg_send += "Group: %s%s" % (msg_group, "\n\n")
            msg_send += "Content: %s" % (msg_content)

            itchat.send(msg_send, toUserName='filehelper')

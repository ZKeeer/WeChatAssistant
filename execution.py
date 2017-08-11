import os
import re

import itchat

from watchword import Keyword
from signin import SignInMPS
import screenshoot


class Execution:
    REVOCATIONPATH = "./Revocation/"

    def __init__(self):
        self.keyword = Keyword()
        self.snin = SignInMPS()

    def Execution(self, message):
        """
        执行命令
        :param message: 微信消息中提取的命令
        :return: 无
        """
        # "%s%s%s%s%s关键词" % ("="*4, "Command Message", "="*4, "\n\n", action)

        command = message['Text']
        msg_send = "{0}{1}{0}{2}".format("="*4, "System Message", "\n\n")
        if re.search(r"(.*?)文件\[(.*?)\]", command):
            action, filename = re.search(r"(.*?)文件\[(.*?)\]", command).group(1, 2)
            self.ViewDeleteFile(action, filename)
        
        elif re.match(r"^添加关键词\[.*\]", command):
            msg_send += "添加关键词"

            keyword = re.search(r"^添加关键词\[(.*?)\]", command).group(1)
            added, msg = self.keyword.SetKeyword(keyword)
            msg_send = msg_send + msg + "\n\n"
            msg_send += self.keyword.ShowKeyword()

            itchat.send(msg_send, toUserName='filehelper')

        elif re.match(r"^删除关键词\[.*\]", command):
            msg_send += "删除关键词"

            keyword = re.search(r"^删除关键词\[(.*?)\]", command).group(1)
            removed, msg = self.keyword.RemoveKeyword(keyword)
            msg_send = msg_send + msg + "\n\n"
            msg_send += self.keyword.ShowKeyword()

            itchat.send(msg_send, toUserName='filehelper')

        elif re.match(r"^撤回附件列表$", command):
            self.ReturnAttachmentList()

        elif re.match(r"^清空附件列表$", command):
            self.ClearAttachmentList()

        elif re.match("^查看关键词$", command):
            msg_send += self.keyword.ShowKeyword()
            itchat.send(msg_send, toUserName='filehelper')

        elif re.match("^清空关键词$", command):
            cleared, msg = self.keyword.ClearKeyword()
            msg_send += msg
            
            itchat.send(msg_send, toUserName='filehelper')

        elif re.match("^查看签到口令$", command):
            msg_send += self.snin.ShowComd()
            itchat.send(msg_send, toUserName='filehelper')

        elif re.match("^清空签到口令$", command):
            self.snin.ClearComd()
            msg_send += "清空签到口令成功"
            itchat.send(msg_send, toUserName='filehelper')

        elif re.match("^添加签到口令.*#$", command):
            mps, cmd = re.search("^添加签到口令#(.*?):(.*?)#$", command).group(1, 2)
            self.snin.AddComd(mps, cmd)
            msg_send += "添加签到口令【{}:{}】成功".format(mps, cmd)
            itchat.send(msg_send, toUserName='filehelper')

        elif re.match("^删除签到口令#.*#$", command):
            mps = re.search("^删除签到口令#(.*?)#$", command).group(1)
            if self.snin.DeleteComd(mps):
                msg_send += "口令【{}】删除成功".format(mps)
            else:
                msg_send += "口令【{}】删除失败".format(mps)
            itchat.send(msg_send, toUserName='filehelper')

        elif re.match("^截图$", command):
            screenshoot.SC()

        else:
            itchat.send(r"暂时支持以下指令：{1}"
                        r"查看/删除文件[文件名]{0}e.g.查看[123345234.mp3]{1}"
                        r"撤回附件列表(查看都有哪些保存在电脑中的已撤回附件){1}"
                        r"清空附件列表(清空已经保存在电脑中的附件){1}"
                        r"添加关键词[关键词]{0}e.g.设置关键词[在不在]{1}"
                        r"删除关键词[关键词]{0}e.g.删除关键词[在不在]{1}"
                        r"清空关键词  清空已经设置的所有关键词{1}"
                        r"查看关键词  查看目前设置的关键词{1}"
                        r"添加签到口令#公众号:签到口令#{0}e.g.添加签到口令#招商银行信用卡:签到#{1}"
                        r"删除签到口令#公众号#{0}e.g.删除签到口令#招商银行信用卡#{1}"
                        r"查看签到口令  查看已经存在的公众和和对应的签到口令{1}"
                        r"清空签到口令  清空所有签到口令{1}"
                        r"截图 截取运行本程序的机器当前界面{1}"
                        r"其他指令暂不支持，请期待最新版本。".format("\n", "\n\n"),
                        toUserName="filehelper")

    def ViewDeleteFile(self, action, filename):
        """
        查看或者删除文件
        :param action: 查看/删除
        :param filename: 文件名
        :return: 无
        """
        if action is None or filename is None:
            itchat.send(r"目前支持的指令: 查看/删除文件[文件名] e.g.查看文件[12345678.jpg]", toUserName="filehelper")
            return

        if action == r"查看":
            if re.search(r"png|jpg|bmp|jpeg|gif", filename):
                msg_type = "img"
            elif re.search(r"avi|rm|map4|wmv", filename):
                msg_type = "vid"
            else:
                msg_type = "fil"

            itchat.send("@{}@{}".format(msg_type, r"./Revocation/" + filename),
                        toUserName="filehelper")

        elif action == r"删除":
            try:
                if os.path.exists(r"./Revocation/" + filename):
                    os.remove(r"./Revocation/" + filename)
                    msg = "{0}{1}{0}{2}撤回助手：删除附件成功".format(
                            "="*4, "Command Message", "\n\n")
                    itchat.send(msg, toUserName='filehelper')
                return
            except:
                msg = "{0}{1}{0}{2}撤回助手：删除附件失败，请重试".format(
                        "="*4, "Command Message", "\n\n")
                itchat.send(msg, toUserName='filehelper')

    def ClearAttachmentList(self):
        if self.REVOCATIONPATH:
            try:
                for item in os.listdir(self.REVOCATIONPATH):
                    os.remove(self.REVOCATIONPATH + item)

                msg = "{0}{1}{0}{2}撤回助手：清空附件成功".format(
                    "="*4, "Command Message", "\n\n")
                itchat.send(msg, toUserName='filehelper')
            except:
                msg = "{0}{1}{0}{2}撤回助手：清空附件失败，请重试".format(
                    "="*4, "Command Message", "\n\n")
                itchat.send(msg, toUserName='filehelper')
        else:
            msg = "{0}{1}{0}{2}撤回助手：暂时没有附件".format(
                "="*4, "Command Message", "\n\n")
            itchat.send(msg, toUserName='filehelper')

    # 返回撤回附件所有文件名
    def ReturnAttachmentList(self):
        if os.listdir(self.REVOCATIONPATH):
            msg_send = r"{0}{1}{0}{2}撤回助手：所有储存的附件如下：{3}".format("="*4, "Command Message", "\n\n", "\n")
            for item in os.listdir(self.REVOCATIONPATH):
                msg_send += "{} {}".format(item, "\n")
            itchat.send(msg_send, toUserName="filehelper")
        else:
            msg = r"{0}{1}{0}{2}撤回助手：暂时没有撤回的附件".format("="*4, "Command Message", "\n\n")
            itchat.send(msg, toUserName="filehelper")

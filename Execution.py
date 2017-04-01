import os
import re

import itchat


def ViewDeleteFile(action, filename):
    if action == None or filename == None:
        itchat.send(r"亲，目前支持两种指令：查看/删除文件[文件名] e.g.查看文件[12345678.jpg]", toUserName="filehelper")
        return

    if action == r"查看":
        if re.search(r"png|jpg|bmp|jpeg|gif", filename):
            msg_type = "img"
        elif re.search(r"avi|rm|map4|wmv", filename):
            msg_type = "vid"
        else:
            msg_type = "fil"

        itchat.send("@%s@%s" % (msg_type, r".\\Revocation\\" + filename),
                    toUserName="filehelper")

    elif action == r"删除":
        try:
            if os.path.exists(r".\\Revocation\\" + filename):
                os.remove(r".\\Revocation\\" + filename)
                itchat.send("撤回助手：删除附件成功", toUserName='filehelper')
            return
        except:
            itchat.send("撤回助手：删除附件失败，请重试", toUserName='filehelper')


def ClearAttachmentList():
    filepath = ".\\Revocation\\"
    filelist = os.listdir(filepath)
    if filelist:
        try:
            for item in filelist:
                os.remove(filepath + item)
            itchat.send("撤回助手：清空附件成功", toUserName='filehelper')
        except:
            itchat.send("撤回助手：清空附件失败，请重试", toUserName='filehelper')
    else:
        itchat.send("撤回助手：暂时没有附件", toUserName='filehelper')


# 返回撤回附件所有文件名
def ReturnAttachmentList():
    filepath = ".\\Revocation\\"
    filelist = os.listdir(filepath)
    if filelist:
        msg_send = r"所有储存的附件如下：%s" % ("\n")
        for item in filelist:
            msg_send += "%s %s" % (item, "\n")
        itchat.send(msg_send, toUserName="filehelper")
    else:
        itchat.send(r"撤回助手：暂时没有撤回的附件", toUserName="filehelper")


def Execution(message):
    command = message['Text']
    print("command:", command)
    if re.search(r"(.*?)文件\[(.*?)\]", command):
        action, filename = re.search(r"(.*?)文件\[(.*?)\]", command).group(1, 2)
        ViewDeleteFile(action, filename)
    elif re.match(r"^撤回附件列表$", command):
        ReturnAttachmentList()
    elif re.match(r"^清空附件列表$", command):
        ClearAttachmentList()
    else:
        itchat.send(r"暂时支持以下指令：%s"
                    r"查看/删除文件[文件名] e.g.查看[123345234.mp3]%s"
                    r"撤回附件列表(查看都有哪些保存在电脑中的已撤回附件)%s"
                    r"清空附件列表(清空已经保存在电脑中的附件)%s"
                    r"其他指令暂不支持，请期待最新版本。" % ("\n\n", "\n\n", "\n\n", "\n\n"), toUserName="filehelper")


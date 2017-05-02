import os
import re
import itchat
import Config


def ViewDeleteFile(action, filename):
    """
    查看或者删除文件
    :param action: 查看/删除
    :param filename: 文件名
    :return: 无
    """
    if action == None or filename == None:
        itchat.send(r"目前支持的指令: 查看/删除文件[文件名] e.g.查看文件[12345678.jpg]", toUserName="filehelper")
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
    """
    清空附件
    :return: 
    """
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
    """
    查看撤回消息的相关附件
    :return: 
    """
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
    """
    执行命令
    :param message: 微信消息中提取的命令
    :return: 无
    """
    command = message['Text']
    print("command:", command)
    if re.search(r"(.*?)文件\[(.*?)\]", command):
        action, filename = re.search(r"(.*?)文件\[(.*?)\]", command).group(1, 2)
        ViewDeleteFile(action, filename)
    elif re.search(r".{2}关键词\[.*\]", command):
        action, keyword = re.search("(.*?)关键词\[(.*?)\]", command).group(1, 2)
        msg_send = "%s关键词" % (action)
        if action == r"添加":
            if Config.SetKeyword(keyword):
                msg_send += "成功"
            else:
                msg_send += "失败，请重试"
        elif action == r"删除":
            if Config.RemoveKeyword(keyword):
                msg_send += "成功"
            else:
                msg_send += "失败，请重试"
        itchat.send(msg_send, toUserName='filehelper')
    elif re.match(r"^撤回附件列表$", command):
        ReturnAttachmentList()
    elif re.match(r"^清空附件列表$", command):
        ClearAttachmentList()
    elif re.match("^查看关键词$", command):
        msg_send = Config.ShowKeyword()
        itchat.send(msg_send, toUserName='filehelper')
    elif re.match("^清空关键词$", command):
        if Config.ClearKeyword():
            msg_send = "清空关键词成功"
        else:
            msg_send = "清空关键词失败，请重试"
        itchat.send(msg_send, toUserName='filehelper')
    else:
        itchat.send(r"暂时支持以下指令：%s"
                    r"查看/删除文件[文件名] e.g.查看[123345234.mp3]%s"
                    r"撤回附件列表(查看都有哪些保存在电脑中的已撤回附件)%s"
                    r"清空附件列表(清空已经保存在电脑中的附件)%s"
                    r"添加关键词[关键词] e.g.设置关键词[在不在]%s"
                    r"删除关键词[关键词] e.g.删除关键词[在不在]%s"
                    r"清空关键词 清空已经设置的所有关键词%s"
                    r"查看关键词 查看目前设置的关键词%s"
                    r"其他指令暂不支持，请期待最新版本。" % ("\n\n", "\n\n", "\n\n", "\n\n", "\n\n", "\n\n", "\n\n", "\n\n"),
                    toUserName="filehelper")

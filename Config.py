# -*-encoding:utf-8-*-
import os

CONFIG_PATH = ".\\config.txt"


def InitConfig():
    """
    初始化配置文件
    :return: 
    """
    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "w")as fw:
            fw.write("关键词1#关键词2#关键词n#") #每个关键词后面带#，这是标准格式


def GetKeyword():
    """
    获取关键词
    :return: 
    """
    with open(CONFIG_PATH, "r")as fr:
        keyword_list = fr.read().split("#")
    return keyword_list


def SetKeyword(keyword):
    """
    添加关键词
    :param keyword: 
    :return: 
    """
    try:
        with open(CONFIG_PATH, "a") as fw:
            fw.write("%s#" % (keyword))
        return True
    except:
        return False


def RemoveKeyword(key):
    """
    删除关键词
    :param key: 
    :return: 
    """
    with open(CONFIG_PATH, "r") as fr:
        key_list = fr.read().split("#")

    if key in key_list:
        key_list.remove(key)
    else:
        return False

    if key_list:
        with open(CONFIG_PATH, "w") as fw:
            for item in key_list:
                fw.write(item + "#")

    return True


def ClearKeyword():
    """
    清空所有关键词
    :return: 
    """
    try:
        with open(CONFIG_PATH, "w")as fw:
            fw.write("")
        return True
    except:
        return False


def ShowKeyword():
    """
    查看关键词
    :return: 
    """
    with open(CONFIG_PATH, "r") as fr:
        flist = fr.read().split("#")

    msg_send = "现有的关键词：%s" % ("\n")
    for item in flist:
        if item:
            msg_send += "%s%s" % (item, "\n")

    return msg_send



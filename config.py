# -*-encoding:utf-8-*-
import os

CONFIG_PATH = "./config.txt"


class Config:
    def __init__(self):
        if not os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "w")as fw:
                fw.write("关键词1#关键词2#关键词n#")  # 每个关键词后面带#，这是标准格式

    def GetKeyword(self):
        with open(CONFIG_PATH, "r")as fr:
            keyword_list = fr.read().split("#")
        return keyword_list

    def SetKeyword(self, keyword):
        try:
            with open(CONFIG_PATH, "a") as fw:
                fw.write("%s#" % (keyword))
            return True
        except:
            return False

    def RemoveKeyword(self, key):
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

    def ClearKeyword(self):
        try:
            with open(CONFIG_PATH, "w")as fw:
                fw.write("")
            return True
        except:
            return False

    def ShowKeyword(self):
        with open(CONFIG_PATH, "r") as fr:
            flist = fr.read().split("#")

        msg_send = "现有的关键词：%s" % ("\n")
        for item in flist:
            if item:
                msg_send += "%s%s" % (item, "\n")

        return msg_send

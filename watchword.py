# -*-encoding:utf-8-*-
import os

KEYWORD_FILE_PATH = "./keyword.txt"


class Keyword:
    def __init__(self):
        if not os.path.exists(KEYWORD_FILE_PATH):
            with open(KEYWORD_FILE_PATH, "w")as fw:
                fw.write("# 关键词格式如下，由#分隔\n")
                fw.write("关键词1#关键词2#关键词n#")  # 每个关键词后面带#，这是标准格式

    def GetKeyword(self):
        keyword_list = []
        keyword_file = open(KEYWORD_FILE_PATH, "r")
        for line in keyword_file:
            # Parse不是由#开头的第一行关键词
            if not line.startswith("#"):
                keyword_list = line.split("#")
                break

        return keyword_list

    def SetKeyword(self, keyword):
        try:
            with open(KEYWORD_FILE_PATH, "a") as fw:
                fw.write("{}#".format(keyword))
            return True, "成功"
        except:
            return False, "无法打开keyword文件"

    def RemoveKeyword(self, key):
        keyword_file = open(KEYWORD_FILE_PATH, "r+")
        line = ""
        for line in keyword_file:
            if not line.startswith("#"):
                break

        new_line = line.replace(key+'#', '')
        if new_line != line:
            keyword_file.seek(0)
            keyword_file.truncate()
            keyword_file.write(new_line)
            keyword_file.close()
            return True, "成功"

        else:
            keyword_file.close()
            return False, "失败，列表中无此关键词"

    def ClearKeyword(self):
        try:
            with open(KEYWORD_FILE_PATH, "w")as fw:
                fw.write("")
            return True, "清空关键词成功"
        except:
            return False, "清空关键词失败，无法打开keyword文件"

    def ShowKeyword(self):
        keyword_list = []
        # Parse不是由#开头的第一行关键词
        for line in open(KEYWORD_FILE_PATH, "r"):
            if not line.startswith("#"):
                keyword_list = line.split("#")
                break

        msg_send = "现有的关键词：\n"
        for item in keyword_list:
            if item:
                msg_send += "{}\n".format(item)

        return msg_send

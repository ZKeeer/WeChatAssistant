# -*-encoding:utf-8-*-
import os
import time


class Log:
    LOG_PATH = "./Log/log.txt"

    def __init__(self):
        if not os.path.exists("./Log/"):
            os.mkdir("./Log/")

        if not os.path.exists(self.LOG_PATH):
            with open(self.LOG_PATH, "w") as fw:
                pass

    def WriteLog(self, e):
        with open(self.LOG_PATH, "a") as fw:
            msg_error = "ERROR:{0}time: {1}{0}lineno: {2}{0}errorinfo: {3}{4}".format(
                "\n",
                time.ctime(),
                e.__traceback__.tb_lineno,
                e.args[0],
                "\n\n\n"
            )
            fw.write(msg_error)

# -*-encoding:utf-8-*-
import os
import time


class Log:
    LOG_PATH = ".\\Log\\log.txt"

    def __init__(self):
        if not os.path.exists(".\\Log\\"):
            os.mkdir(".\\Log\\")

        if not os.path.exists(self.LOG_PATH):
            with open(self.LOG_PATH, "w") as fw:
                pass

    def WriteLog(self, msg):
        with open(self.LOG_PATH, "a") as fw:
            fw.write(time.ctime() + "\n" + msg + "\n\n\n")
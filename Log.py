# -*-encoding:utf-8-*-
import os
import time

LOG_PATH = ".\\Log\\log.txt"


def InitLog():
    """
    初始化日志文件
    :return: 无
    """
    if not os.path.exists(".\\Log\\"):
        os.mkdir(".\\Log\\")

    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w") as fw:
            pass


def WriteLog(msg):
    """
    将错误信息写入日志文件
    :param msg: 错误消息
    :return: 无
    """
    InitLog()
    with open(LOG_PATH, "a") as fw:
        fw.write(time.time() + "\n" + msg + "\n\n\n")

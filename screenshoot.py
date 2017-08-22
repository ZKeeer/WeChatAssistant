import os
import platform
from time import time

import itchat


def GetImagePath():
    if not os.path.exists("./ScreenShoot/"):
        os.mkdir("./ScreenShoot/")
    return "./ScreenShoot/"


def SC():
    im_path = GetImagePath()
    im_name = "{}{}.{}".format(im_path, str(time()), "png")

    im = None

    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        from PIL import ImageGrab
        try:
            im = ImageGrab.grab()
        except OSError as e:
            itchat.send("截图失败，请重试。（或许您的设备不支持截图）", toUserName="filehelper")
            return

    elif platform.system() == 'Linux':
        import pyscreenshot as ImageGrab
        try:
            im = ImageGrab.grab()
        except OSError as e:
            itchat.send("截图失败，请重试。（或许您的设备不支持截图）", toUserName="filehelper")
            return


    im.save(im_name)
    if os.path.exists(im_name):
        try:
            itchat.send("@img@{}".format(im_name), toUserName="filehelper")
        except BaseException as e:
            itchat.send("发送截图失败，请重试。", toUserName="filehelper")
    else:
        itchat.send("截图失败，请重试。", toUserName="filehelper")

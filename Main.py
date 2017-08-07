# -*-encoding:utf-8-*-

import sys
import os
import itchat
from itchat.content import *
import traceback
from config import Config
from execution import Execution
from keeponline import KeepOnline
from keywordlistener import KeywordListener
from revocation import Revocation
from signin import SignInMPS

exec_command = Execution()
rmsg = Revocation()
listener = KeywordListener()
signfunc = SignInMPS()
kol = KeepOnline()


# 将接收到的消息存放在字典中，当接收到新消息时对字典中超时的消息进行清理
# 没有注册note（通知类）消息，通知类消息一般为：红包 转账 消息撤回提醒等，不具有撤回功能
@itchat.msg_register([TEXT, PICTURE, MAP, CARD, SHARING, NOTE, RECORDING, ATTACHMENT, VIDEO, FRIENDS],
                     isFriendChat=True,
                     isGroupChat=True)
def Main(msg):
    """
    获取微信消息，进行处理指令、关键词监听、撤回消息监听的动作
    :param msg: 微信消息
    :return: 无
    """
    # 三大功能之一：处理指令(新添加的功能：签到，其中添加/删除/清空/查看签到口令相关命令和功能未实现)
    itchat.get_friends(update=True)
    if msg['ToUserName'] == "filehelper" and msg['Type'] == "Text":
        try:
            exec_command.Execution(msg)
        except BaseException as e:
            traceback.print_exc(file=open('log.txt', 'a'))

    # 三大功能之二：撤回消息部分
    try:
        rmsg.SaveMsg(msg)
        rmsg.Revocation(msg)
        rmsg.ClearTimeOutMsg()
    except BaseException as e:
        traceback.print_exc(file=open('log.txt', 'a'))

    # 三大功能之三：关键词监听
    if msg['Type'] in ['Text', 'Sharing', 'Map', 'Card']:
        try:
            listener.Listener(msg)
        except BaseException as e:
            traceback.print_exc(file=open('log.txt', 'a'))

    # 功能：公众号签到
    try:
        signfunc.SignIn()
    except BaseException as e:
        traceback.print_exc(file=open('log.txt', 'a'))
    # 功能：保持在线
    kol.ActiveWX()


if __name__ == '__main__':
    config = Config()
    # 机器上有默认的图片打开程序，使用这个，直接弹出二维码扫码登陆
    #itchat.auto_login(hotReload=True)
    # 使用命令行登录，选此条语句，参数选2或者1，根据不同机器的字符宽度决定，大家挨个尝试
    #itchat.auto_login(hotReload=True, enableCmdQR=2)
         
    if len(sys.argv) > 1:
        if sys.argv[1] == '-t':
            itchat.auto_login(hotReload=True, enableCmdQR=2)
    else:
        if sys.platform == 'linux':
            if "XDG_CURRENT_DESKTOP" in os.environ:
                itchat.auto_login(hotReload=True)
            else:
                itchat.auto_login(hotReload=True, enableCmdQR=2)
        else:
            itchat.auto_login(hotReload=True)
                
    itchat.run()

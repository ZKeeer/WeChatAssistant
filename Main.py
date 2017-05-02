# -*-encoding:utf-8-*-
import os

import itchat
from itchat.content import *

import Config
import Execution
import KeywordListener
import Log
import Revocation

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
    # 三大功能之一：处理指令
    itchat.get_friends(update=True)
    if msg['ToUserName'] == "filehelper" and msg['Type'] == "Text":
        Execution.Execution(msg)

    # 三大功能之二：撤回消息部分
    Revocation.SaveMsg(msg)
    Revocation.Revocation(msg)
    Revocation.ClearTimeOutMsg()

    # 三大功能之三：关键词监听
    if msg['Type'] in ['Text', 'Sharing', 'Map', 'Card']:
        KeywordListener.Listener(msg)

if __name__ == '__main__':
    try:
        Revocation.ClearTimeOutMsg()
        if not os.path.exists(".\\Cache\\"):
            os.mkdir(".\\Cache\\")
        Config.InitConfig()

        itchat.auto_login(hotReload=True)
        itchat.run()
    except BaseException as e:
        Log.WriteLog(e)

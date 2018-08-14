# -*-encoding:utf-8-*-

import os
import sys
import time
import traceback
from threading import Thread

import itchat

from autoreply import MsgAutoReply
from execution import Execution
from keeponline import KeepOnline
from keywordlistener import KeywordListener
from revocation import Revocation
from signin import SignInMPS

exec_command = Execution()
rmsg = Revocation()
listener = KeywordListener()
signfunc = SignInMPS()
keeponline = KeepOnline()
reply = MsgAutoReply()

visitors = 4
visitor_wait = False
msglist = list()


# 解析消息，构造{id:xxx, msg:{}, visit:xxx}类型的消息，加入消息队列
@itchat.msg_register(
    [
        itchat.content.TEXT,
        itchat.content.PICTURE,
        itchat.content.MAP,
        itchat.content.CARD,
        itchat.content.SHARING,
        itchat.content.NOTE,
        itchat.content.RECORDING,
        itchat.content.ATTACHMENT,
        itchat.content.VIDEO,
        itchat.content.FRIENDS,
    ],
    isFriendChat=True,
    isGroupChat=True
)
def msg_acceptor(msg):
    msg['Visitor'] = 0
    msglist.append(msg)
    print(msg, '\n\n\n\n')


def clearmsglist_func():
    record = {'MsgId': "", "time": 0.0}
    while True:
        if msglist:
            if int(msglist[0].get("Visitor", 0)) >= visitors:
                msglist.pop(0)
                if msglist:
                    record.update({msglist[0].get('MsgId', ''): time.time()})
            else:
                # 消息阻塞清理
                if msglist[0].get('MsgId', '') == record.get('MsgId', ''):
                    if time.time() - record.get('time', '') > 10.0:
                        msglist.pop(0)
                else:
                    record.update({'MsgId': msglist[0].get('MsgId', ''), "time": time.time()})
        else:
            time.sleep(1)


def Pretreat(func):
    def wapper(*args, **kwargs):
        msgid = ''
        while True:

            # 消息队列为空，等待
            while not msglist:
                time.sleep(0.1)

            # 头元素是已经访问过的消息，继续下一次循环
            try:
                if msglist[0].get('MsgId', '') == msgid:
                    continue
            except BaseException as e:
                traceback.print_exc(file=open('log.txt', 'a'))

            # 消息队列不为空并且头元素是未访问过的消息，进行处理。
            try:
                func()
            except BaseException as e:
                traceback.print_exc(file=open('log.txt', 'a'))
            finally:
                # 最终必须更新消息ID，证明访问过该消息
                if msglist:
                    msgid = msglist[0].get('MsgId', '')
                    # 互斥锁，该消息的访问次数的修改必须是串行
                    global visitor_wait
                    while visitor_wait:
                        pass
                    visitor_wait = True
                    msglist[0]['Visitor'] = (msglist[0].get('Visitor', 0) + 1)
                    visitor_wait = False

    return wapper


@Pretreat
def execute_func():
    global exec_command
    # 1.文件助手命令
    if msglist[0].get('ToUserName', "") == "filehelper" and msglist[0].get('Type', "") == "Text":
        exec_command.Execution(msglist[0])


@Pretreat
def revocation_func():
    # 2.撤回消息
    global rmsg
    rmsg.SaveMsg(msglist[0])
    rmsg.Revocation(msglist[0])
    rmsg.ClearTimeOutMsg()


@Pretreat
def keywordlisten_func():
    # 3.关键词监听
    global listener
    if msglist[0].get('Type', '') in ['Text', 'Sharing', 'Map', 'Card'] \
            and msglist[0].get('FromUserName', '') != 'filehelper':
        listener.Listener(msglist[0])


@Pretreat
def autoreply_func():
    # 4.自动回复
    global reply
    if os.path.exists("openautoreply"):
        reply.AutoReply(msglist[0])


def signin_func():
    global signfunc
    while True:
        # 功能：公众号签到
        signfunc.SignIn()
        time.sleep(3600)


def keeponline_func():
    global keeponline
    while True:
        # 功能：保持在线
        keeponline.ActiveWX()
        time.sleep(1800)


if __name__ == '__main__':
    # 机器上有默认的图片打开程序，直接弹出二维码扫码登陆
    # 否则使用命令行输出二维码

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

    run_thread = Thread(target=itchat.run)
    clearmsglist_thread = Thread(target=clearmsglist_func)
    execute_thread = Thread(target=execute_func)
    revocation_thread = Thread(target=revocation_func)
    keywordlisten_thread = Thread(target=keywordlisten_func)
    autoreply_thread = Thread(target=autoreply_func)
    signin_thread = Thread(target=signin_func)
    keeponline_thread = Thread(target=keeponline_func)

    run_thread.start()
    execute_thread.start()
    revocation_thread.start()
    keywordlisten_thread.start()
    autoreply_thread.start()
    signin_thread.start()
    keeponline_thread.start()
    clearmsglist_thread.start()

    run_thread.join()
    execute_thread.join()
    revocation_thread.join()
    keywordlisten_thread.join()
    autoreply_thread.join()
    signin_thread.join()
    keeponline_thread.join()
    clearmsglist_thread.join()

import itchat
import os
path = os.path.dirname(__file__) + '/QR'
if not os.path.exists(path):
    os.mkdir(path)
    while not itchat.get_QRuuid():
        time.sleep(1)
    itchat.get_QR(picDir=path + '/QR.png')
itchat.auto_login(picDir=path+'/sss.png')
import time

import itchat


class KeepOnline:
    curr_hour = 0

    def __init__(self):
        self.curr_hour = time.localtime().tm_mday

    def IsActived(self):
        if self.curr_hour == time.localtime().tm_mday:
            return True
        else:
            return False

    def ActiveWX(self):
        if self.IsActived():
            pass
        else:
            itchat.login()

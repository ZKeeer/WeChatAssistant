import time

import itchat


class KeepOnline:
    def __init__(self):
        self.curr_hour = time.localtime().tm_hour

    def IsActived(self):
        if self.curr_hour == time.localtime().tm_hour:
            return True
        else:
            self.curr_hour = time.localtime().tm_hour
            return False

    def ActiveWX(self):
        if self.IsActived():
            pass
        else:
            itchat.login()

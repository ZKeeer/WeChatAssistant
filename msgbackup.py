import sqlite3

import config


class MsgBackup:
    def __init__(self):
        self.db = config.database
        self.table = config.msgbackup_table
        self.connect = sqlite3.connect(self.db)
        self.cursor = self.connect.cursor()
        self.connect.execute("""CREATE TABLE IF NOT EXISTS {} ();""".format(self.table))

    def Backup(self, msg):
        pass

    def SearchMsg(self, keyword):
        pass

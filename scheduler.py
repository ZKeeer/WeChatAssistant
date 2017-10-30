# 日程存储以队列形式[{index:1, name:日程1, date:2017/07/26, time:13:30:00},{}],外部存储用.csv
# 按时间先后排序，每新添加一个日程都要进行排序。
# 增删改查日程
# 日程与日程之间采用time.sleep(距离下次日程的秒数)
# 彩蛋：若name的值为“发送消息给xxx，消息内容”则可定时发送消息，并且提醒消息已发送。

class Schedule:
    def __init__(self):
        pass

    def AddItem(self,):
        pass

    def DeleteItem(self,):
        pass

    def ModifyItem(self):
        pass

    def ViewItem(self):
        pass

    def ExstractItem(self,msg):
        """
        从msg中提取content然后从content中提取事件，日期，事件
        :param content: 文件助手发来的字符串
        :return: {name:xxxx, date:xxxx time:xxxx}
        """
        pass

    def OrderItems(self):
        pass

    def GetScondsBTWItems(self):
        pass

    def ExecuteItem(self,sleeptime,content):
        pass

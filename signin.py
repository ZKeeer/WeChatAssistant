# -*-encoding:utf-8-*-
import os
import re
import time

import itchat


class SignInMPS:
    Command_Path = "Command.txt"
    Date_path = "Date.txt"

    def __init__(self):
        if not os.path.exists(self.Command_Path):
            with open(self.Command_Path, "w") as fw:
                fw.write('')
        if not os.path.exists(self.Date_path):
            with open(self.Date_path, "w") as fw:
                fw.write((time.localtime().tm_mday - 1).__str__())

    def GetCommand(self):
        """
        从command.txt文件中获取公众号及其对应口令。
        口令格式为：#公众号:口令#
        例如：#招商银行信用卡:签到#
        :return: 返回一个dict类型
        """
        if not os.path.exists(self.Command_Path):
            with open(self.Command_Path, "w") as fw:
                fw.write('')
            return {}

        command_dict = {}
        with open(self.Command_Path, 'r') as fr:
            file_content = fr.read()
            # result类型为：[(), (), ...]
            result = re.findall("#(.*?):(.*?)#", file_content)
            if result:
                for item in result:
                    command_dict.update({item[0]: item[1]})

        return command_dict

    def IsSigned(self):
        """
        获取上次签到日期,并进行判断当天是否签到了
        :return: True:两次日期相同，已经签到了
        """
        if not os.path.exists(self.Date_path):
            with open(self.Date_path, "w") as fw:
                fw.write(time.localtime().tm_mday.__str__())
            last_date = (time.localtime().tm_mday - 1).__str__()
        else:
            with open(self.Date_path, 'r') as fr:
                last_date = fr.read()

        return (last_date == time.localtime().tm_mday.__str__())

    def SignIn(self):
        """
        获取当前日期，后期上次签到日期，若一致放弃签到，不同则进行签到
        获取签到口令
        对需要签到的公众号进行签到。
        :return: 无
        """

        if self.IsSigned():
            pass
        else:
            sign_list = self.GetCommand()
            if sign_list:
                for item_key in sign_list.keys():
                    for item_key_mps in itchat.search_mps(name=item_key):
                        if item_key_mps:
                            itchat.send(sign_list.get(item_key, '签到'), toUserName=item_key_mps['UserName'])
        with open(self.Date_path, 'w') as fw:
            fw.write(time.localtime().tm_mday.__str__())

    def ShowComd(self):
        with open(self.Command_Path, 'r') as fr:
            comd_list = fr.read()
            comd_list_tmp = re.findall("#(.*?)#", comd_list)
            comd_list_retn = ''
            for item in comd_list_tmp:
                comd_list_retn += (item + '\n')
        return comd_list_retn

    def ClearComd(self):
        with open(self.Command_Path, 'w') as fw:
            fw.write('')
        return True

    def AddComd(self, mps, comd):
        with open(self.Command_Path, 'a') as fa:
            fa.write('#{}:{}#'.format(mps, comd))
        return True

    def DeleteComd(self, mps):
        file_content = ''

        with open(self.Command_Path, 'r') as fr:
            file_content = fr.read()
        if re.findall(mps, file_content):
            comd = re.search("#{}:(.*?)#".format(mps), file_content).group(1)
            file_content = file_content.replace('#{}:{}#'.format(mps, comd), '')
            with open(self.Command_Path, 'w') as fw:
                fw.write(file_content)
            return True
        return False

# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     read_ini
# Author:      Jakiro
# Datetime:    2020/12/5 17:03
# Description:
# -----------------------------------------------------------------------------------

import configparser
from common.get_path import get_file_path
import os

# 读取ini文件数据模块 提供了加载配置文件路径的方法
class ReadIni(object):
    def __init__(self):
        # 实例化configparser对象
        self.config = configparser.ConfigParser()
        # 调用get_path()函数，获取项目的绝对路径
        self.pro_absolute_path = get_file_path('ranzhi_project')
        # 读取ini文件内容
        self.config.read(self.pro_absolute_path + r'\data_config\file_path.ini',
                         encoding='utf8')

    def get_yaml_path(self):
        # 读取ini文件中的yaml配置文件路径数据
        date_file_path = self.config.get("path", 'yaml_path')
        # print(date_file_path)
        # 拼接项目的绝对路径和配置文件路径数据
        return os.path.join(self.pro_absolute_path, date_file_path)

    def get_json_path(self):
        # 读取ini文件中的json配置文件路径数据
        date_file_path = self.config.get("path", 'json_path')
        # print(date_file_path)
        # 拼接项目的绝对路径和配置文件路径数据
        return os.path.join(self.pro_absolute_path, date_file_path)

    def get_excel_path(self):
        # 读取ini文件中的excel配置文件路径数据
        date_file_path = self.config.get("path", 'excel_path')
        # print(date_file_path)
        # 拼接项目的绝对路径和配置文件路径数据
        return os.path.join(self.pro_absolute_path, date_file_path)

    def get_screen_shot_path(self):
        # 读取ini文件中的截图配置文件路径数据
        date_file_path = self.config.get("path", 'screen_shot_path')
        # print(date_file_path)
        # 拼接项目的绝对路径和配置文件路径数据
        return os.path.join(self.pro_absolute_path, date_file_path)

    def get_logging_path(self):
        # 读取ini文件中的日志配置文件路径数据
        date_file_path = self.config.get("path", 'logging_path')
        # print(date_file_path)
        # 拼接项目的绝对路径和配置文件路径数据
        return os.path.join(self.pro_absolute_path, date_file_path)

    def get_case_path(self):
        # 读取ini文件中的case文件路径数据
        date_file_path = self.config.get("path", 'case_path')
        # print(date_file_path)
        # 拼接项目的绝对路径和配置文件路径数据
        return os.path.join(self.pro_absolute_path, date_file_path)

    def get_report_path(self):
        # 读取ini文件中的报告文件路径数据
        date_file_path = self.config.get("path", 'report_path')
        # print(date_file_path)
        # 拼接项目的绝对路径和配置文件路径数据
        return os.path.join(self.pro_absolute_path, date_file_path)


if __name__ == '__main__':
    readini = ReadIni()
    print(readini.get_case_path())

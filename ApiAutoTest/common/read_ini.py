# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ApiAutoTest
# FileName:     read_ini.py
# Author:      Jakiro
# Datetime:    2021/3/5 11:32 上午
# Description:  此模块用于读取系统内文件的绝对路径
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import os
from configparser import ConfigParser


class ReadIni(object):
    def __init__(self):
        # 实例化configParser对象
        self.config = ConfigParser()
        # dirname方法找到参数文件的父目录
        self.base_path = os.path.dirname(os.path.dirname(__file__))
        # 通过拼接项目的绝对路径和当前文件到项目的相对路径 获得当前ini文件所在目录路径
        current_ini_file_path = os.path.join(self.base_path, 'data\path.ini').replace('\\', '/')
        print(current_ini_file_path)
        # 通过config对象的read方法 读取ini文件
        self.config.read(current_ini_file_path, encoding='utf8')

    # 声明一个方法可以获得excel文件路径
    def get_excel_path(self):
        # 通过section和选项获得ini文件对应的相对路径值 然后用os.path的join方法将项目的绝对路径和相对路径拼接
        return os.path.join(self.base_path, self.config.get('path', 'excel_path')).replace('\\', '/')

    # 声明一个方法可以获得参数json文件路径
    def get_params_json_path(self):
        # 通过section和选项获得ini文件对应的相对路径值 然后用os.path的join方法将项目的绝对路径和相对路径拼接
        return os.path.join(self.base_path, self.config.get('path', 'params_json_path')).replace('\\', '/')

    # 声明一个方法可以获得断言json文件路径
    def get_exception_json_path(self):
        # 通过section和选项获得ini文件对应的相对路径值 然后用os.path的join方法将项目的绝对路径和相对路径拼接
        return os.path.join(self.base_path, self.config.get('path', 'exception_json_path')).replace('\\', '/')

    # 声明一个方法可以获得path中的sheet名
    def get_sheet_name(self):
        # 通过section和选项获得ini文件对应的sheet_name值
        return self.config.get('path', 'sheet_name')


if __name__ == '__main__':
    read = ReadIni()
    print(read.get_excel_path())
    print(read.get_params_json_path())
    print(read.get_exception_json_path())
    print(read.get_sheet_name())
    print(read.current_ini_file_path)

# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ApiAutoTest
# FileName:     read_json.py
# Author:      Jakiro
# Datetime:    2021/3/5 11:38 上午
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import json


def read_json(json_path):
    with open(json_path, encoding='utf8') as fp:
        # loads方法的参数为字符串 ，返回值为字典
        return json.loads(fp.read())


if __name__ == '__main__':
    print(read_json(r'/Users/qiujie/PycharmProjects/ApiAutoTest/data/params.json'))

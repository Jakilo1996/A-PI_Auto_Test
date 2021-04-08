# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ApiAutoTest
# FileName:     main.py
# Author:      Jakiro
# Datetime:    2021/3/11 1:21 下午
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import pytest
from time import strftime

tt = strftime('%Y-%m-%d_%H-%M-%S')
test_path = r'/Users/qiujie/PycharmProjects/ApiAutoTest/case/test_pytest.py'
report_path = r'/Users/qiujie/PycharmProjects/ApiAutoTest/result/test_report'
file_name = '/test_all_api_report{}.html'.format(tt)
# main 函数 依次拼接参数和用例p路径，完成日志文件的生成
pytest.main(['--self-contained-html', '--html=' + report_path + file_name, test_path])

# 解决 linux下，maim  按时间生成日志运行问题 并复制一份 为发送附件目录文件名 每次新生成的报告 会覆盖原来的报告 ，能保证每次都是按时间发送报告

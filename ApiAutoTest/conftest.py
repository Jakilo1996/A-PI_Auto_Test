# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ApiAutoTest
# FileName:     conftest.py
# Author:      Jakiro
# Datetime:    2021/3/11 1:19 下午
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

'''
pytest的固件装饰器配置文件，pytest运行时，会从此文件下寻找固件来调用
此文件下定义的装饰器，可以不将固件传入用例形参直接调用

conftest.py：在pytest中，可以把所有自定义的固件写到conftest.py中，好处是可以不用导入模块，就可以在任意测试模块中
调用自定义的固件，注意conftest.py文件的路径必须放到测试模块所在目录或者上一级目录下才能保证被调用到，在实际中，可以放到
项目的根目录下，这样项目下的所有测试模块都能调用到自定义固件。

描述同.case.test_pytest_01
'''

import pytest
from request_method.request_method import RequestMethod


# 自定义一个固件，实例化RequestMethod对象
@pytest.fixture(scope='session')
def get_request_method_fixture():
    yield RequestMethod()
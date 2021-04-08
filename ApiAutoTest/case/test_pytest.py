# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ApiAutoTest
# FileName:     test_pytest.py
# Author:      Jakiro
# Datetime:    2021/3/11 1:17 下午
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import pytest
from common.get_data import get_data

'''
通过pytest来实现用例定义
使用自定义固件初始化RequestMethod类
通过装饰器pytest.mark.parameterize()来进行参数化 需要将参数名以字符串传给装饰器的第一个参数，对应的解析数据为第二个参数
get_data函数以列表套元组返回对应数据
'''


class TestCaseWithPytest():
    @pytest.mark.parametrize(
        'case_id, method, url, if_execute, precondition, depend_key, pattern, expect, data_type, row', get_data())
    def test_all(self, get_request_method_fixture, case_id, method, url, if_execute, precondition, depend_key, pattern,
                 expect, data_type, row):
        print(case_id, if_execute)
        print('响应数据类型是', data_type)
        print('前置条件', precondition)
        if if_execute == "Y":
            print("现在开始执行第%d行的用例" % row)
            # print("前置用例是：%s"%precondition_case_id)
            if precondition:
                params = get_request_method_fixture.update_case_params_depend_field(row=row)
                print(params)
            else:
                params = get_request_method_fixture.read_execl.get_case_parameters_value(row=row)
            print(method, url, params)
            actual = get_request_method_fixture.get_case_actual_result(method=method, url=url,
                                                                       response_data_type=data_type, params=params)
            # 断言：如果响应数据类型是JSON，就判断预期结果与实际结果是否相等，如果响应是XML，就判断预期结果
            # 是否包含在实际结果中
            if expect:
                if data_type == "JSON":
                    try:
                        # self.assertEqual(expect, actual, msg="实际与预期不一致！")
                        assert expect == actual
                    except AssertionError:
                        print("预期结果是：%s" % dict(set(expect.items()) - set(actual.items())))
                        print("实际结果是：%s" % dict(set(actual.items()) - set(expect.items())))
                        raise AssertionError
                elif data_type == "XML":
                    try:
                        assert expect in actual
                    except AssertionError:
                        print('预期结果不在实际结果中')
                    # self.assertIn(expect, actual, msg="预期不在实际中！")

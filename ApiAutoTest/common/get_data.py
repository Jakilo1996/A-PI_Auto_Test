# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ApiAutoTest
# FileName:     get_data.py
# Author:      Jakiro
# Datetime:    2021/3/5 12:01 下午
# Description: 此模块通过调用read_excel模块，实现所有用例的读取，每条用例组装成一个元祖，所有用例元祖组成一个列表
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

from common.read_excel import ReadExcel


def get_data():
    read_excel = ReadExcel()
    data_list = []
    for row in range(2, read_excel.get_row_count() + 1):
        case_id = read_excel.get_case_id(row)
        method = read_excel.get_case_method(row)
        url = read_excel.get_case_url(row)
        if_execute = read_excel.get_case_if_execute(row)
        precondition = read_excel.get_case_precondition_id(row)
        depend_key = read_excel.get_case_depend_field(row)
        pattern = read_excel.get_case_regular_expression(row)
        expect = read_excel.get_case_expected_outcome_value(row)
        data_type = read_excel.get_case_response_data_type(row)
        if if_execute == "Y":
            data_list.append(
                (case_id, method, url, if_execute, precondition, depend_key, pattern, expect, data_type, row))
    return data_list


if __name__ == '__main__':
    print(get_data())

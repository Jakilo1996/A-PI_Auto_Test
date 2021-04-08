# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ApiAutoTest
# FileName:     request_method.py
# Author:      Jakiro
# Datetime:    2021/3/5 5:45 下午
# Description:  通过requests模块组装请求，通过re模块筛选需要数据，调用ReadExcel类调用数据
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import requests, re
from common.read_excel import ReadExcel


class RequestMethod(object):
    def __init__(self):
        # 通过requests的session方法实例化一个session对象
        self.session = requests.session()
        # 实例化一个read_excel对象，用来进行表格数据读取操作
        self.read_execl = ReadExcel()

    # # 封装一个方法可以获得响应吗
    # def get_response_code(self):
    #
    # 封装一个方法，发送get和post请求
    def get_or_post(self, method, url, params=None):
        # 根据传入方法参数的不同，通过使用session对象的不同方法使用不同的请求类型进行请求
        # 方法的返回值是一个response对象
        if method == 'GET':
            return self.session.get(url=url, params=params, verify=False)

        elif method == 'POST':
            return self.session.post(url=url, data=params, verify=False)

        else:
            raise ValueError('请求类型不支持')

    # 封装一个方法，请求结果获取响应body，可以用于正则提取，或者断言，如果返回json对象则返回字典数据，如果返回xml对象则返回text属性
    def get_case_actual_result(self, method, url, response_data_type, params=None):
        # 通过调用类方法get_or_post 来获得当前请求的响应对象
        current_response = self.get_or_post(method=method, url=url, params=params)
        # 将响应的解码为utf8
        current_response.encoding = 'utf-8'
        # 打印响应的文本
        # print(current_response.text)
        # 根据形参response_data_type的值，来返回不同的数据类型
        if response_data_type == 'JSON':
            # 调用response对象的.json方法获得当前响应的json返回数据 返回值为dict类型
            return current_response.json()

        elif response_data_type == 'XML':
            # 返回response对象的text属性，获得text文本 返回值为str类型
            return current_response.text

        else:
            # 如果没有获得想要的参数，则抛出一个传入值错误
            raise ValueError('不支持响应数据类型')

    # 声明一个方法根据前置用例id返回前置用例的行号 row
    def get_case_precondition_row(self, row):
        # 通过调用read_excel的get_case_precondition_id方法 获得当前用例的前置用例id
        precondition_id = self.read_execl.get_case_precondition_id(row=row)
        # 遍历所有行号
        for row_01 in range(2, self.read_execl.get_row_count() + 1):
            # 通过read_excel的get_case_id的到当前遍历行号的用例id
            current_case_id = self.read_execl.get_case_id(row=row_01)
            # 对比当前遍历行号的id与当前用例前置用例的id 如果相同则此行号为当前用例前置用例的行号
            if current_case_id == precondition_id:
                precondition_row = row_01
                # 返回该行号
                return precondition_row

    # 声明一个方法根据前置用例的行号，获得前置用例的响应的结果 pre_row 返回值为响应的text或json的result
    def get_case_precondition_response_result(self, precondition_row):
        # 通过read_excel的get_response_data_type方法 获得前置用例的返回数据类型
        pre_case_response_data_type = self.read_execl.get_case_response_data_type(row=precondition_row)
        # 通过read_excel的get_case_method方法 获得前置用例的请求方法
        pre_case_method = self.read_execl.get_case_method(row=precondition_row)
        # 通过read_excel的get_case_url方法 获得前置用例的请求url
        pre_case_url = self.read_execl.get_case_url(row=precondition_row)
        # 通过read_excel的get_case_parameters_value 根据前置用例行号 获得前置用例的参数值
        pre_case_params = self.read_execl.get_case_parameters_value(row=precondition_row)
        # 通过调用类的get_actual方法 获得前置用例请求的响应结果
        precondition_row_response_result = self.get_case_actual_result(method=pre_case_method, url=pre_case_url,
                                                                       response_data_type=pre_case_response_data_type,
                                                                       params=pre_case_params)
        # 返回前置用例请求的响应结果
        return precondition_row_response_result

    # 声明一个方法，从响应中根据正则表达式提取value，与依赖字段组成键值对返回 pre_row dict数据类型
    def get_depend_key_value_items(self, row):
        # 调用类的get_case_precondition_row方法 获得前置用例的行号
        # print('当前行数', row)
        precondition_row = self.get_case_precondition_row(row=row)
        # 通过调用read_excel的get_case_depend_field方法 获得前置用例的依赖字段的key值
        depend_field_key = self.read_execl.get_case_depend_field(row=precondition_row)
        # 通过调用类的get_case_precondition_response_result方法 传入前置用例的行号 获得前置用例的响应结果
        pre_case_response_result = self.get_case_precondition_response_result(precondition_row=precondition_row)
        # 通过调用read_excel的get_case_regular_expression传入前置用例行号 获得前置用例的正则表达式
        pre_regular_expression = self.read_execl.get_case_regular_expression(row=precondition_row)
        # 通过前置用例的正则表达式以及前置用例的响应结果，进行正则匹配，获得需求的依赖字段的值
        depend_field_value = re.findall(pattern=pre_regular_expression, string=pre_case_response_result)[0]
        # 以字典类型返回当钱用例的依赖字段的key与value
        # print(depend_field_key, depend_field_value)
        return {depend_field_key: depend_field_value}

    # 声明一个方法，把正则表达式提取到的键值对，更新到请求参数中 row
    def update_case_params_depend_field(self, row):
        # 通过调用read_excel的get_case_parameters_value传入当前参数的行号，获得更新前的参数
        require_params = self.read_execl.get_case_parameters_value(row=row)
        # 通过调用类的get_depend_key_value_items获得当前用例的依赖字段的键值对
        depend_filed = self.get_depend_key_value_items(row=row)
        # 通过字典的update方法将依赖字段跟新到当前用例的所需参数中
        require_params.update(depend_filed)
        # 返回更新了依赖字段键值对的参数 作为当前用例的参数
        return require_params


if __name__ == '__main__':
    # 实例化request_method对象
    request_method = RequestMethod()
    # request_method.update_case_params_depend_field(8)
    read_excel = ReadExcel()

    # my_request = RequestMethod()
    # rows = [2, 3, 4, 5, 6, 7, 10]
    # for row in rows:
    #     method = read_excel.get_case_method(row=row)
    #     url = read_excel.get_case_url(row=row)
    #     params = read_excel.get_case_parameters_value(row)
    #     content_type = read_excel.get_response_data_type(row)
    #     print('当前响应数据类型')
    #     print(read_excel.get_case_id(row=row))
    #     print(my_request.get_actual_result(method=method, url=url, response_data_type=content_type, params=params))

    for row in range(4, request_method.read_execl.get_row_count() + 1):
        # 根据列表是否运行字段 如果字段的值为Y 那么执行当前行号用例
        if request_method.read_execl.get_case_if_execute(row=row) == "Y":
            print("现在开始执行第%d行的用例" % row)
            # 获得当前行号用例的方法
            method = request_method.read_execl.get_case_method(row)
            # 获得当前行号的url
            url = request_method.read_execl.get_case_url(row)
            # 获得当前用例的前置用例的id
            precondition_case_id = request_method.read_execl.get_case_precondition_id(row)
            # 获得当前用例的响应数据类型
            content_type = read_excel.get_case_response_data_type(row)
            # print("前置用例是：%s" % precondition_case_id)
            # 如果当前行号用例有前置用例 则调用request_method对象的update_case_params_depend_field方法 获得更新后参数
            if precondition_case_id:
                params = request_method.update_case_params_depend_field(row)
                # print(params)
            # 如果没有前置用例 则直接读取列表中的参数值
            else:
                params = request_method.read_execl.get_case_parameters_value(row)
            # 打印请求所需要的每个参数
            print(method, url, params)
            # 通过类的获得实际结果方法 将各个参数传入 霍霍响应的实际结果
            actual_result = request_method.get_case_actual_result(method=method, url=url, params=params,
                                                                  response_data_type=content_type, )
            # 打印实际结果

            response_data_type = request_method.read_execl.get_case_response_data_type(row)
            expect_result = request_method.read_execl.get_case_expected_outcome_value(row)
            if expect_result:
                # print(actual_result)
                if response_data_type == "JSON":
                    if expect_result == actual_result:
                        print("断言成功！")
                    else:
                        print("断言失败！")
                        print("预期结果是：%s" % dict(set(expect_result.items()) - set(actual_result.items())))
                        print("实际结果是：%s" % dict(set(actual_result.items()) - set(expect_result.items())))
                elif response_data_type == "XML":
                    if expect_result in actual_result:
                        print("断言成功！")
                    else:
                        print("断言失败！")

# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     main
# Author:      Jakiro
# Datetime:    2020/12/10 16:24
# Description:
# -----------------------------------------------------------------------------------
from case.login_test_case import Login_Test
from case.user_append_test_case import Useradd_test
from runner_test_case.test_case_runner import runner_manage


# 此模块主要实现根据测试方法不同，选择不同的用例执行方式，可以选择失败的单条用例进行回归执行，
# 也可以批量执行测试模块，也可根据测试类执行单测试类执行
class RanzhiTest(object):
    def lets_run_test(self):
        runner_manage(run_type='run_uts', mode_parameter='login_test_case.py', report_type='tr1')
        # 可选参数
        '''
           用来被测试的主函数调用
           :param run_type: 测试调用类型 'run_uts_single' 单例执行 'run_uts' 多模块执行 
           'run_test_classname' 测试类名执行 run_default_method 测试多模块执行
           :param report_type: 报告类型  htr tr1  tr2
           :param mode_parameter: 测试类型参数（每个类型不同）参数 单例：用例名  test_login_success_2_9527396399
           多模块一：模块名  后面跟模块名 *代表所有测试用例模块 匹配用例 必须有.py login_test_case.py'
           测试类名：测试类名 Login_Test
           多模块二：模块名 后面跟模块名 *代表所有测试用例模块 匹配用例 必须有.py login_test_case.py'
           :param email_title: 发送邮件的标题
           :param report_title: 生成报告的标题
           :param report_tester: 生成报告的作者
           :param report_desc: 生成报告的描述
           :param report_name: 生成的报告的命名
           :return: 函数没有返回值，主功能为执行用例，生成报告，发送邮件
        '''


if __name__ == '__main__':
    # RanzhiTest().lets_run_test()
    runner_manage(run_type='run_test_classname', mode_parameter=Useradd_test,
                  report_type='tr1', email_title='用户添加测试', report_title='用户添加测试')
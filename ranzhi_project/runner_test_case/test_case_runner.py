# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     test_case_runner
# Author:      Jakiro
# Datetime:    2020/12/9 16:18
# Description:
# -----------------------------------------------------------------------------------
import unittest

from unittestreport import TestRunner
from unittestreport.core.HTMLTestRunnerNew import HTMLTestRunner

from case.login_test_case import Login_Test
from common.send_email import SendEmail
from common.read_ini import ReadIni

import time

# 此模块主要定义了测试执行的用例加载方法，测试报告的生成模板，测试报告的邮件发送

class Runner_Test_Case(object):

    def __init__(self, run_type='run_test_classname', report_type='tr1', mode_parameter=Login_Test,
                 email_title='email标题',
                 report_title='测试报告标题', report_tester='Jakiro', report_desc='测试描述', report_name='report-{}.html'):
        # 找到测试用例的路径
        self.case_path = ReadIni().get_case_path()
        # 生成报告路径
        tt = time.strftime('%Y-%m-%d-%H-%M-%S')
        self.report_path = ReadIni().get_report_path() + report_name.format(tt)
        # 报告类型
        self.report_type = report_type
        # 用例加载类型
        self.run_type = run_type
        # 用例加载方式类型
        self.mode_parameter = mode_parameter
        # 邮件标题
        self.email_title = email_title
        # 报告标题
        self.report_title = report_title
        # 报告作者
        self.report_tester = report_tester
        # 报告描述
        self.report_desc = report_desc

    def runner_run_test_classname(self, test_classname):
        '''
        通过测试类名加载
        :param test_classname: 测试类名 TestLogin
        :return:
        '''
        # 添加多个用例方法3 通过用defaulttestloader类的方法 通过测试类名来加载 参数为一个类
        # 不需要实例化testsuite类 不需要case路径 直接通过测试类名
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_classname)
        return suite

    def runner_run_default_method(self, module_name):
        '''
        通过测试模块加载
        :param module_name: 测试模块名
        :return:
        '''
        # 添加多个用例方法2 用defaulttestloader类的方法 测试路径 用例模块名可以用*遍历所有模块
        # 不需要实例化testsuite类 'login_test_case.py'
        suite = unittest.defaultTestLoader.discover(self.case_path, pattern=module_name)
        return suite

    def runner_run_unittest_testsuite_single(self, case_name):
        '''
        通过用例名加载
        :param case_name: 测试用例名
        :return:
        '''
        # 实例化测试套件
        suite = unittest.TestSuite()

        # 运行单个用例参数   用例名

        suite.addTest(Login_Test(case_name))
        return suite

    def runner_run_unittest_testsuite(self, module_name):
        '''
        通过测试模块加载
        :param module_name: 测试模块名
        :return:
        '''
        # 实例化测试套件
        suite = unittest.TestSuite()
        # 添加多个用例方法1
        # 加载用例 对象.addtest加载一个 addtests加载多个 添加用例
        # 导入unittest的TestLoader的类 加载用例
        # 方法discover() 第一个填用例路径 选择用例
        # pattern匹配规则 后面跟模块名 *代表所有测试用例模块 匹配用例 必须有.py login_test_case.py'
        suite.addTests(unittest.TestLoader().discover(self.case_path, pattern=module_name))
        return suite

    def runner_run_type_control(self):
        '''
         通过测试类名，执行一组测试用例 参数为测试类
        三种 多个用例执行方式 1个单个用例执行方式
        通过共有属性run——type来控制用例加载方式
        :param
        :return:suite对象
        '''
        if self.run_type == 'run_uts_single':
            case_name = self.mode_parameter
            suite = self.runner_run_unittest_testsuite_single(case_name)

        elif self.run_type == 'run_uts':
            module_name = self.mode_parameter
            suite = self.runner_run_unittest_testsuite(module_name)

        elif self.run_type == 'run_test_classname':
            test_classname = self.mode_parameter
            # print(type(test_classname))
            suite = self.runner_run_test_classname(test_classname)

        elif self.run_type == 'run_default_method':
            module_name = self.mode_parameter
            suite = self.runner_run_default_method(module_name)

        else:
            raise TypeError('run_type is invalid')

        return suite

    def report_type_control(self, suite):
        '''
        通过 参数suite来发送报告，参数必须为suite对象 通过共有属性report_type来使用模板
        :param suite:
        :return:
        '''

        if self.report_type == "htr":
            # 打印存储报告  htmltestrunner  testrunner
            # 打印报告的第一种方法
            # 获取数据流 以二进制文件写入
            file_report = open(self.report_path, mode='wb')
            # 数据流 模板 报告名 描述 测试员（作者）
            # 实例化htr类
            html_test_runner = HTMLTestRunner(file_report, verbosity=2, title=self.report_title,
                                              description=self.report_desc, tester=self.report_tester)
            # 运行用例 参数为用例
            html_test_runner.run(suite)
            file_report.close()

        elif self.report_type == 'tr1':
            # 第二种方法
            # 参数 ：测试套件suite ， 报告文件名filename，报告文件路径report_dir，
            # 测试套件标题title，描述description，测试报告模板templates 1,2对应两种不赞同的模板
            test_runner_run = TestRunner(suite, self.report_path, self.report_path,
                                         title=self.report_title, desc=self.report_desc, tester=self.report_tester,
                                         templates=1)
            test_runner_run.run()

        elif self.report_type == 'tr2':
            # 第二种方法
            # 参数 ：测试套件suite ， 报告文件名filename，报告文件路径report_dir，
            # 测试套件标题title，描述description，测试报告模板templates 1,2对应两种不赞同的模板
            test_runner_run = TestRunner(suite, self.report_path, self.report_path,
                                         title=self.report_title, desc=self.report_desc, tester=self.report_tester,
                                         templates=2)
            test_runner_run.run()

        else:
            raise ValueError('report_type is wrong')

    def runner_function(self):
        '''
        用来控制runner的主流程方法 用例加载方式 报告发送模板 发送邮件
        :return:
        '''
        self.report_type_control(self.runner_run_type_control())
        time.sleep(10)
        email_title = self.email_title
        SendEmail().send_email(self.report_path, email_title)


def runner_manage(run_type='run_test_classname', report_type='tr1', mode_parameter=Login_Test,
                  email_title='email标题',
                  report_title='测试报告标题', report_tester='Jakiro',
                  report_desc='测试描述', report_name='report-{}.html'):
    '''
    用来被测试的主函数调用
    :param run_type: 测试调用类型
    :param report_type: 报告类型
    :param mode_parameter: 测试类型参数（每个类型不同）
    :param email_title: 发送邮件的标题
    :param report_title: 生成报告的标题
    :param report_tester: 生成报告的作者
    :param report_desc: 生成报告的描述
    :param report_name: 生成的报告的命名
    :return: 函数没有返回值，主功能为执行用例，生成报告，发送邮件
    '''
    runner1 = Runner_Test_Case(run_type=run_type, report_type=report_type, mode_parameter=mode_parameter,
                               email_title=email_title, report_title=report_title, report_tester=report_tester,
                               report_desc=report_desc, report_name=report_name)
    runner1.runner_function()


if __name__ == '__main__':
    # # 实例化Runner_Test_Case类
    # runner = Runner_Test_Case()
    # # 通过类方法运行测试用例
    # runner.runner_run_case()

    # 自定义4种用例运行方法
    # 测试类名驱动
    # runner_run_method('test_classname', 'tr2', Login_Test)
    # 单用例名 驱动
    # runner_run_method('single_case', 'tr2', 'test_login_success_0_9527258742')

    # Runner_Test_Case('run_test_classname', 'tr2', Login_Test).report_type_control()
    # Runner_Test_Case('run_default_method', 'tr2', 'login_test_case.py').report_type_control()
    # Runner_Test_Case('run_uts', 'tr1', 'login_test_case.py').report_type_control()
    # Runner_Test_Case('run_uts_single', 'tr1', 'test_login_success_2_9527396399', '测试报告主题').runner_manage()
    # Runner_Test_Case('run_uts_single', 'tr1', 'test_login_success_2_9527396399', '测试报告标题题').runner_manage()
    # Runner_Test_Case().runner_manage()
    # Runner_Test_Case(run_type='run_test_classname', report_type='tr1',
    #                   mode_parameter=Login_Test, email_title='email标题',
    #                  report_title='测试报告标题', report_tester='Jakiro',
    #                  report_desc='测试描述', report_name='report-{}.html').runner_manage()
    runner_manage()

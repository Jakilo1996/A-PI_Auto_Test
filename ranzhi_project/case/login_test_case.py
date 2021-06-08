# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     login_testcase
# Author:      Jakiro
# Datetime:    2020/12/7 11:03
# Description:
# -----------------------------------------------------------------------------------


# 用户登录测试用例
from parameterized import parameterized

from common.get_path import get_file_path
from common.raed_yaml import read_yaml_data
from common.read_json import read_json_data
from common.read_sql import read_sql
from modules.login_page_module import Login_page
from common.read_excel import read_excel_data
from common.read_ini import ReadIni
from common.get_log import get_logging
import unittest
import time


# 登录相关测试类

class Login_Test(unittest.TestCase):
    # succeed_data_excel = read_excel_data(
    #     r'C:\Users\Administrator\codes\test\project\ranzhi_project\data_config\login_data.xlsx', 'test_login_success')
    # failed_data_excel = read_excel_data(
    #     r'C:\Users\Administrator\codes\test\project\ranzhi_project\data_config\login_data.xlsx', 'test_login_failed')
    # succeed_data_yaml = read_yaml_data(
    #     r'C:\Users\Administrator\codes\test\project\ranzhi_project\data_config\test_data.yaml')
    # succeed_data_json = read_json_data(get_file_path(r'ranzhi_project/data_config/test_data.json'))

    # 通过ReadIni类获取实例路径
    # succeed_data_excel = read_excel_data(ReadIni().get_excel_path(), 'test_login_success')
    login_data_json = read_json_data(ReadIni().get_json_path())
    # 实例化logging对象 参数为当前文件路径
    ttt = time.strftime('%Y-%m-%d-%H-%M-%S')
    current_test = 'login_test'
    current_logging = get_logging(ReadIni().get_logging_path() + 'logging-{}-{}.log'.format(current_test, ttt))
    login_data_yaml = read_yaml_data(ReadIni().get_yaml_path())

    # 通过setUp和tearDown固件进行用例配置
    def setUp(self):
        self.login_test = Login_page('Chrome')
        # print(self.succeed_data_lists)

    def tearDown(self):
        self.login_test.quit()

    # 通过setUpClass和tearDownClass固件进行用例配置
    # @classmethod  # 需要加装饰器，把他继承的cls改为self 可以放前置条件 和连接数据库
    # def setUpClass(self):
    #     self.login_test = Login_page('Chrome')
    #     # 连接数据库
    #
    # @classmethod
    # def tearDownClass(self):
    #     self.login_test.quit()

    @parameterized.expand(login_data_yaml['test_login_success'])
    # @parameterized.expand(succeed_data_excel)
    # @parameterized.expand(login_data_json['test_login_success'])
    # @parameterized.expand([[
    #     "9527258742",
    #     "123456",
    #     "李越川258742",
    #     "2"
    # ], ])
    def test_login_success(self, username, password, expectation, case_number, current_test_module):
        '''
        登录成功的用例
        :param username:
        :param password:
        :param expectation:
        :param case_number:
        :return:
        '''
        try:
            # 登录流程
            self.login_test.login(username, password)
            # 断言，获取文本n
            # actual_name = self.login_test.get_login_success_text()
            # 打印文本获取成功
            # self.current_logging.info('文本获取成功')
            # 通过数据库进行断言
            actual_name = read_sql(expectation)

            # 断言失败时，才会报错  先填期望，再填实际
            self.assertEqual(expectation, actual_name, '预期用户名与实际用户名结果不一致')
        except Exception as e:
            tt = time.strftime('%Y-%m-%d-%H-%M-%S')
            # print(tt,e)
            # 错误时调用base中的截图方法截图
            # self.login_test.get_screenshot_as_file(r'C:\Users\Administrator\codes\test\project\ranzhi_project\result\screenshot\screenshot--{}.png'.format(tt))
            self.login_test.get_screenshot_as_file(
                ReadIni().get_screen_shot_path() + "screenshot—-{}-{}-date-{}.png".format(current_test_module,
                                                                                          case_number, tt))
            # 错误时，通过实例化日志对象的.error方法，将后面的的message信息打印进日志，打印日志,并保存日志
            self.current_logging.error("{}}第{}用例出现错误，请排查".format(current_test_module, case_number))
            raise AssertionError("{}第{}用例出现错误，请排查".format(current_test_module, case_number))
            # 如果不是AssertError 会报Error A 会报failed为么同步用例执行结果，一般用A

        finally:
            try:
                self.login_test.check_out()
            except Exception:
                self.login_test.click_login_failed_box_accept()

    # @parameterized.expand(failed_data_excel)
    @parameterized.expand(login_data_yaml['test_login_failed'])
    def test_login_failed(self, username, password, selector, expectation, case_number, current_test_module):
        '''
        登录失败的用例
        :param username: 用户名
        :param password: 密码
        :param expectation: 期望结果
        :return:
        '''
        try:
            # 登录流程
            self.login_test.login(username, password)
            # 断言，获取警告窗文本
            # actual_alert_text = self.login_test.get_failed_alert_text()
            # 断言优化
            actual_alert_text = self.login_test.get_text(selector, wait=20)
            # 断言，警告窗文本对比
            # self.assertEqual(expectation, actual_alert_text, '预期用户名与实际用户名结果不一致')
            self.assertIn(expectation, actual_alert_text, '预期用户名与实际用户名结果不一致。。。')
            # self.assertTrue(expectation == actual_alert_text )
            # 后面需要填入一个bowl值表达式
        except:
            tt = time.strftime('%Y-%m-%d-%H:%M:%S')
            self.login_test.get_screenshot_as_file(
                ReadIni().get_screen_shot_path() + "screenshot—-{}-{}-date-{}.png".format(current_test_module,
                                                                                          case_number, tt))
            # 错误时，通过实例化日志对象的.error方法，将后面的的message信息打印进日志，打印日志,并保存日志
            self.current_logging.error("{}第{}用例出现错误，请排查".format(current_test_module, case_number))
            raise AssertionError('{}第{}条用例出错了快去查看'.format(current_test_module, case_number))


        finally:
            self.login_test.click_login_failed_box_accept()


if __name__ == '__main__':
    unittest.main()

# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     user_append_Case
# Author:      Jakiro
# Datetime:    2020/12/3 19:08
# Description:
# -----------------------------------------------------------------------------------

# 添加用户测试用例
from parameterized import parameterized
# from modules.login_page_module import Login_page
from common.get_log import get_logging
from common.raed_yaml import read_yaml_data
from common.read_excel import read_excel_data
import unittest
import time

from common.read_ini import ReadIni
from modules.useradd_page_module import Useradd_page


# 用户添加测试类
class useadd_test(unittest.TestCase):
    # succeed_add_user_data = read_excel_data(
    #     r'C:\Users\Administrator\codes\test\project\ranzhi_project\data_config\useradd_data.xlsx', 'useadd_success')
    # failed_add_user_data = read_excel_data(
    #     r'C:\Users\Administrator\codes\test\project\ranzhi_project\data_config\useradd_data.xlsx', 'useadd_failed')
    # 获得用户添加的yaml文件
    useadd_yaml_data = read_yaml_data(ReadIni().get_yaml_path())
    # 实例化logging类，获得日志生成路径 日志名为当前用例执行时间
    ttt = time.strftime('%Y-%m-%d-%H-%M-%S')
    current_test = 'useadd'
    current_logging = get_logging(ReadIni().get_logging_path() + 'logging-{}-{}.log'.format(current_test, ttt))

    @classmethod
    def setUpClass(self):
        # 登录动作 实例化类
        self.useadd_test = Useradd_page('Chrome')

    def setUp(self):

        self.useadd_test.login('admin', '123456')

    # def tearDown(self):
    #     self.useadd_test.chick_out_useadd()

    def tearDownClass(self):
        self.useadd_test.quit()

    # @parameterized.expand(succeed_add_user_data)
    # 参数化数据格式化
    # @parameterized.expand([('jakiro', '邱杰', '123456', '123456', '@qq.com', 'Jakiro')])
    # 通过yaml_data进行数据驱动
    @parameterized.expand(useadd_yaml_data['useadd_success'])
    def test_useadd_succeed(self, username, realname, password, confirm_password, email, expectation,
                            case_number, current_test_module):
        '''

        :param username: 用户名称
        :param realname: 用户真实姓名
        :param password: 用户密码
        :param confirm_password:再次确认密码
        :param email: 用户邮箱
        :param expectation: 期望用户名
        :return:
        '''
        try:
            # 添加成功动作
            self.useadd_test.useradd(username, realname, password, confirm_password, email)
            # 断言动作 获取最后一个数据的用户姓名文本
            actual_text = self.useadd_test.get_user_text()
            # 断言 实际用户姓名文本与输出用户姓名文本对比
            self.assertEqual(expectation, actual_text, '实际用户姓名与期望用户姓名不一致')
        except:
            tt = time.strftime('%Y-%m-%d-%H:%M:%S')
            self.useadd_test.get_screenshot_as_file(
                ReadIni().get_screen_shot_path() + "screenshot—{}-{}-{}.png".format(current_test_module, case_number,
                                                                                    tt))
            # 错误时，通过实例化日志对象的.error方法，将后面的的message信息打印进日志，打印日志,并保存日志
            self.current_logging.error("{}第{}用例出现错误，请排查".format(current_test_module, case_number))
            raise AssertionError('{}}第{}条用例出错了快去查看'.format(current_test_module, case_number))

    # 通过yaml文件进行数据驱动 key值为useadd_failed
    @parameterized.expand(useadd_yaml_data['useadd_failed'])
    def test_useadd_failed(self, username, realname, password, confirm_password, email, expectation,
                           prompt_selector, case_number, current_test_module):

        try:
            # 添加失败动作
            self.useadd_test.useradd(username, realname, password, confirm_password, email)
            # 断言动作 获取弹出的提示窗的文本
            actual_prompt_text = self.useadd_test.get_text(prompt_selector, wait=30)
            # 断言 实际提示窗文本与期望文本对比
            self.assertTrue(expectation == actual_prompt_text, '实际提示窗文本与期望文本不相等')
        except:
            tt = time.strftime('%Y-%m-%d-%H:%M:%S')
            self.useadd_test.get_screenshot_as_file(
                ReadIni().get_screen_shot_path() + "screenshot—-{}-{}-{}.png".format(current_test_module, case_number,
                                                                                     tt))
            # 错误时，通过实例化日志对象的.error方法，将后面的的message信息打印进日志，打印日志,并保存日志
            self.current_logging.error("{}第{}用例出现错误，请排查".format(current_test_module, case_number))
            raise AssertionError('{}第{}条用例出错了快去查看'.format(current_test_module, case_number))
        finally:
            self.useadd_test.chick_out_useadd()


if __name__ == '__main__':
    unittest.main()

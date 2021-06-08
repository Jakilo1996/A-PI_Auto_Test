# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     login_module01
# Author:      Jakiro
# Datetime:    2020/12/4 11:42
# Description:
# -----------------------------------------------------------------------------------

from common.base import Base
from common.raed_yaml import read_yaml_data
from time import sleep


class Login_page(Base):
    login_yaml_data = read_yaml_data(
        r'C:\Users\Administrator\codes\test\project\ranzhi_project\data_config\element_selector.yaml')
    
    def login(self, login_use, login_pw):
        try:
            sleep(2)
            # 输入登录用户
            self.send_keys(self.login_yaml_data['RanzhiLogin']['USERNAME'], login_use, Wait_time=20)
            # 输入密码
            self.send_keys(self.login_yaml_data['RanzhiLogin']['PWD'], login_pw, Wait_time=5)
            # 点击登录
            self.click(self.login_yaml_data['RanzhiLogin']['SUBMIT'], Wait_time=5)
            # sleep(3)
        except:
            raise NotImplementedError('登录错误')
            # sleep(30)
            # self.click('lt,签退', wait_time=20)
            # sleep(2)
            # # 输入登录用户
            # self.send_keys(self.login_yaml_data['RanzhiLogin']['USERNAME'], login_use, Wait_time=20)
            # # 输入密码
            # self.send_keys(self.login_yaml_data['RanzhiLogin']['PWD'], login_pw, Wait_time=5)
            # # 点击登录
            # self.click(self.login_yaml_data['RanzhiLogin']['SUBMIT'], Wait_time=5)

    def check_out(self):
        '''
        登陆成功后的签退
        :return:
        '''
        sleep(3)
        self.click('lt,签退', wait=True)

    def get_login_success_text(self):
        '''
        获取登录后的用户name文本
        :return: 返回真实姓名问本
        '''
        sleep(3)
        return self.get_text('x,//*[@id="mainNavbar"]/div/ul[1]/li/a', wait=True)

    def get_login_failed_alert_text(self):
        '''
        获取警告窗内容
        :return:
        '''
        sleep(3)
        return self.get_text('x,/html/body/div[2]/div/div/div[1]/div', wait=True)

    def click_login_failed_box_accept(self):
        sleep(3)
        self.click('x,/html/body/div[2]/div/div/div[2]/button')

if  __name__ == '__main__':
    Login_page('Chrome').login('admin', '123456')
    # Login('Chrome').login('admin','1')

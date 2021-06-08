# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     useradd_module
# Author:      Jakiro
# DateWait_time:    2020/12/3 19:09
# Description:
# -----------------------------------------------------------------------------------


import random
import datetime
from time import sleep

from common.raed_yaml import read_yaml_data
from modules.login_page_module import Login_page


class Useradd_page(Login_page):
    useradd_yaml_data = read_yaml_data(
        r'C:\Users\Administrator\codes\test\project\ranzhi_project\data_config\element_selector.yaml')

    def useradd(self, times, username, realname, password1, password2, email):
        i = 1
        # 定位后台系统 运用显示等待解决页面加载问题
        # ele_cms = WebDriverWait(self,3,0.2,ignored_exceptions='').until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s-menu-superadmin"]/button')))
        # ele_cms.click()
        self.click(self.useradd_yaml_data['AddUser']['ELE_CMS_BUTTON_SELECTOR'], Wait_time=3)
        # 切换到iframe中 两种方法
        # 通过iframe_id 进行切换 wd.switch_to.frame(iframe_id)
        # wd.switch_to.frame('iframe-superadmin')
        # 通过寻找框架位置切换
        # self.switch_to.frame(self.find_element(By.XPATH, '//*[@id="iframe-superadmin"]'))
        self.switch_to_frame(self.useradd_yaml_data['AddUser']['FRAME_SWITCH_SELECTOR'], Wait_time=3)
        # 定位添加成员
        self.click(self.useradd_yaml_data['AddUser']['ADD_MEMBER_BUTTON_SELECTOR'])
        # ele_append = self.find_element(By.XPATH, '//*[@id="shortcutBox"]/div/div[1]/div/a/h3')
        # ele_append.click()
        # sleep(3)
        # 循环添加学员
        while i < times:
            tt = datetime.datetime.now().microsecond
            # 定位用户名输入框
            self.send_keys(self.useradd_yaml_data['AddUser']['USERNAME_INPUT_SELECTOR'], username + str(tt))
            # ele_username_box = WebDriverWait(self, 3, 0.2, ignored_exceptions='').until(
            #     EC.visibility_of_element_located((By.XPATH, '//*[@id="account"]')))
            # ele_username_box.send_keys('9527' + str(tt))
            # 定位真实姓名输入框
            self.send_keys(self.useradd_yaml_data['AddUser']['REALNAME_INPUT_SELECTOR'], realname + str(tt))
            # ele_actual_name_box = self.find_element(By.XPATH, '//*[@id="realname"]')
            # ele_actual_name_box.send_keys('李越川' + str(tt))
            # 定位性别单选框 通过random.choice实现随机选择
            gender = self.useradd_yaml_data['AddUser']['GENDER_INPUT_SELECTOR']
            self.click('i,' + random.choice(gender))
            # ele_gender_box = self.find_element(By.ID, random.choice(gender))
            # ele_gender_box.click()

            # 通过二次定位 定位下拉框中的所有部门列表 然后通过随机数实现随机选择
            self.second_locator_element(self.useradd_yaml_data['AddUser']['DEPARTMENT_INPUT_SELECTOR1'],
                                        self.useradd_yaml_data['AddUser']['DEPARTMENT_INPUT_SELECTOR2'])
            # ele_department_lists = self.second_locator_element('i,dept','tn,option')
            # ele_department_lists = self.find_element(By.ID, 'dept').find_elements_by_tag_name('option')
            # .click()

            # 通过二次定位 定位下拉框中的所有角色元素 通过随机数实现随机选择
            self.second_locator_element('i,role', 'tn,option')
            # ele_role_lists = self.find_element(By.ID, 'role').find_elements_by_tag_name('option')
            # random.choice(ele_role_lists).click()

            # 定位密码输入框
            self.send_keys('i,password1', password1, wait=False)
            # ele_passcode_box = self.find_element(By.ID, 'password1')
            # ele_passcode_box.send_keys(password1)
            # 定位重复密码输入框
            self.send_keys('i,password2', password2, Wait_time=3)
            # ele_re_passcode_box = self.find_element(By.ID, 'password2')
            # ele_re_passcode_box.send_keys('123456')
            # 定位邮箱输入框
            self.send_keys('i,email', str(tt) + email, Wait_time=3)
            # ele_emial_box = self.find_element(By.ID, 'email')
            # ele_emial_box.send_keys(str(tt) + email)
            # 定位保存按钮
            self.click('i,submit', wait=True)
            # ele_submit1_button = self.find_element(By.ID, 'submit')
            # ele_submit1_button.click()
            sleep(3)
            # 输入页数
            self.send_keys('i,_pageID', '100', Wait_time=5)
            # 点击go
            self.click('i,goto', Wait_time=5)
            # 定位最后一个成员并断言
            user_name_element = 'body > div > div > div > div.col-md-10 > div > div > table > tbody > tr:last-child > td:nth-child(3)'
            user_name_text = self.get_text('css,' + user_name_element)
            print("实际结果是：{}，期望结果是：{}".format(user_name_text, username + str(tt)))
            assert user_name_text == username + str(tt)
            # print("实际结果是：{}，期望结果是：{}".format(user_name_text,"xiao"+str(tt)))
            i += 1
            # 定位添加成员按钮并点击
            self.click('plt,添加成员', wait=True)
            # ele_app_member_button = WebDriverWait(self, 3, 0.2, ignored_exceptions='').until(
            #     EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '添加成员')))
            # ele_app_member_button.click()

        self.quit()


if __name__ == '__main__':
    useradd = Useradd_page('Chrome')
    useradd.login('admin', '123456')
    useradd.useradd(3, '9527', '谷小姐', '123456', '123456', '@qq.com')

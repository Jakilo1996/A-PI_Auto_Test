# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     useradd_page_module
# Author:      Jakiro
# Datetime:    2020/12/7 23:11
# Description:
# -----------------------------------------------------------------------------------

import random
from time import sleep

from common.raed_yaml import read_yaml_data
from modules.login_page_module import Login_page


class Useradd_page(Login_page):
    useradd_yaml_data = read_yaml_data(
        r'C:\Users\Administrator\codes\test\project\ranzhi_project\data_config\element_selector.yaml')

    def useradd(self, username, realname, password1, password2, email):
        # i = 1
        # 定位后台系统 运用显示等待解决页面加载问题
        # ele_cms = WebDriverWait(self,3,0.2,ignored_exceptions='').until(EC.visibility_of_element_located((By.XPATH,'//*[@id="s-menu-superadmin"]/button')))
        # ele_cms.click()
        self.click(self.useradd_yaml_data['AddUser']['ELE_CMS_BUTTON_SELECTOR'], Wait_time=20)
        # 切换到iframe中 两种方法
        # 通过iframe_id 进行切换 wd.switch_to.frame(iframe_id)
        # wd.switch_to.frame('iframe-superadmin')
        # 通过寻找框架位置切换
        try:
            # self.switch_to.frame(self.find_element(By.XPATH, '//*[@id="iframe-superadmin"]'))
            sleep(2)
            self.switch_to_frame(self.useradd_yaml_data['AddUser']['FRAME_SWITCH_SELECTOR'], Wait_time=20)
            # 定位添加成员
            self.click(self.useradd_yaml_data['AddUser']['ADD_MEMBER_BUTTON_SELECTOR'], ignored='TimeoutException')
        except Exception as e:
            # 避免缓存签退重新登录
            # self.check_out()
            print(e)
            sleep(2)
            # # 输入登录用户
            # self.send_keys(self.login_yaml_data['RanzhiLogin']['USERNAME'], 'admin', Wait_time=20)
            # # 输入密码
            # self.send_keys(self.login_yaml_data['RanzhiLogin']['PWD'], '123456', Wait_time=5)
            # # 点击登录
            # self.click(self.login_yaml_data['RanzhiLogin']['SUBMIT'], Wait_time=5)
            # 重新定位后台按钮并切换重新登录
            # self.click(self.useradd_yaml_data['AddUser']['ELE_CMS_BUTTON_SELECTOR'], Wait_time=20)
            self.switch_to_frame(self.useradd_yaml_data['AddUser']['FRAME_SWITCH_SELECTOR'], Wait_time=30)
            raise TimeoutError('页面加载超时')

        finally:

            # ele_append = self.find_element(By.XPATH, '//*[@id="shortcutBox"]/div/div[1]/div/a/h3')
            # ele_append.click()
            # sleep(3)
            # 循环添加学员
            # while i < times:
            # tt = datetime.datetime.now().microsecond
            # 定位用户名输入框
            self.send_keys(self.useradd_yaml_data['AddUser']['USERNAME_INPUT_SELECTOR'], username)
            # ele_username_box = WebDriverWait(self, 3, 0.2, ignored_exceptions='').until(
            #     EC.visibility_of_element_located((By.XPATH, '//*[@id="account"]')))
            # ele_username_box.send_keys('9527' + str(tt))
            # 定位真实姓名输入框
            self.send_keys(self.useradd_yaml_data['AddUser']['REALNAME_INPUT_SELECTOR'], realname)
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
            self.second_locator_element(self.useradd_yaml_data['AddUser']['ROLE_INPUT_SELECTOR1'],
                                        self.useradd_yaml_data['AddUser']['ROLE_INPUT_SELECTOR2'])
            # ele_role_lists = self.find_element(By.ID, 'role').find_elements_by_tag_name('option')
            # random.choice(ele_role_lists).click()

            # 定位密码输入框
            self.send_keys(self.useradd_yaml_data['AddUser']['PASSWORD_INPUT_SELECTOR'], password1, wait=False)
            # ele_passcode_box = self.find_element(By.ID, 'password1')
            # ele_passcode_box.send_keys(password1)
            # 定位重复密码输入框
            self.send_keys(self.useradd_yaml_data['AddUser']['CONFIRM_PASSWORD_INPUT_SELECTOR'], password2, Wait_time=3)
            # ele_re_passcode_box = self.find_element(By.ID, 'password2')
            # ele_re_passcode_box.send_keys('123456')
            # 定位邮箱输入框
            self.send_keys(self.useradd_yaml_data['AddUser']['EMAIL_INPUT_SELECTOR'], email, Wait_time=3)
            # ele_emial_box = self.find_element(By.ID, 'email')
            # ele_emial_box.send_keys(str(tt) + email)
            # 定位保存按钮
            self.click(self.useradd_yaml_data['AddUser']['SUBMIT_BUTTON_SELECTOR'], wait=True)
            # ele_submit1_button = self.find_element(By.ID, 'submit')
            # ele_submit1_button.click()
            # sleep(5)

    def get_user_text(self):
        sleep(3)
        # 输入页数
        self.send_keys(self.useradd_yaml_data['AddUser']['PAGE_INPUT_SELECTOR'], '100', Wait_time=30)
        # 点击go
        self.click(self.useradd_yaml_data['AddUser']['GOTO_BUTTON_SELECTOR'], Wait_time=5)
        # 定位最后一个成员并断言
        user_name_element = self.useradd_yaml_data['AddUser']['LAST_USERNAME_SELECTOR']
        user_name_text = self.get_text('css,' + user_name_element, Wait_time=20)
        # print("实际结果是：{}，期望结果是：{}".format(user_name_text, username + str(tt)))
        # assert user_name_text == username + str(tt)
        # print("实际结果是：{}，期望结果是：{}".format(user_name_text,"xiao"+str(tt)))
        # i += 1
        # 定位添加成员按钮并点击
        # self.click(self.useradd_yaml_data['AddUser']['ADD_MEMBER_BUTTON_SELECTOR1'], wait=True)
        # ele_app_member_button = WebDriverWait(self, 3, 0.2, ignored_exceptions='').until(
        #     EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '添加成员')))
        # ele_app_member_button.click()
        return user_name_text

    def chick_out_useadd(self):
        # 添加成员在框架内 ，要跳转到最外层框架
        self.switch_to_default_content()
        print('切换成功')
        sleep(3)
        self.click('lt,签退', wait=5)
        print('签退成功')
        sleep(3)


if __name__ == '__main__':
    # useradd = Useradd_page('Chrome')
    # useradd.login('admin', '123456')
    # useradd.useradd('95272', '谷小姐', '123456', '123456', '12332244@qq.com')
    # useradd.quit()
    useradd = Useradd_page('Chrome')
    useradd.login('admin', '123456')
    useradd.useradd('9527', 'qjj', '123', '123', '213213')
    useradd.chick_out_useadd()

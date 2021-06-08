# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     User_Append_case
# Author:      Jakiro
# Datetime:    2020/12/3 15:12
# Description:
# -----------------------------------------------------------------------------------


import random
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
# 提供until方法
from selenium.webdriver.support import expected_conditions as EC
# 提供EC类
from selenium.webdriver.common.by import By

# 实例化浏览器对象
wd = webdriver.Chrome()
# 进入登录界面
wd.get('http://127.0.0.1/ranzhi/sys/user-login.html')
# 最大化窗口
wd.maximize_window()
# 设置隐式等待时间
wd.implicitly_wait(30)
time = 5
i = 0

try:
    # 定位用户输入框
    ele_uesrid_box = wd.find_element(By.ID, 'account')
    ele_uesrid_box.send_keys('admin')
    # 定位密码输入框
    ele_password_box = wd.find_element(By.ID, 'password')
    ele_password_box.send_keys('123456')
    # 定位登录按钮
    ele_submit_botton = wd.find_element(By.ID, 'submit')
    ele_submit_botton.click()
    # 定位后台系统 运用显示等待解决页面加载问题
    ele_cms = WebDriverWait(wd, 3, 0.2, ignored_exceptions='').until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="s-menu-superadmin"]/button')))
    ele_cms.click()
    # 切换到iframe中 两种方法
    # 通过iframe_id 进行切换 wd.switch_to.frame(iframe_id)
    # wd.switch_to.frame('iframe-superadmin')
    # 通过寻找框架位置切换
    wd.switch_to.frame(wd.find_element(By.XPATH, '//*[@id="iframe-superadmin"]'))
    # 定位添加学员
    ele_append = wd.find_element(By.XPATH, '//*[@id="shortcutBox"]/div/div[1]/div/a/h3')
    ele_append.click()
    # 循环添加学员
    while i < time:
        tt = datetime.datetime.now().microsecond
        # 定位用户名输入框
        ele_username_box = WebDriverWait(wd, 3, 0.2, ignored_exceptions='').until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="account"]')))
        ele_username_box.send_keys('9527' + str(tt))
        # 定位真实姓名输入框
        ele_actual_name_box = wd.find_element(By.XPATH, '//*[@id="realname"]')
        ele_actual_name_box.send_keys('李越川' + str(tt))
        # 定位性别单选框 通过random.choice实现随机选择
        gender = ['genderm', 'genderf']
        ele_gender_box = wd.find_element(By.ID, random.choice(gender))
        ele_gender_box.click()

        # 通过二次定位 定位下拉框中的所有部门列表 然后通过随机数实现随机选择
        ele_department_lists = wd.find_element(By.ID, 'dept').find_elements_by_tag_name('option')
        random.choice(ele_department_lists).click()

        # 通过二次定位 定位下拉框中的所有角色元素 通过随机数实现随机选择
        ele_role_lists = wd.find_element(By.ID, 'role').find_elements_by_tag_name('option')
        random.choice(ele_role_lists).click()

        # 定位密码输入框
        ele_passcode_box = wd.find_element(By.ID, 'password1')
        ele_passcode_box.send_keys('123452')
        # 定位重复密码输入框
        ele_re_passcode_box = wd.find_element(By.ID, 'password2')
        ele_re_passcode_box.send_keys('123456')
        # 定位邮箱输入框
        ele_emial_box = wd.find_element(By.ID, 'email')
        ele_emial_box.send_keys(str(tt) + '212@qq.com')
        # 定位保存按钮
        ele_submit1_button = wd.find_element(By.ID, 'submit')
        ele_submit1_button.click()
        i += 1
        # 定位添加成员按钮并点击
        ele_app_member_button = WebDriverWait(wd, 3, 0.2, ignored_exceptions='').until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '添加成员')))
        ele_app_member_button.click()
        # 点导航
        wd.find_element(By.XPATH,'//*[@id="mainNavbar"]/div/a').click()
        # 切出框架
        wd.switch_to.default_content()
        # 点后台
        ele_cms = WebDriverWait(wd, 3, 0.2, ignored_exceptions='').until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="s-menu-superadmin"]/button')))
        ele_cms.click()
        # 切入框架
        wd.switch_to.frame(wd.find_element(By.XPATH, '//*[@id="iframe-superadmin"]'))
        # 定位添加成员按钮并点击
        ele_app_member_button = WebDriverWait(wd, 3, 0.2, ignored_exceptions='').until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '添加成员')))
        ele_app_member_button.click()


        # # 签退
        # wd.switch_to.default_content()
        # wd.find_element(By.LINK_TEXT, '签退').click()
        # sleep(3)
        # # 定位用户输入框
        # ele_uesrid_box = wd.find_element(By.ID, 'account')
        # ele_uesrid_box.send_keys('admin')
        # # 定位密码输入框
        # ele_password_box = wd.find_element(By.ID, 'password')
        # ele_password_box.send_keys('123456')
        # # 定位登录按钮
        # ele_submit_botton = wd.find_element(By.ID, 'submit')
        # ele_submit_botton.click()
        # 定位
        # sleep(3)
        # wd.switch_to.frame(wd.find_element(By.XPATH, '//*[@id="iframe-superadmin"]'))
        # 定位添加学员

        ele_username_box = WebDriverWait(wd, 3, 0.2, ignored_exceptions='').until(
             EC.visibility_of_element_located((By.XPATH, '//*[@id="account"]')))
        ele_username_box.send_keys('9527' + str(tt))
        sleep(20)

finally:
    print('添加成功')
    sleep(3)
    wd.quit()

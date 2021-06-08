# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   ranzhi_project
# FileName:     base
# Author:      Jakiro
# DateWait_time:    2020/12/4 10:10
# Description:
# -----------------------------------------------------------------------------------
import random
from time import sleep

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# webdriver相关方法

class Base(object):
    def __init__(self, browser_type):
        if browser_type == 'Chrome':
            self.wd = webdriver.Chrome()
        elif browser_type == "Firefox":
            self.wd = webdriver.Firefox()
        elif browser_type == 'Ie':
            self.wd = webdriver.Ie()
        else:
            raise TypeError('浏览器类型错误')
        # 调用进入网址方法
        self.wd.get('http://127.0.0.1/ranzhi/sys/user-login.html')
        # 调用最大化窗口方法
        self.wd.maximize_window()
        # 调用设置隐式等待方法
        # self.wd.implicitly_wait(30)

    def get(self, url):
        """
        获取网址
        :param url:
        :return:
        """
        self.wd.get(url)

    def maximize_window(self):
        """
        窗口最大化
        :return:
        """
        self.wd.maximize_window()

    def implicitly_wait(self, Wait_time):
        """
        设置隐式等待时间
        :return:
        """
        self.wd.implicitly_wait(Wait_time)

    def _convert_selector_to_locator(self, selector):
        """
        :param selector(string):
        :return(By,value):
        """

        selector_type = selector.split(',')[0].strip()
        selector_value = selector.split(',')[1].strip()
        if selector_type == 'i' or selector_type == 'ID':
            locator = (By.ID, selector_value)

        elif selector_type == 'x' or selector_type == 'XPATH':
            locator = (By.XPATH, selector_value)

        elif selector_type == 'n' or selector_type == 'NAME':
            locator = (By.NAME, selector_value)

        elif selector_type == 'cn' or selector_type == 'CLASS_NAME':
            locator = (By.CLASS_NAME, selector_value)

        elif selector_type == 'css' or selector_type == 'CSS_SELECTOR':
            locator = (By.CSS_SELECTOR, selector_value)

        elif selector_type == 'tn' or selector_type == 'TAG_NAME':
            locator = (By.TAG_NAME, selector_value)

        elif selector_type == 'lt' or selector_type == 'LINK_TEXT':
            locator = (By.LINK_TEXT, selector_value)

        elif selector_type == 'plt' or selector_type == 'PARTIAL_LINK_TEXT':
            locator = (By.PARTIAL_LINK_TEXT, selector_value)

        else:
            raise TypeError(selector_type + 'is invalid string')

        return locator

    def locator_element(self, selector, Wait_time=0, wait=True, ignored=''):
        """
        :param locator(by,value):
        :return web_element:
        """
        locator = self._convert_selector_to_locator(selector)
        if Wait_time > 0:
            return WebDriverWait(self.wd, Wait_time, 0.2, ignored_exceptions=ignored).until(
                EC.visibility_of_element_located(locator),
                message='元素查找超时')
        elif Wait_time == 0:
            if wait:
                return WebDriverWait(self.wd, 5, 0.2).until(EC.visibility_of_element_located(locator), message='元素查找超时')
            else:
                return self.wd.find_element(*locator)
        else:
            raise ValueError('输入时间非法')

    def send_keys(self, selector, text, Wait_time=0, wait=True):
        """
        输入
        :param selector:
        :param text:
        :return:
        """
        input_ele = self.locator_element(selector, Wait_time, wait)
        input_ele.clear()
        input_ele.send_keys(text)

    def click(self, selector, Wait_time=3, wait=True, ignored=''):
        """
        点击操作
        :param selector:
        :return:
        """
        self.locator_element(selector, Wait_time, wait, ignored).click()

    def switch_to_frame(self, selector, Wait_time=0, wait=True):
        '''
        跳转frame框架
        :return:
        '''
        ele = self.locator_element(selector)
        if Wait_time > 0:
            return WebDriverWait(self.wd, Wait_time, 0.2).until(EC.frame_to_be_available_and_switch_to_it(ele),
                                                                message='元素查找超时')
        elif Wait_time == 0:
            if wait:
                return WebDriverWait(self.wd, 5, 0.2).until(EC.frame_to_be_available_and_switch_to_it(ele),
                                                            message='元素查找超时')
            else:
                return self.switch_to_frame(ele)
        else:
            raise ValueError('输入时间非法')

    def select_by_visible_text(self, selector, text):
        '通过文本选择下拉框'
        Select(self.locator_element(selector)).select_by_visible_text(text)

    def select_by_index(self, selector, num):
        """
        通过下标索引选择下拉框
        :param selector:
        :param num:
        :return:
        """
        Select(self.locator_element(selector)).deselect_by_index(num)

    def select_by_value(self, selector, value):
        """
        通过value选择下拉框
        :param selector:
        :param num:
        :return:
        """
        Select(self.locator_element(selector)).deselect_by_value(value)

    def second_locator_element(self, selector1, selector2, Wait_time=0, wait=True):
        """
        二次定位并自动点击
        :param selector1:
        :param selector2:
        :return:
        """
        locator1 = self._convert_selector_to_locator(selector1)
        locator2 = self._convert_selector_to_locator(selector2)
        if Wait_time > 0:
            eles = self.locator_element(*locator1, Wait_time, wait).find_elements(*locator2)
        elif Wait_time == 0:
            if wait:
                eles = self.wd.find_element(*locator1).find_elements(*locator2)
            else:
                eles = self.wd.find_element(*locator1).find_elements(*locator2)
        else:
            raise ValueError('输入时间非法')
        random.choice(eles).click()

    def get_text(self, selector, Wait_time=0, wait=True):
        """
        获得文本
        :return:
        """
        sleep(8)
        return self.locator_element(selector, Wait_time, wait).text

    def quit(self):
        """
        退出浏览器进程
        :return:
        """
        sleep(2)
        # print('退出准备')
        self.wd.quit()

    def get_screenshot_as_file(self, filename):
        '''
        截图,用with open打开文件，如果路径错误，不报错，直接关闭
        :param filename:文件路径
        :return:
        '''
        self.wd.get_screenshot_as_file(filename)

    def switch_to_alert(self, mode, text='None'):
        """
        弹窗接收
        :param selector:
        :param Wait_time:
        :param wait:
        :return:
        """
        alert = self.wd.switch_to.alert()
        if mode == 'text':
            return alert.text

        if mode == 'accept':
            return alert.accept()

        if mode == 'dismiss':
            return alert.dismiss()

        if mode == 'sendkeys':
            return alert.sendkeys(text)

    def switch_to_default_content(self):
        return self.wd.switch_to.default_content()

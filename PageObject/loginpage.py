# -*- coding: utf-8 -*-
# @Time    : 2021/9/1 19:32
# @Author  : CuiShuangqi
# @Email   : 1159533975@qq.com
# @File    : baiduIndex.py
from Common.basePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class LoginIndex(BasePage):
    """
    页面元素
    """
    # 日清首页链接
    riqing_index_url = "http://10.189.0.78/warning-service/"
    # 姓名输入框
    name_input = (By.ID, "username")
    # 密码输入框
    password_input= (By.ID, "password")
    #确认登录按钮
    submit_btn = (By.ID, "submit")
    #登录名
    name="43347"
    #密码
    password="BW@jason8854"
    # 登录操作
    def login(self):
        self.logger.info("【===登录操作===】")
        # 等待用户名文本框元素出现
        self.wait_eleVisible(self.name_input, model='姓名输入框')
        # 输入姓名
        self.input_text(self.name_input, self.name, model="姓名输入框")
        # 输入密码
        self.input_text(self.password_input, text=self.password, model='密码框')
        # 点击登录
        # self.click_element((By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[3]'), model='点击父元素')
        js = 'document.getElementById({}).click();'.format(self.submit_btn)
        self.driver.execute_script(js)
        # self.click_element(self.submit_btn, model='点击登录')
        # 搜索后等待界面加载完成
        self.driver.implicitly_wait(10)
        sleep(3)

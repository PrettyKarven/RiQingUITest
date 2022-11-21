# -*- coding: utf-8 -*-
# @Time    : 2021/9/1 19:32
# @Author  : CuiShuangqi
# @Email   : 1159533975@qq.com
# @File    : baiduIndex.py
from selenium.webdriver import Keys

from Common.basePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep
import datetime


class WeekplanIndex(BasePage):
    """
    页面元素
    """
    # 左侧导航栏<我的计划>按钮
    # myplan_ele=(By.ID, "firstPageAction")
    weekplan_ele=(By.LINK_TEXT, "周计划管理")
    #周计划管理iframe元素
    weekplan_iframe=(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div[2]/iframe")
    #新建按钮元素
    # addplan_ele=(By.CLASS_NAME, "layui-btn addWeek")
    addplan_ele=(By.XPATH, "/html/body/div[2]/div[1]/form/div/dive/button[2]")
    #下拉框元素
    select_ele=(By.XPATH, "//*[@id='add-body']/tr/td[1]/div/div")
    #小类元素
    xiaolei_ele=(By.XPATH, "//*[@id='add-body']/tr/td[1]/div/div/div/ul/li[2]")
    #周计划添加框元素
    textarea_ele=(By.XPATH, "//*[@id='add-body']/tr/td[2]/textarea")
    #保存按钮元素
    save_ele=(By.XPATH, "//*[@id='main']/div/div/button[2]")



    #打开添加日清弹出框
    def add_weekplan(self):
        self.logger.info("【===添加周计划操作===】")
        # 点击左侧导航栏<周计划管理>按钮
        self.click_element(self.weekplan_ele, model='<周计划管理>按钮')
        # 设置元素等待
        self.driver.implicitly_wait(30)
        # 切换到周计划iframe
        self.switch_iframe(self.weekplan_iframe, model='<周计划iframe>')
        #点击新建按钮
        self.click_element(self.addplan_ele,model='新建按钮')
        # 修改小类下拉框的属性为选中
        self.setAttribute(self.find_element(self.select_ele), 'class', 'chosen-container chosen-container-single chosen-with-drop chosen-container-active')
        #选择小类
        self.click_element(self.xiaolei_ele,model='选择小类')
        #周计划输入框输入内容
        self.input_text(self.textarea_ele,text='测试周计划内容'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),model="输入周计划内容")
        #点击保存
        self.click_element(self.save_ele,model="保存周计划")
        sleep(3)





    # #获取提示消息
    # def getmsg(self):
    #     sleep(1)
    #     return self.get_text(self.msg,model='获取消息提示框信息')

    # #判断元素是否存在
    # def isisEleExist(self):
    #     return self.isElementExist()
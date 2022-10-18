# -*- coding: utf-8 -*-
# @Time    : 2021/9/1 19:32
# @Author  : CuiShuangqi
# @Email   : 1159533975@qq.com
# @File    : baiduIndex.py
from Common.basePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class PlananalysisIndex(BasePage):
    """
    页面元素
    """
    # 开始时间
    startDate = (By.ID, "startDate")
    # 结束时间
    endDate = (By.ID, "endDate")
    # 搜索按钮
    btnSearch = (By.ID, "btnSearch")
    #计划分析元素
    planal_ele= (By.XPATH,'/html/body/div[1]/div[2]/div/ul[1]/li[1]/dl/dd[2]/a')
    #计划分析iframe
    planal_iframe= (By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div[4]/iframe')

    # 查询操作
    def query_plan(self, search_key):
        self.logger.info("【===搜索大类操作===】")
        # 点击左侧导航栏<我的计划>按钮
        self.click_element(self.planal_ele, model='<我的计划>按钮')
        # 设置元素等待
        self.driver.implicitly_wait(30)
        # 切换到我的计划iframe
        self.switch_iframe(self.planal_iframe, model='<我的计划iframe>')
        # 设置元素等待
        self.driver.implicitly_wait(30)
        #点击搜索
        self.click_element(self.btnSearch)
        # 搜索后等待界面加载完成
        self.driver.implicitly_wait(10)

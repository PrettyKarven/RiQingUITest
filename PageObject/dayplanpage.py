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


class DayplanIndex(BasePage):
    """
    页面元素
    """
    # 左侧导航栏<我的计划>按钮
    myplan_ele=(By.ID, "firstPageAction")
    #我的计划iframe元素
    myplan_iframe=(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div[1]/iframe")
    #添加按钮元素
    addplan_ele=(By.ID, "insertDayPlan")
    #添加框iframe元素
    addpage_iframe=(By.XPATH,'//*[contains(@id,"layui-layer-iframe")]')
    #常用小类下拉框元素
    common_select=(By.XPATH,'/html/body/div[2]/div/form/div[1]/div/div')
    #常用小类下拉框元素
    commonxiaolei_ele=(By.XPATH, '/html/body/div[2]/div/form/div[1]/div/div/dl/dd[1]')
    #大类下拉框元素
    dalei_select=(By.XPATH,'/html/body/div[2]/div/form/div[2]/div/div')
    #大类下拉框item元素
    dalei_ele=(By.XPATH, '/html/body/div[2]/div/form/div[2]/div/div/dl/dd[text()="{}"]')
    #中类下拉框元素
    zhonglei_select=(By.XPATH,'/html/body/div[2]/div/form/div[3]/div/div')
    #中类下拉框item元素
    zhonglei_ele=(By.XPATH,'/html/body/div[2]/div/form/div[3]/div/div/dl/dd[text()="{}"]')
    #小类下拉框元素
    xiaolei_select=(By.XPATH,'/html/body/div[2]/div/form/div[4]/div/div')
    #小类下拉框item元素
    xiaolei_ele=(By.XPATH,'/html/body/div[2]/div/form/div[4]/div/div/dl/dd[text()="{}"]')
    # 成本类型下拉框元素
    costtype_ele=(By.XPATH,'/html/body/div[2]/div/form/div[5]/div/div')
    #成本类型item元素
    costitem_ele=(By.XPATH, '/html/body/div[2]/div/form/div[5]/div/div/dl/dd[text()="{}"]')
    #工作计划内容元素
    planContent_ele=(By.ID,'PlanContent')
    #计划用时元素
    chengNuoDate_ele = (By.ID, 'ChengNuoDate')
    #提交按钮元素
    submitplanbtn_ele=(By.ID,'saveSumDayPlan')
    #添加后消息提示框元素
    msg=(By.XPATH,'//*[@id="layui-layer2"]/div')
    #删除按钮元素
    deletedayplan_ele=(By.XPATH,'/html/body/div[2]/div[1]/div[1]/button[2]')
    #删除输入框
    searchinpt_ele=(By.ID,'searchWord')


    #打开添加日清弹出框
    def base_operation(self):
        self.logger.info("【===添加日清操作===】")
        # 点击左侧导航栏<我的计划>按钮
        self.click_element(self.myplan_ele, model='<我的计划>按钮')
        # 设置元素等待
        self.driver.implicitly_wait(30)
        # 切换到我的计划iframe
        self.switch_iframe(self.myplan_iframe, model='<我的计划iframe>')
        # 设置元素等待
        self.driver.implicitly_wait(30)
        # 点击添加按钮
        self.click_element(self.addplan_ele, model='添加按钮')
        # 设置元素等待
        self.driver.implicitly_wait(30)
        sleep(3)
        # 回到主页面（由于添加框页面是一个新的iframe，所以需要切换到主页面，重新切换到添加框iframe才能进行添加操作）
        self.driver.switch_to.default_content()
        # 设置元素等待
        self.driver.implicitly_wait(30)
        # 切换添加框iframe元素
        self.switch_iframe(self.addpage_iframe, model='切换添加框iframe')
        # 设置元素等待
        self.driver.implicitly_wait(30)

    # 添加计划外日清操作，选择常用小类
    def addriqing_unplanned(self):
        self.base_operation()
        # 修改常用小类下拉框的属性为选中
        # self.setAttribute(self.commonxiaolei_ele,'class','layui-form-select layui-form-selected')
        self.setAttribute(self.find_element(self.common_select),'class','layui-form-select layui-form-selected')
        # 点击常用小类下拉框元素
        self.click_element(self.commonxiaolei_ele,model='选择常用小类')
        # 修改成本类型下拉框的选中属性
        # self.setAttribute(self.costtype_ele,'class','layui-form-select layui-form-selected')
        self.setAttribute(self.find_element(self.costtype_ele),'class','layui-form-select layui-form-selected')
        # 选择建设类型
        list_ele = list(self.costitem_ele)
        list_ele[1] = self.costitem_ele[1].format('建设及其他成本')
        self.click_element(tuple(list_ele),model='建设成本类型')
        # 点击提交按钮
        self.click_element(self.submitplanbtn_ele,model='提交成功')
        # 搜索后等待界面加载完成
        self.driver.implicitly_wait(10)

    #添加计划内日清,手动选择大中小类
    def addriqing_planned(self,dalei='实施项目',zhonglei='BW003(项目制)',xiaolei='日清测试小类',chengnuodate=1):
        self.base_operation()
        # 修改大类下拉框的属性为选中
        self.setAttribute(self.find_element(self.dalei_select), 'class', 'layui-form-select layui-form-selected')
        # 选择大类
        dalei_elelist = list(self.dalei_ele)
        dalei_elelist[1] = self.dalei_ele[1].format(dalei)
        self.click_element(tuple(dalei_elelist), model='选择大类')
        # 修改中类下拉框的属性为选中
        self.setAttribute(self.find_element(self.zhonglei_select), 'class', 'layui-form-select layui-form-selected')
        #选择中类
        zhonglei_elelist = list(self.zhonglei_ele)
        zhonglei_elelist[1] = self.zhonglei_ele[1].format(zhonglei)
        self.click_element(tuple(zhonglei_elelist), model='选择中类')
        # 修改小类下拉框的属性为选中
        self.setAttribute(self.find_element(self.xiaolei_select), 'class', 'layui-form-select layui-form-selected')
        # 选择小类
        xiaolei_elelist = list(self.xiaolei_ele)
        xiaolei_elelist[1] = self.xiaolei_ele[1].format(xiaolei)
        self.click_element(tuple(xiaolei_elelist), model='选择小类')
        # 修改成本类型下拉框的选中属性
        self.setAttribute(self.find_element(self.costtype_ele), 'class', 'layui-form-select layui-form-selected')
        # 选择建设类型
        list_ele = list(self.costitem_ele)
        list_ele[1] = self.costitem_ele[1].format('建设及其他成本')
        self.click_element(tuple(list_ele), model='建设成本类型')
        #输入工作计划内容
        self.input_text(self.planContent_ele,'自动化测试计划内容<'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'>',model='计划内容')
        #输入计划工时
        self.input_text(self.chengNuoDate_ele,chengnuodate,model='计划工时')
        # 点击提交按钮
        self.click_element(self.submitplanbtn_ele, model='提交成功')
        # 搜索后等待界面加载完成
        self.driver.implicitly_wait(10)

    #删除第一条日计划
    def delete_myplan(self):
        self.logger.info("【===删除第一条日计划操作===】")
        # 点击左侧导航栏<我的计划>按钮
        self.click_element(self.myplan_ele, model='<我的计划>按钮')
        # 设置元素等待
        self.driver.implicitly_wait(30)
        # 切换到我的计划iframe
        self.switch_iframe(self.myplan_iframe, model='<我的计划iframe>')
        # 设置元素等待
        self.driver.implicitly_wait(30)
        # #选择第一条日清
        # self.setAttribute(self.find_element((By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/div/div')),'class','layui-unselect layui-form-checkbox layui-form-checked')
        #选中第一条数据
        self.click_element((By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[1]'))
        #点击删除按钮
        self.click_element(self.deletedayplan_ele,model='删除第一条日清')
        #点击确认按钮
        self.click_element((By.XPATH, '//*[@id="layui-layer1"]/div[3]/a[1]'))
        # 设置元素等待
        self.driver.implicitly_wait(30)

    #查询日清
    def query_myplan(self,searchWord='hahah '):
        self.logger.info("【===查询日计划操作===】")
        # 点击左侧导航栏<我的计划>按钮
        self.click_element(self.myplan_ele, model='<我的计划>按钮')
        # 设置元素等待
        self.driver.implicitly_wait(30)
        # 切换到我的计划iframe
        self.switch_iframe(self.myplan_iframe, model='<我的计划iframe>')
        # 设置元素等待
        self.driver.implicitly_wait(30)
        #输入检索内容
        self.input_text(self.searchinpt_ele,searchWord,model='输入搜索内容')
        #回车操作
        self.find_element(self.searchinpt_ele).send_keys(Keys.ENTER)


    #获取提示消息
    def getmsg(self):
        return self.get_text(self.msg,model='获取消息提示框信息')
#coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PageObject.loginpage import LoginIndex
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Common.basePage import BasePage
from selenium.webdriver.support.select import Select

if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get("http://10.189.0.78/warning-service/")
    driver.maximize_window()


    lgoin1=LoginIndex(driver)
    # lgoin1.login()
    lgoin1.input_text((By.ID, "username"),"43347")
    lgoin1.input_text((By.ID, "password"),"BW@jason8854")
    time.sleep(1)
    lgoin1.click_element((By.ID, "submit"))
    lgoin1.click_element((By.ID, "firstPageAction"))
    # driver.implicitly_wait(30)
    lgoin1.switch_iframe((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div[1]/iframe"))
    driver.implicitly_wait(30)
    time.sleep(3)
    lgoin1.click_element((By.ID, "insertDayPlan"))
    driver.implicitly_wait(30)
    # time.sleep(3)
    #回到主页面
    driver.switch_to.default_content()
    driver.implicitly_wait(30)
    time.sleep(3)
    # lgoin1.find_element((By.XPATH, '//*[contains(@id,"layui-layer-iframe")]'))
    lgoin1.switch_iframe((By.XPATH,'//*[contains(@id,"layui-layer-iframe")]'))
    driver.implicitly_wait(30)
    # lgoin1.find_element((By.XPATH,'//*[contains(@id,"layui-layer-iframe")]'))
    # lgoin1.click_element((By.ID, 'saveSumDayPlan'))
    #定位下拉框元素
    # ele = lgoin1.driver.find_element(By.ID, 't_service_outline')
    # select=Select(ele)
    # # select.select_by_index(2)
    # select.select_by_value('人力资源')
    # lgoin1.click_element((By.ID, 'saveSumDayPlan'))
    # #修改下拉框的属性为选中
    # lgoin1.setAttribute(lgoin1.find_element((By.XPATH,'/html/body/div[2]/div/form/div[1]/div/div')),'class','layui-form-select layui-form-selected')
    # #点击下拉框元素
    # # lgoin1.find_element((By.XPATH,'/html/body/div[2]/div/form/div[1]/div/div/dl/dd[3]'))
    # lgoin1.click_element((By.XPATH,'/html/body/div[2]/div/form/div[1]/div/div/dl/dd[text()="内控建设"]'))
    #修改大类下拉框属性值
    lgoin1.setAttribute(lgoin1.find_element((By.XPATH,'/html/body/div[2]/div/form/div[2]/div/div')),'class','layui-form-select layui-form-selected')
    #选择大类的值
    lgoin1.click_element((By.XPATH, '/html/body/div[2]/div/form/div[2]/div/div/dl/dd[text()="实施项目"]'))
    #修改成本类型下拉框的选中属性
    lgoin1.setAttribute(lgoin1.find_element((By.XPATH,'/html/body/div[2]/div/form/div[5]/div/div')),'class','layui-form-select layui-form-selected')
    #选择建设类型
    lgoin1.click_element((By.XPATH, '/html/body/div[2]/div/form/div[5]/div/div/dl/dd[text()="建设及其他成本"]'))
    # #点击提交按钮
    # lgoin1.click_element((By.ID,'saveSumDayPlan'))
    # time.sleep(5)
    # lgoin1.get_text((By.XPATH,'//*[@id="layui-layer2"]/div'))
    # print(lgoin1.get_text((By.XPATH,'//*[@id="layui-layer2"]/div')))







# See PyCharm help at https://www.jetbrains.com/help/pycharm/

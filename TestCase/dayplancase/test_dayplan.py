# -*- coding: utf-8 -*-
# @Time    : 2021/9/1 19:37
# @Author  : CuiShuangqi
# @Email   : 1159533975@qq.com
# @File    : test_001_login.py
import os
import time
import pytest
import allure
from time import sleep
from selenium import webdriver
from PageObject.loginpage import LoginIndex
from PageObject.dayplanpage import DayplanIndex
import datetime


@allure.feature("新建计划")
# @pytest.mark.usefixtures('start_session')
class TestAddMyPlan:
    @allure.story("如果9点之前新建计划内，否则新建计划内")
    @pytest.mark.addriqing
    # @pytest.mark.run(order=2)
    def test_addriqing(self,start_session):
        if datetime.datetime.now().hour < 9:
            start_session[2].info("【===创建计划内日计划===】")
            start_session[1].addriqing_planned()
        else:
            start_session[2].info("【===创建计划外日计划===】")
            start_session[1].addriqing_unplanned()
        assert "提交成功" == start_session[1].getmsg()

@allure.feature("删除计划")
class TestDeleteMyPlan:
    @allure.story("删除第一条日计划")
    def test_delriqing(self,start_session):
        start_session[1].delete_myplan()
        assert '删除成功'==start_session[1].getmsg()

@allure.feature("查询计划")
class TestQueryMyPlan:
    @allure.story("查询日计划")
    def test_queryriqing(self,start_session):
        start_session[1].query_myplan()



if __name__ == '__main__':
    # 当前时间
    now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
    # allure 测试报告路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    report_path = os.path.join(os.path.dirname(cur_path), f'Report\\{now_time}')
    print(111)
    # -s : 打印信息
    # -m ：运行含标签的用例
    pytest.main(["-vs", "-m", "test_dayplan.py::TestDeleteMyPlan", "--alluredir",'../report'])
    # TODO 执行: allure serve ./Report 解析测试报告
    os.system(f"allure serve {report_path}")
    # 执行多个标签
    # pytest.main(["-s", "-m", "login or test_demo", "test_001_login.py::TestLogin"])

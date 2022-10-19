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
from TestDatas.DayPlan_Datas import add_riiqng_datas as ar


@allure.feature("新建计划")
# @pytest.mark.usefixtures('start_session')
class TestAddMyPlan:
    @allure.story("如果9点之前新建计划内，否则新建计划内")
    @pytest.mark.addriqing
    @pytest.mark.parametrize("data",ar.riqing_data)
    # @pytest.mark.run(order=2)
    def test_addriqing(self,start_session,data):
        if datetime.datetime.now().hour < 9:
            start_session[2].info("【===创建计划内日计划===】")
            start_session[1].addriqing_planned(dalei=data["dalei"],zhonglei=data["zhonglei"],xiaolei=data["xiaolei"],chengnuodate=data["chengnuodate"])
        else:
            start_session[2].info("【===创建计划外日计划===】")
            start_session[1].addriqing_unplanned(dalei=data["dalei"],zhonglei=data["zhonglei"],xiaolei=data["xiaolei"],chengnuodate=data["chengnuodate"])
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





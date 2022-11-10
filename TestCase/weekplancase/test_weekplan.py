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


@allure.feature("新建周计划")
# @pytest.mark.usefixtures('start_session')
class TestAddWeekPlan:
    @allure.story("新建周计划")
    @pytest.mark.addriqing
    # @pytest.mark.run(order=2)
    def test_addweekplan(self,start_session):
        start_session[2].info("【===创建周计划===】")
        start_session[1].add_weekplan()





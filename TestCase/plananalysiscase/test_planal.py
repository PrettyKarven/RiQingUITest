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
from selenium.webdriver.common.by import By

from PageObject.loginpage import LoginIndex
from PageObject.dayplanpage import DayplanIndex
import datetime


@allure.feature("查询")
# @pytest.mark.usefixtures('start_session')
class TestQueryPlan:
    @allure.story("查询大类")
    # @pytest.mark.run(order=2)
    def test_queryplan(self,start_session):
        start_session[1].query_plan()
        assert not start_session[1].isElementExist((By.XPATH,'/html/body/div[3]/div[1]/div[1]/div/div[1]/div[2]/div')),'查询结果为空'







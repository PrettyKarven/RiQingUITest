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


@allure.feature("查询")
# @pytest.mark.usefixtures('start_session')
class TestQueryPlan:
    @allure.story("查询大类")
    # @pytest.mark.run(order=2)
    def test_queryplan(self,start_session):
        start_session[1].query_plan()
        assert "提交成功" == start_session[1].getmsg()





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
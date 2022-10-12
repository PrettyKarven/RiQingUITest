# -*- coding: utf-8 -*-
import pytest
from Utils.myLog import MyLog
from PageObject.loginpage import LoginIndex
from PageObject.dayplanpage import DayplanIndex


logger = MyLog().getLog()


@pytest.fixture(scope='class')
def start_session(project_session_start):
    '''
    所有模块只打开一次浏览器
    :param project_session_start: 所有模块只打开一次浏览器
    :return: driver MP
    '''
    logger.info("==========开始执行测试用例集===========")
    logger.info("----------前置操作：登录日清系统-----------")
    global driver
    driver = project_session_start
    logger.info("---" + str(driver))
    driver.get(LoginIndex.riqing_index_url)
    LoginIndex(driver).login()
    MP = DayplanIndex(driver)
    logger.info("----------前置操作完成：登录日清系统-----------")
    yield (driver, MP)
    logger.info("==========结束执行测试用例集===========")
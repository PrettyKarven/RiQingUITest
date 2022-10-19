# -*- coding: utf-8 -*-
import pytest
from Utils.myLog import MyLog
from PageObject.loginpage import LoginIndex
from PageObject.plananalysispage import PlananalysisIndex


logger = MyLog().getLog()


@pytest.fixture(scope='module')
def start_session(project_session_start):
    '''
    所有模块只打开一次浏览器
    :param project_session_start: 所有模块只打开一次浏览器
    :return: driver MP
    '''
    logger.info("==========开始执行***计划分析***测试用例集===========")
    logger.info("----------前置操作：登录日清系统-----------")
    global driver
    driver = project_session_start
    logger.info("---" + str(driver))
    driver.get(LoginIndex.riqing_index_url)
    LoginIndex(driver).login()
    PA = PlananalysisIndex(driver)
    logger.info("----------前置操作完成：登录日清系统-----------")
    yield (driver, PA, logger)
    logger.info("==========结束***计划分析***测试用例集===========")
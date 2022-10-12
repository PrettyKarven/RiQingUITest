# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from Utils.myLog import MyLog


logger = MyLog().getLog()


@pytest.fixture(scope='session')
def project_session_start():
    logger.info("==========开始 日清项目 执行测试===========")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    logger.info("==========结束 日清项目 测试===========")
# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: pytest

import pytest
from Base.android.BasePage import BasePage
from Base.BaseInitPath import InitPath
from Base.BaseReadConfig import ReadConfig
from Base.BaseLog import Log
import time
import os

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


# 定义命令行传参参数
def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="device", help="None")


# 命令行参数传递给pytest
@pytest.fixture(scope="session")
def cmdopt(request):
    return request.config.getoption("--cmdopt")


# 初始化开始连接设备
@pytest.fixture(scope="session")
def MyDriver(cmdopt):
    # 初始化日志
    log = Log()
    log.set_logger(cmdopt, setLevel='info')

    # 初始化设备
    basepage = BasePage()
    basepage.set_driver(cmdopt)
    basepage.set_openfastinput_ime()

    # 获取apk名启动
    rc = ReadConfig()
    driver = basepage.d.session(rc.get_apk_name())

    return_dict = {
        'basepage': basepage,
        'driver': driver,
        'log': log
    }
    yield return_dict
    print("driver finished")
    basepage.set_original_ime()
    driver.close()

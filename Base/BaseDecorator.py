# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: logging

from Base.BaseLog import Log
from functools import wraps
from time import localtime
import time
import os
from Base.android.BasePage import BasePage
from Base.BaseInitPath import InitPath
import allure

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
log = Log()


# 错误截图
def _failToImage(name):
    now = time.strftime('%Y.%m.%d.%H.%M.%S', localtime(time.time()))
    screen_shot = now + '_' + name + '_' + '.PNG'
    image_path = os.path.join(InitPath().get_report_path(), screen_shot)
    print(image_path)
    d = BasePage().get_driver()
    d.screenshot(image_path)
    return image_path
    # return d.screenshot(image_path)
    # allure.attach(body=d.screenshot(image_path), name='error pic', attachment_type=allure.attachment_type.PNG)
    # return screen_shot


# 测试步骤装饰器
def myTestSteps(func):
    @wraps(func)
    def wraper(*args, **kwargs):
        try:
            log.i(f'-->{func.__qualname__}')
            result = func(*args, **kwargs)
            return result
        except AssertionError as e:
            log.e(f'AssertionError {e}')
            log.e(f'\t<--{func.__qualname__}, AssertionError, Error')
            raise AssertionError(e)
        except Exception as e:
            log.e(f'Exception {e}')
            log.e(f'\t<--{func.__qualname__}, Exception, Error')
            raise Exception(e)

    return wraper


# 测试用例装饰器
def myTestCases(func):
    @wraps(func)
    def wraper(*args, **kwargs):
        try:
            log.d(f'-->{func.__qualname__}')
            result = func(*args, **kwargs)
            log.d(f'<--{func.__qualname__}, Success')
            return result
        except AssertionError as e:
            log.e(f'AssertionError {e}')
            log.e(f'\t<--{func.__qualname__}, AssertionError, Fail')
            # _failToImage(func.__qualname__)
            with open(_failToImage(func.__qualname__), 'rb') as file:
                file = file.read()
                # now = time.strftime('%Y.%m.%d.%H.%M.%S', localtime(time.time()))
                allure.attach(body=file, name=func.__qualname__ + '_Fail_img', attachment_type=allure.attachment_type.PNG)
            # allure.attach(body=_failToImage(func.__qualname__), name=_failToImage(func.__qualname__), attachment_type=allure.attachment_type.PNG)
            raise AssertionError(e)
        except Exception as e:
            log.e(f'Exception {e}')
            log.e(f'\t<--{func.__qualname__}, Exception, Error')
            raise Exception(e)

    return wraper


if __name__ == '__main__':
    # BasePage.set_driver('3EP7N19320003888')
    # _failToImage('nihao')
    BasePage.set_driver('3EP7N19320003888')
    report_path = InitPath()
    # report_path = ReportPath()
    path = PATH('../Report')
    path_time = os.path.join(path, time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime(time.time())))
    report_path.set_params(path_time, log_path='../Log')
    _failToImage('N18')

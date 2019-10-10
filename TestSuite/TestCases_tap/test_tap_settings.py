# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: allure, pytest, pytest-repeat

import allure
from Base.BaseDecorator import myTestCases
import pytest
from PageObjects.Page_tap.login_tap import Login

@myTestCases
@pytest.mark.repeat(1)
@allure.feature("group_call")
@allure.story("login")
def test001_login(MyDriver):
    '''登入选择单位'''
    login = Login()
    login.wait_page(MyDriver['driver'])
    assert 1 == 2

    # MyDriver['driver'].xpath('//*[@resource-id="com.taptap:id/home_head_portrait"]/android.widget.ImageView[1]').click()

# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: uiautomator2

from Base.android.BasePage import BasePage
from Base.BaseDecorator import myTestSteps


class Login(BasePage):
    @myTestSteps
    def wait_page(self, driver):
        driver.xpath('//*[@resource-id="com.taptap:id/home_head_portrait"]/android.widget.ImageView[1]').click()

    def input_login_info(self):
        pass

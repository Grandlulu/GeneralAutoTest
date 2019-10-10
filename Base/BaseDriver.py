# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: uiautomator2
from Base.android.BasePage import BasePage
from Base.BaseLog import Log
import time
import uiautomator2 as u2


# class MyDriver():
#     @staticmethod
#     def initDriver(uuid):
#         '''
#         :return: basepage, log
#         '''
#         basepage = BasePage()
#         basepage.set_driver(uuid)
#
#         log = Log()
#         log.set_logger(name=uuid, setLevel='info')
#
#         basepage.d.shell('logcat -c')
#         time.sleep(1)
#         basepage.d.shell('logcat -d > /sdcard/logcat.log')
#
#
#
#
#     def connectDevice(self):
#         self.basepage.set_fastinput_ime()
#         self.driver = self.basepage.d.session(self.apkName)
#         yield
#         self.basepage.set_original_ime()
#         self.driver.close()
#         self.log.d('driver close')

# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: uiautomator2

import os
import configparser

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
config_path = PATH('../config.ini')

print(config_path)

class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path, 'utf-8')

    def get_to_email(self):
        res = self.cf.get('EMAIL', 'to_addr')
        return res

    def get_email_subject(self):
        res = self.cf.get('EMAIL', 'email_subject')
        return res

    def get_admin_account(self):
        res = self.cf.get('EMAIL', 'admin_addr')
        return res

    def get_admin_password(self):
        res = self.cf.get('EMAIL', 'admin_psw')
        return res


    def get_apk_path(self):
        res = self.cf.get('APP', 'apk_path')
        return res

    def get_apk_url(self):
        res = self.cf.get('APP', 'apk_url')
        return res

    def get_apk_name(self):
        res = self.cf.get('APP', 'apk_name')
        return res

    def get_test_suite(self):
        res = self.cf.get('TESTDATA', 'test_suite')
        return res

if __name__ == '__main__':
    rc = ReadConfig()
    print(type(rc.get_to_email()))
    print(rc.get_apk_name())
    # from Base.android.BasePage import BasePage
    # from Base.BaseLog import Log
    # bp = BasePage()
    # log = Log()
    # bp.set_driver('3EP7N19320003888')
    # log.set_logger('3EP7N19320003888')
    # bp.app_install_ll()
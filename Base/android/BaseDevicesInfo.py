# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: 获取手机的硬件信息

import uiautomator2 as u2
import os
import re


# 获取手机UUID
def get_devices_serial_list():
    device_serial_list = []
    ADB_devices = os.popen('adb devices').readlines()
    for i in (range(len(ADB_devices)-2)):
        device_serial = re.findall(r'^\w*', ADB_devices[i+1])[0]
        device_serial_list.append(device_serial)
    return device_serial_list


# 获取手机信息
def get_device_info(device):
    driver = u2.connect(f'{device}')
    result = driver.device_info
    print(result)
    return result


# 获取手机分辨率
def get_device_pix(device):
    driver = u2.connect(f'{device}')
    pix = driver.device_info['display']
    print(pix)
    return pix


# 获取手机电池信息
def get_device_battery(device):
    driver = u2.connect(f'{device}')
    battery = driver.device_info['battery']
    print(battery)
    return battery


if __name__ == '__main__':
    # for i in get_devices_serial_list():
    #     phone = get_device_info(i)
    #     phone_name = phone['brand'] + '_' + phone['model'] + '_' + phone['version']
    #     print(phone_name)
    get_device_info('3EP7N19320003888')
# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: uiautomator2

from Base.BaseRunCase import RunCase
from Base.android.BaseDevicesInfo import get_devices_serial_list

if __name__ == '__main__':
    runner = RunCase()
    device_list = get_devices_serial_list()
    print(device_list)
    runner.run(device_list)


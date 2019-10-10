# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: logging


import os
import logging
import time
from time import localtime
from Base.BaseInitPath import InitPath

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class Log(object):
    @classmethod
    def set_logger(cls, name, setLevel='debug'):
        '''
        :param name: 日志名称
        :param setLevel: 设置日志打印级别（info，debug, error, critical, warning）
        :return:
        '''
        levels = {
            'info': logging.INFO,
            'debug': logging.DEBUG,
            'error': logging.ERROR,
            'critical': logging.CRITICAL,
            'warning': logging.WARNING
        }

        logger = logging.getLogger()
        logger.setLevel(levels[setLevel])

        # 输出格式
        Formatter = logging.Formatter(f'%(asctime)s  - {name} - %(levelname)s - %(message)s')

        # 日志路径设置
        log_path = InitPath().get_log_path()
        # path = PATH('../Log/')
        # file = time.strftime('%Y.%m.%d.%H.%M.%S', localtime(time.time())) + '-' + name + '.log'
        # cls.log_path = os.path.join(path, file)

        # 添加文件handle
        fh = logging.FileHandler(filename=log_path, encoding='utf-8')
        fh.setLevel(levels[setLevel])

        # 添加流handle
        st = logging.StreamHandler()
        st.setLevel(logging.DEBUG)

        fh.setFormatter(Formatter)
        st.setFormatter(Formatter)

        logger.addHandler(fh)
        logger.addHandler(st)

        cls.logger = logger

    # def get_log_path(self):
    #     return self.log_path

    def d(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def i(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def c(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def e(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def w(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    # def __init__(self, device):
    #     '''
    #     :param device: Phone serial number
    #     '''
    #
    #     # 生成日志路径
    #     phone = get_device_info(device)
    #     phoneName = phone['brand'] + '_' + phone['model'] + '_' + phone['version']
    #     resultPath = PATH('../Log/')
    #     logPath = os.path.join(resultPath, (phoneName + '_' + time.strftime('%Y%m%d%H%M%S', time.localtime())))
    #     if not os.path.exists(logPath):
    #         os.makedirs(logPath)
    #
    #     # 实例化log类
    #     self.logger = logging.getLogger()
    #     self.logger.setLevel(logging.INFO)
    #
    #     # 设置日志handle
    #     file = logging.FileHandler(os.path.join(logPath, f'{phoneName}.log'))
    #     formatt = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
    #     file.setFormatter(formatt)
    #     self.logger.addHandler(file)
    #
    #     # 运行前清空手机缓存日志
    #     cmdClear = 'adb -s' + device + 'logcat -c'
    #     subprocess.run(cmdClear, shell=True)
    #
    #     # 获取手机实时日志
    #     crashPath = os.path.join(PATH("../Log/CrashInfo/Android/"))
    #     if not os.path.exists(crashPath):
    #         os.makedirs(crashPath)
    #     logcatLog = os.path.join(crashPath, "logcat.log")
    #     cmdLogcat = 'adb -s ' + device + f' logcat > {logcatLog}'
    #     print(cmdLogcat)
    #     subprocess.run(cmdLogcat, shell=True)


if __name__ == '__main__':
    log = Log()
    log.set_logger('3EP7N19320003888', setLevel='info')
    print(log.get_log_path())
    # log.d('hello')
    # log.i('this is info')
    # log.d('this is a debug')
    # Log = Log.set_logger('3EP7N19320003888')
    # Log.d('hellow')

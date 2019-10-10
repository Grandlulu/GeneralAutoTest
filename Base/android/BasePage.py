# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: uiautomator2

import uiautomator2 as u2
import time
import os
import subprocess
from uiautomator2 import UiObjectNotFoundError
from Base.BaseLog import Log
from Base.BaseReadConfig import ReadConfig

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
log = Log()
rc = ReadConfig()


class BasePage(object):
    @classmethod
    def set_driver(cls, adder):
        '''
        :param adder: 既可以为设备uuid，也可以填写同一网段设备的ip地址
        '''
        cls.d = u2.connect(adder)

    def get_driver(self):
        return self.d

    # 截图
    def screenshot_ll(self, report_path):
        '''
        :param report_path: 截图存放路径
        :return: None
        '''
        date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screenshot_name = 'Manual_' + date_time + '.PNG'
        path = os.path.join(report_path, screenshot_name)
        log.i(f'screen shot saved in {path}')
        self.d.screenshot(screenshot_name)

    # 打开元素监控
    def watch_device_ll(self, keyword):
        '''
        存在元素则自动点击
        keyword = yes|允许|好的|跳过
        '''
        self.d.watchers.watched = False
        for i in keyword.split("|"):
            self.d.watcher(i).when(text=i).click(text=i)
        log.i('Starting watcher,parameter is %s' % keyword.split("|"))
        # print('Starting watcher,parameter is %s' % keyword.split("|"))
        self.d.watchers.watched = True
        time.sleep(2)

    # 关闭元素监控
    def disable_watcher_ll(self):
        # print('stop watchers')
        log.i('stop watchers')
        self.d.watchers.remove()
        self.d.watchers.watched = False

    # 安装apk包
    def app_install_ll(self):
        self.watch_device_ll('允许|继续安装|允许安装|始终允许|安装|重新安装|完成')
        # file_path = PATH('..\\..\\APK_Package\\')
        # APK_Path = os.path.join(file_path, packageName)
        APK_Path = os.path.abspath(rc.get_apk_path())
        log.i(f'apk install from path : {APK_Path}')
        # print(APK_Path)
        subprocess.Popen(f'adb install -r {APK_Path}', shell=True, close_fds=True)
        time.sleep(20)
        self.disable_watcher_ll()
        log.i('apk install success')
        # print('apk install finished')

    # 通过url安装apk包
    def app_install_url_ll(self):
        '''url example: https://d.taptap.com/latest'''
        url = rc.get_apk_url()
        log.i(f'apk install from url : {url}')
        self.watch_device_ll('允许|继续安装|允许安装|始终允许|安装|重新安装|完成')
        self.d.app_install(url)
        self.disable_watcher_ll()
        log.i('apk install success')

    # 返回
    def back_ll(self):
        time.sleep(1)
        self.d.press('back')
        time.sleep(1)

    # 等待页面
    def wait_page_ll(self, activity):
        self.d.wait_activity(activity=activity, timeout=10)

    # 唤醒设备
    def wakeup_device_ll(self):
        try:
            self.d.unlock()
            log.i('screen has been waked up')
            # print('screen has been waked up')
        except Exception as e:
            log.e(f'Exception: {e}')
            raise Exception(e)
            # print(f'Wakeup failed : {e}')

    def get_toast_message_ll(self):
        message = self.d.toast.get_message(3, 3)
        self.d.toast.reset()
        return message

    # 在手机上显示提示信息
    def toast_show_ll(self, text, duration):
        self.d.toast.show(text, duration)

    # 打开通用键盘
    def set_openfastinput_ime(self):
        self.d.set_fastinput_ime(True)

    # 关闭通用键盘
    def set_original_ime(self):
        self.d.set_fastinput_ime(False)

    # # 输入文字信息
    # def send_keys_ll(self, keys):
    #     try:
    #         self.d.set_fastinput_ime(True)
    #         self.d.send_keys(keys)
    #         self.d.set_fastinput_ime(False)
    #     except Exception as e:
    #         print(f'Send key event failed : {e}')

    # 获取手机分辨率
    def _get_phone_size(self):
        size = self.d.window_size()
        x = size[0]
        y = size[1]
        return x, y

    # 获取元素的各坐标点
    def _get_element_size(self, text_element):
        result = text_element.info['bounds']
        print(result)
        x_left = result['left']
        x_right = result['right']
        y_top = result['top']
        y_down = result['bottom']
        x_center = (x_left + x_right) / 2
        y_center = (y_top + y_down) / 2
        return x_left, x_right, y_top, y_down, x_center, y_center

    # 滑动
    def _swipe(self, Fx, Fy, Tx, Ty, steps):
        '''Fx(from x)缩写，其他类推；
        steps：1 steps 为 5ms；数字越小，滑动越快'''
        return self.d.swipe(Fx, Fy, Tx, Ty, steps)

    # 向上滑动
    def swipe_up(self, text_element=None, steps=0.2):
        """
        element: 有值时，坐标定位在元素内部滑动
        element: None 坐标为整机全屏内滑动
        """
        if text_element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(text_element)
            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_up
        else:
            x, y = self._get_phone_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.5 * x
            toY = 0.25 * y
        self._swipe(fromX, fromY, toX, toY, steps)

    # 向下滑动
    def swipe_down(self, text_element=None, steps=0.2):
        """
        element: 有值时，坐标定位在元素内部滑动
        element: None 坐标为整机全屏内滑动
        """
        if text_element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(text_element)
            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_down
        else:
            x, y = self._get_phone_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.5 * x
            toY = 0.75 * y
        self._swipe(fromX, fromY, toX, toY, steps)

    # 向左滑动
    def swipe_left(self, text_element=None, steps=0.2):
        """
        element: 有值时，坐标定位在元素内部滑动
        element: None 坐标为整机全屏内滑动
        """
        if text_element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(text_element)
            fromX = x_center
            fromY = y_center
            toX = x_left
            toY = y_center
        else:
            x, y = self._get_phone_size()
            fromX = 0.50 * x
            fromY = 0.5 * y
            toX = 0.25 * x
            toY = 0.5 * y
            print(fromX, fromY, toX, toY)
        self._swipe(fromX, fromY, toX, toY, steps)

    # 向右滑动
    def swipe_right(self, text_element=None, steps=0.2):
        """
        element: 有值时，坐标定位在元素内部滑动
        element: None 坐标为整机全屏内滑动
        """
        if text_element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(text_element)
            fromX = x_center
            fromY = y_center
            toX = x_right
            toY = y_center
        else:
            x, y = self._get_phone_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.75 * x
            toY = 0.5 * y
            print(fromX, fromY, toX, toY)
        self._swipe(fromX, fromY, toX, toY, steps)

    # 滑动查找元素
    def _find_element_by_swipe(self, dirction, text_element, swipe_times, swipe_by_element, steps=0.2):
        '''
        :param dirction: 滑动的方向包括: up, down, left, right
        :param textElement:需要寻找的元素 exp：d(text='settings')
        :param swipeTimes: 滑动的次数
        :param swipeByElement:定位一个text元素滑动
        :param steps: 滑动速度，数值越小滑动越快
        :return:
        '''
        for i in range(swipe_times):
            try:
                result = self.d(text=f'{text_element}')
                if result.exists:
                    return result
                else:
                    log.e(f'Error: {UiObjectNotFoundError}')
                    raise UiObjectNotFoundError
            except UiObjectNotFoundError:
                if dirction == 'up':
                    self.swipe_up(swipe_by_element, steps)
                elif dirction == 'down':
                    self.swipe_down(swipe_by_element, steps)
                elif dirction == 'left':
                    self.swipe_left(swipe_by_element, steps)
                elif dirction == 'right':
                    self.swipe_right(swipe_by_element, steps)
                if i == swipe_times - 1:
                    log.e(f'Error: {UiObjectNotFoundError}')
                    raise UiObjectNotFoundError

    # 向上滑动查找元素
    def find_element_by_swipe_up(self, text_element, swipe_times, swipe_by_element=None, steps=0.2):
        return self._find_element_by_swipe('up', text_element, swipe_times, swipe_by_element, steps)

    # 向下滑动查找元素
    def find_element_by_swipe_down(self, text_element, swipe_times, swipe_by_element=None, steps=0.2):
        return self._find_element_by_swipe('down', text_element, swipe_times, swipe_by_element, steps)

    # 向左滑动查找元素
    def find_element_by_swipe_left(self, text_element, swipe_times, swipe_by_element=None, steps=0.2):
        return self._find_element_by_swipe('left', text_element, swipe_times, swipe_by_element, steps)

    # 向右滑动查找元素
    def find_element_by_swipe_right(self, text_element, swipe_times, swipe_by_element=None, steps=0.2):
        return self._find_element_by_swipe('right', text_element, swipe_times, swipe_by_element, steps)


if __name__ == '__main__':
    # BasePage.set_driver('3EP7N19320003888')
    # d = run()
    # d.screenshot('D:\home.jpg')
    from Base.BaseInitPath import InitPath
    init_path = InitPath()
    init_path.set_log_path("../Log")

    init_path.get_log_path()
    log = Log()
    log.set_logger(name="hello")

    basepage = BasePage()
    basepage.set_driver('3EP7N19320003888')
    basepage.app_install_ll()

    # basepage.wakeup_device_ll()

    # rc = ReadConfig()
    # print('222:', os.path.abspath(rc.get_apk_path()))
    # basepage.d.session('com.taptap')
    # basepage.find_element_by_swipe_left('你好', 1)
    # basepage._get_element_size(basepage.d(text='游戏'))
    # print(basepage._get_phone_size())
    # basepage.d.click(element)
    # basepage.swipe_down(element=element, steps=0.2)
    # basepage.send_keys_ll('你好')

    # basepage.screenshot(PATH('../../Log/'))
    # basepage.watch_device('yes')
    # basepage.APK_install('com.taptap_2.1.4.apk')


    # bp = BasePage()
    # bp.set_driver('3EP7N19320003888')
    # log.set_logger('3EP7N19320003888')
    # bp.app_install_ll()

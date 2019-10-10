# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: concurrent, pytest

from concurrent.futures import ProcessPoolExecutor
import pytest
from Base.android.BaseDevicesInfo import get_device_info, get_devices_serial_list
import time
import os
from Base.BaseInitPath import InitPath
from Base.BaseSentMail import SentMail
from Base.BaseReadConfig import ReadConfig
from Base.BaseZip import MyZip

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class RunCase:
    # 初始化
    def __init__(self):
        self.rc = ReadConfig()
        self.to_email = self.rc.get_to_email()
        self.email_subject = self.rc.get_email_subject()
        self.init_path = InitPath()
        self.my_zip = MyZip()

    # 启动多进程
    def run(self, device_list):
        with ProcessPoolExecutor(len(get_devices_serial_list())) as pool:
            pool.map(self.run_pytest, device_list)

    # 压缩测试报告
    def _zip(self, report_path):
        print('====================zip test report to html.zip====================')
        # 压缩测试报告
        log_path = self.init_path.get_log_path()
        tool_path = PATH('../Tools/open_report.bat')
        to_path = report_path + '\\' + 'html'
        os.system(f"copy {tool_path} {to_path}")
        os.system(f"copy {log_path} {to_path}")
        self.my_zip.zip_file_path(input_path=f'{report_path}\\html', output_path=report_path, output_name='html.zip')

    # 发送邮件
    def _sentMail(self, now, phone):
        print('====================test finished and sent mail====================')
        # 实例化邮件模块发送邮件
        mail = SentMail(to_addr=self.to_email, subject=now + self.email_subject)
        mail.add_header()
        mail.add_html()
        attachment_name = now + '_' + phone['serial'] + '.zip'
        print(attachment_name)
        mail.add_attachment(file_path=self.init_path.get_report_path() + '\\' + 'html.zip', attch_name=attachment_name)
        mail.sent_mail()
        print('mail has been sent')

    # 运行
    def run_pytest(self, device):
        # 初始化报告，日志
        phone = get_device_info(device)
        now = time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime(time.time()))
        report_path = os.path.abspath(os.path.join(PATH('../Report'), now + '_' + phone['serial']))
        log_path = os.path.abspath(os.path.join(PATH('../Log'), now + '_' + phone['serial']))
        self.init_path.set_report_path(report_path=report_path)
        self.init_path.set_log_path(log_path=log_path)
        # report_path = self.init_path.get_report_path()
        # os.system(f'mkdir {report_path}')
        # os.system(f'mkdir {report_path}\\html')

        # 执行测试并生成测试报告
        print("====================start running test====================")
        print(f"sent cmdopt is {phone['serial']}")
        print(f'report path is {report_path}')
        try:
            print(f"pool run device :{phone['serial']}")
            print(f'report_path :{report_path}')
            pytest.main(
                [f"{self.rc.get_test_suite()}", f"--cmdopt={phone['serial']}", "--alluredir", f"{report_path}/xml"])
            time.sleep(1)
            os.system(f"allure generate {report_path}/xml -o {report_path}/html")

            # 压缩测试报告
            self._zip(report_path)

            # 发送邮件
            self._sentMail(now, phone)

        except Exception as e:
            print(f"error occur {e}")


if __name__ == '__main__':
    # case = RunCase()
    # case.run(['3EP7N19320003888'])
    phone = '123'
    now = time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime(time.time()))
    report_path = os.path.abspath(os.path.join(PATH('../Report'), now + '_' + phone))
    log_path = os.path.abspath(os.path.join(PATH('../Log'), now + '_' + phone))
    # init_path.set_params(report_path=report_path, log_path=log_path)
    print(report_path, log_path)

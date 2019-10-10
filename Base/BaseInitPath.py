# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: uiautomator2

import os
import zipfile


# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

# class LogPath:
#     @classmethod
#     def set_path(cls, path):
#         cls.path = path
#
#     def get_path(self):
#         return self.path

class InitPath:
    @classmethod
    def set_report_path(cls, report_path):
        cls.report_path = report_path

    @classmethod
    def set_log_path(cls, log_path):
        cls.log_path = log_path

    def get_report_path(self):
        return self.report_path

    def get_log_path(self):
        return self.log_path


# class ReportPath:
#     @classmethod
#     def set_path(cls, path):
#         cls.path = path
#
#     def get_path(self):
#         return self.path
#
#     def _get_zip_file(self, input_path, result):
#         files = os.listdir(input_path)
#         for file in files:
#             if os.path.isdir(input_path + '\\' + file):
#                 self._get_zip_file(input_path + '\\' + file, result)
#             else:
#                 result.append(input_path + '\\' + file)
#
#     def zip_file_path(self):
#         input_path = self.get_path() + '\\' + 'html'
#         output_path = self.get_path()
#         output_name = 'html.zip'
#         f = zipfile.ZipFile(output_path + '\\' + output_name, 'w', zipfile.ZIP_DEFLATED)
#         filelists = []
#         self._get_zip_file(input_path, filelists)
#         for file in filelists:
#             fpath = file.replace(input_path, '')
#             print(fpath)
#             f.write(file, fpath)
#         f.close()
#         return output_path + r"/" + output_name


if __name__ == '__main__':
    report_path = ReportPath()
    report_path.set_path('D:\\Atx-AutoFrame\\Report\\2019-07-22_16.54.18_3EP7N19320003888')
    report_path.zip_file_path()

    # res = os.listdir('D:\\Atx-AutoFrame\\Report\\2019-07-18_15.39.55_3EP7N19320003888\\html')
    # print(res)
    # print(os.path.isdir('D:\\Atx-AutoFrame\\Report\\2019-07-18_15.39.55_3EP7N19320003888\\html\\app.js'))
    # for file in res:
    # source_path = 'D:\\Atx-AutoFrame\\Report\\2019-07-22_16.54.18_3EP7N19320003888\\html'
    # to_path = 'D:\\Atx-AutoFrame\\Report\\2019-07-22_16.54.18_3EP7N19320003888\\'
    # save_path = 'D:\\Atx-AutoFrame\\Report\\2019-07-22_16.54.18_3EP7N19320003888\\'
    # zip_file_path(source_path, to_path, 'html.zip')
    # for (root1, dirs1, files1) in os.walk(source_path):
    #     for filename in files1:
    #         res = os.path.join(root1, filename)
    #         print(res)
    #         try:
    #             z = zipfile.ZipFile(res + '.zip', 'w')
    #             z.write(source_path)
    #             z.close()
    #         except:
    #             pass
    # zip = zipfile.ZipFile(to_path, "w", zipfile.ZIP_DEFLATED)
    # zip.write(source_path)
    # zip.close()
    # for path, dirnames, filenames in os.walk(source_path):
    #     # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
    #     print(path)
    #     fpath = path.replace(source_path, '')
    #     print(fpath)
    #     for filename in filenames:
    #         print(os.path.join(path, filename))
    #         print(os.path.join(fpath, filename))
    #         zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    # zip.close()
    # path = 'D:\\Atx-AutoFrame\\Report\\2019-07-22_16.54.18_3EP7N19320003888\\html'
    # to_path = 'D:\\Atx-AutoFrame\\Report\\2019-07-22_16.54.18_3EP7N19320003888\\html.zip'
    # zip = zipfile.ZipFile(to_path, "w", zipfile.ZIP_DEFLATED)
    # zip.write(path)
    # zip.close()

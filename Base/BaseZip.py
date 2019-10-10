# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: uiautomator2

import os
import zipfile


class MyZip:
    def _get_zip_file(self, input_path, result):
        '''
        :param input_path: 需要压缩的文件路径
        :param result:
        :return:
        '''
        files = os.listdir(input_path)
        for file in files:
            if os.path.isdir(input_path + '\\' + file):
                self._get_zip_file(input_path + '\\' + file, result)
            else:
                result.append(input_path + '\\' + file)

    def zip_file_path(self, input_path, output_path, output_name):
        '''
        :param input_path: 需要压缩的文件路径
        :param output_path: 压缩后的存储目录
        :param output_name: 压缩后的文件命名
        :return:
        '''
        f = zipfile.ZipFile(output_path + '\\' + output_name, 'w', zipfile.ZIP_DEFLATED)
        filelists = []
        self._get_zip_file(input_path, filelists)
        for file in filelists:
            fpath = file.replace(input_path, '')
            print(fpath)
            f.write(file, fpath)
        f.close()
        return output_path + r"/" + output_name

if __name__ == '__main__':
    input_path = get_report_path() + '\\' + 'html'
    output_path = get_report_path()
    output_name = 'html.zip'
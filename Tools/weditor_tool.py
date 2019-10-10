# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: weditor

import subprocess


def install_weditor():
    subprocess.run('pip install -U weditor', shell=True)


def run_weditor():
    cmd = 'python -m weditor'
    # os.system(cmd)
    p = subprocess.Popen(cmd, shell=True)
    p.wait()


if __name__ == '__main__':
    # install_weditor()
    run_weditor()
    # test(64 * 1024 + 1)

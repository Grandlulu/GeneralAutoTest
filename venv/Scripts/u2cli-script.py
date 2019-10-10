#!D:\Atx-AutoFrame\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'uiautomator2==0.3.3','console_scripts','u2cli'
__requires__ = 'uiautomator2==0.3.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('uiautomator2==0.3.3', 'console_scripts', 'u2cli')()
    )

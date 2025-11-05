import datetime
import os
import shutil

import allure
import pytest

from common.HTTPHandle import HTTPHandle
from common.YamlHandle import YamlHandle

@pytest.fixture(scope='function',autouse=True)
def conftest():
    print("==============接口测试开始==============")
    yield
    print("==============接口测试结束==============")



@pytest.fixture(scope='session',autouse=True)
def system_login():
    try:
        shutil.copy('./report/environment.xml','./report/temp/environment.xml')
        if os.path.exists("./extract.yaml"):
            os.remove('./extract.yaml')
        HTTPHandle.handle_case(*YamlHandle.get_testcase('./data/login.yaml')[0])
    except Exception as e:
        print(f'系统登录失败无法进行后续接口测试:{e}')
        exit(0)
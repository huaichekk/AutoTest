from datetime import datetime

import allure
import pytest
import connection.mysql as mysql
import time

from common.HTTPHandle import HTTPHandle
from common.YamlHandle import YamlHandle
from utils.report import Report


@pytest.fixture(scope="class",autouse=True)
def clear_resource():
    start_time = time.time()
    start_datetime = datetime.fromtimestamp(start_time)

    yield

    end_time = time.time()

    mysql.conn.delete(
        'DELETE FROM users WHERE username LIKE %s AND created_at BETWEEN %s AND %s',
        ('test%', start_datetime, datetime.fromtimestamp(end_time))
    )

@pytest.fixture(scope="function")
def before_update():
    HTTPHandle.handle_case(*YamlHandle.get_testcase('./data/login.yaml')[0])


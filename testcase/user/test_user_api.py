import allure
import pytest

from common.HTTPHandle import HTTPHandle
from common.YamlHandle import YamlHandle


@allure.feature('用户管理模块')
class TestUserApi:

    @allure.story('新增用户')
    @pytest.mark.parametrize('base_info,test_case',YamlHandle.get_testcase('./testcase/user/0-add.yaml'))
    def test_add_user(self,base_info,test_case):
        allure.dynamic.title(test_case['case_name'])
        HTTPHandle.handle_case(base_info,test_case)

    @allure.story('用户登录')
    @pytest.mark.parametrize('base_info,test_case',YamlHandle.get_testcase('./testcase/user/1-login.yaml'))
    def test_login(self,base_info,test_case):
        allure.dynamic.title(test_case['case_name'])
        HTTPHandle.handle_case(base_info,test_case)

    @allure.story('修改用户')
    @pytest.mark.parametrize('base_info,test_case',YamlHandle.get_testcase('./testcase/user/2-update.yaml'))
    def test_update_user(self,base_info,test_case,before_update):
        allure.dynamic.title(test_case['case_name'])
        HTTPHandle.handle_case(base_info,test_case)

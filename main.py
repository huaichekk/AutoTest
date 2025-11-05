import os
import pytest
#--clean-alluredir
if __name__=="__main__":
    pytest.main(["-v","-s","--alluredir=./report/temp","./testcase","--clean-alluredir"])
    os.system('allure serve ./report/temp')
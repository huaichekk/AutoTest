import logging

import requests

logging.basicConfig(level=logging.DEBUG)


session=requests.session()
#被测系统信息
server_addr='http://127.0.0.1:8080/api'

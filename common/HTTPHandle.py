import json
from os.path import split
from typing import Dict

import jsonpath
import requests

from common.AssertHandle import AssertHandle
from common.Helper import Helper
from common.YamlHandle import YamlHandle
from setting import server_addr,session
from utils.report import Report

class HTTPHandle:
    @staticmethod
    def handle_case(base_info,test_case):
        r=Report(base_info['api_name'])
        host = server_addr
        url=host+base_info['url']
        method=base_info['method']
        headers=base_info.get("headers",None)
        auth=base_info.get("auth",None)
        if auth is None or auth:
            if headers is None:
                headers = {}
            headers['X-Token']=Helper().get_data('token') #自动填写Token

        case_name = test_case['case_name']
        json = replace_data(test_case.get('json', None))
        data = replace_data(test_case.get('data',None))
        params = replace_data(test_case.get('params',None))
        extract = test_case.get('extract',None)

        r.info(f"接口名称:{base_info['api_name']}")
        r.info(f"url:{url}")
        r.info(f"header:{headers}")
        r.info(f"测试用例名称:{case_name}")
        r.info(f"参数 -- data : {data},json : {json},params : {params}")

        resp = session.request(method=method,
                        url=url,
                        headers=headers,
                        params=params,
                        data=data,
                        json=json,
                        )
        r.info(f'响应码:{resp.status_code}')
        assert resp.status_code==200

        resp=resp.json()
        r.info(f'接口响应信息:{resp}')


        #断言
        validation = test_case['validation']
        AssertHandle(validation).run(resp)

        if extract:
            extract_data(extract,resp)



def extract_data(extract:Dict,resp):
    for k,v in extract.items():
        if '$' in v:
            extract_json = jsonpath.jsonpath(resp,v)[0]
            if extract_json:
                extract_data = {k:extract_json}
                Report('').info(f'取到的数据:{extract_data}',)
                YamlHandle.write_data('./extract.yaml',extract_data)



def replace_data(data):
    if data is None:
        return None
    str_data=data
    if not isinstance(str_data,str):
        str_data = json.dumps(data, ensure_ascii=False)
    #${timestamp()}
    print(f"str_data:{str_data}")
    for _ in range(str_data.count('${')):
        if '${' in str_data and '}' in str_data:
            start = str_data.index('$')
            end = str_data.index('}',start)
            if end+1>len(str_data):
                now_str = str_data[start:]
            else:
                now_str = str_data[start:end+1]
            left_c = now_str.index('(')
            right_c = now_str.index(')')
            func_name = now_str[2:left_c]
            params = now_str[left_c+1:right_c]
            params = params.split(',')
            res = getattr(Helper(),func_name)(*params)

            str_data=str_data.replace(now_str,str(res))

    if data and isinstance(data,dict):
        data = json.loads(str_data)
    else:
        data = str_data
    return data







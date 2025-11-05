import logging
import yaml

class YamlHandle:
    @staticmethod
    def get_testcase(path):
        try:
            with open(path, "r",encoding="utf-8") as file:
                data = yaml.safe_load(file)
                if not data:
                    raise ValueError(f"yaml文件为空(path={path})")
                cases = data if isinstance(data, list) else [data]
                res = []
                for case in cases:
                    base_info = case.get("base_info", {})
                    test_cases = case.get("test_cases", [])
                    if not base_info or not test_cases:
                        continue

                    for test_case in test_cases:
                        res.append((base_info, test_case))

                return res
        except Exception as e:
            logging.error(f'处理【{path}】时出错: {str(e)}')
            return []
    @staticmethod
    def write_data(path,data):
        if not data:
            return
        with open(path,'w+',encoding='utf-8') as file:
            res = yaml.safe_load(file)
            if not res:
                res = {}
            k,v = next(iter(data.items()))
            res[k]=v
            file.seek(0)
            yaml.dump(res,file,default_flow_style=False,sort_keys=False)

    @staticmethod
    def read(path):
        with open(path,'r',encoding='utf-8') as file:
            return yaml.safe_load(file)

from typing import List, Dict


class AssertHandle:
    def __init__(self,validations:List[Dict]):
        self.validations = validations

    def run(self,resp):
        all_flag = 0
        for cond in self.validations:
            if 'eq' in cond:
                eq_rule = cond['eq']
                field,expect = next(iter(eq_rule.items()))
                all_flag+=self._equal(resp[field],expect)
            if 'contains' in cond:
                eq_rule = cond['contains']
                field, expect = next(iter(eq_rule.items()))
                all_flag+=self._contains(resp[field], expect)

        if all_flag==0:
            assert True
        else:
            assert False

    def _equal(self,data:str,expect:str)->int:
        if data == expect:
            return 0
        return 1

    def _contains(self, data: str, expect: str)->int:
        if expect in data:
            return 0
        return 1


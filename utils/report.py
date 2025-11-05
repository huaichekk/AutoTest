import allure

class Report:
    def __init__(self,case_name):
        self.case_name = case_name

    def info(self, data):
        allure.attach(self.case_name, data, allure.attachment_type.TEXT)


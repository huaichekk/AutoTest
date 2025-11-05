import time

from common.YamlHandle import YamlHandle


class Helper:
    def __init__(self):
        self.path = './extract.yaml'

    def get_data(self,field):
        data=YamlHandle.read(self.path)
        return data[field]

    def time(self):
        return int(time.time())
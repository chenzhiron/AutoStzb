import os

import json
current_file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录
current_dir_path = os.path.dirname(current_file_path)

# 拼接config.yaml的路径
config_file_path = os.path.join(current_dir_path, 'conf.json')

class Conf:
    def __init__(self) -> None:
        with open(config_file_path, 'r', encoding='utf-8') as load_f:
            self.conf = json.load(load_f)
        self.sort_task = []
        print(self.conf['state'])
    def get_key_data(self, k):
        if self.conf.__contains__(k):
            return self.conf[k]
        return None
    def get_data(self):
        return self.conf
    def set_key_data(self, k, v):
        if self.conf.get(k):
            self.conf[k] = v
        return self.conf[k]
    
conf = Conf()

    # def sort_task(self):
    #     for key, value in self.conf.item():
    #         if key == 'feat' and value['state']:

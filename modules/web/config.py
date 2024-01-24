import json
import os

current_file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录
current_dir_path = os.path.dirname(current_file_path)

# 拼接config.yaml的路径
config_file_path = os.path.join(current_dir_path, 'config.json')


class WebConfig:
    def __init__(self):
        self.config_data = None
        self.filename = config_file_path
        with open(self.filename, 'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
            self.config_data = load_dict['st']

    def get_data(self):
        return self.config_data

    def update_data(self, data):
        self.config_data = data

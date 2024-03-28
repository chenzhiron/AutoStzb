import json
import os
import copy

current_file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录
current_dir_path = os.path.dirname(current_file_path)

# 拼接config.yaml的路径
config_file_path = os.path.join(current_dir_path, 'config.json')


class WebConfig:
    def __init__(self):
        self.main_data = None
        self.config_file = config_file_path
        with open(self.config_file, 'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
            self.main_data = load_dict

    def get_main_data(self):
        return copy.deepcopy(self.main_data)

    def update_main_data(self, data):
        self.main_data = data

# if __name__ == '__main__':
#     ui = WebConfig()
#     print(ui.get_main_data())

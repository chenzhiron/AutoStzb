import json
import os
import copy

current_file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录
current_dir_path = os.path.dirname(current_file_path)

# 拼接config.yaml的路径
config_file_path = os.path.join(current_dir_path, 'config.json')
main_file_path = os.path.join(current_dir_path, 'main.json')


class WebConfig:
    def __init__(self):
        self.config_data = None
        self.main_data = None
        self.config_file = config_file_path
        self.main_file = main_file_path
        with open(self.config_file, 'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
            self.config_data = load_dict
        with open(self.main_file, 'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
            self.main_data = load_dict

    def get_main_data(self):
        return copy.deepcopy(self.main_data)

    def update_main_data(self, data):
        self.main_data = data

    def get_config_data(self):
        return copy.deepcopy(self.config_data)

    def update_config_data(self, data):
        self.config_data = data

# if __name__ == '__main__':
#     ui = WebConfig()
#     print(ui.get_config_data())
#     print(ui.get_main_data())
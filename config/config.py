import yaml
import os

# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录
current_dir_path = os.path.dirname(current_file_path)

# 拼接config.yaml的路径
config_file_path = os.path.join(current_dir_path, 'config.yaml')
userConfig_file_path = os.path.join(current_dir_path, 'user.yaml')
globalConfig = None
userConfig = None
# 打开并读取YAML文件
with open(config_file_path, 'r', encoding='utf-8') as file:
    globalConfig = yaml.safe_load(file)

with open(userConfig_file_path, 'r', encoding='utf-8') as file:
    userConfig = yaml.safe_load(file)

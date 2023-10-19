import os

# # 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取当前项目的路径
project_dir = os.path.dirname(current_dir)
tasks = os.path.join(project_dir, 'config', 'tasks.json').replace('\\', '/')
adb = os.path.join(project_dir, 'device', 'adb', 'adb.exe').replace('\\', '/')
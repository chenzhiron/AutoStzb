import os

# # 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取当前项目的路径
project_dir = os.path.dirname(current_dir)
path = os.path.join(project_dir, 'screenshot', 'content.jpeg').replace('\\', '/')
map = os.path.join(project_dir, 'scscreenshot','maps').replace('\\', '/')
print(path)

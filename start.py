import sys
import os
# 获取当前脚本所在目录的绝对路径
script_path = os.path.abspath(os.path.dirname(__file__))
# 添加脚本所在目录到模块搜索路径
sys.path.append(script_path)

script_dir = os.path.dirname(os.path.abspath(__file__))
# adb命令的相对路径（注意双反斜杠用于转义）
adb_relative_path = os.path.join('toolkit', 'adb', 'adb.exe')

# 构建完整的adb命令路径
adb_path = os.path.join(script_dir, adb_relative_path)
python_path = os.path.join(script_dir, 'toolkit\\python.exe')
# 设置环境变量，将adb命令所在目录添加到PATH中
os.environ['PATH'] = f"{python_path};{adb_path};{os.environ['PATH']}"

from modules.web.web import start_web

if __name__ == '__main__':
    start_web()
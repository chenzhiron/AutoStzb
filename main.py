import sys
import os

# 动态添加上级目录
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

if __name__ == "__main__":
    from modules.web.main import server

    server()

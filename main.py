import sys
import os

p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'venv', 'Lib', 'site-packages')
sys.path.append(lib_p)

from communication.comsumer import run_websocket

if __name__ == '__main__':
    run_websocket()

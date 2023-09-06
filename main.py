import sys

import os

p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'venv', 'Lib', 'site-packages')
sys.path.append(lib_p)

from communication.comsumer import start_run_websocket_thread
from dispatcher.main import start_scheduler

if __name__ == '__main__':
    start_run_websocket_thread()
    start_scheduler()
    while 1:
        pass

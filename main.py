import os
import sys

p = os.getcwd()
sys.path.append(p)
lib_p = os.path.join(p, 'toolkit', 'Lib', 'site-packages')
sys.path.append(lib_p)

from web.web import start_web
from config.const import web_port

if __name__ == '__main__':
    try:
        start_web(web_port)

    except Exception as e:
        print('主线程发生了错误', e)

import threading

from pywebio import start_server

from modules.web.components.Option import *
from modules.web.components.prop_all import *
from modules.web.components.MemuBar import MemuBar
from modules.web.components.Manager import Manager
from modules.web.components.Log import Log
from modules.web.components.State import State
from modules.web.components.Entry import Entry
from modules.web.components.web_config import WebConfig
from modules.execute.main import stzb

class Web(WebConfig, Entry, MemuBar, Manager, Log, State):
    process = None
    def __init__(self):
        super().__init__()

ui = Web()

def start_web(): 
    execute = threading.Thread(target=stzb.loop)
    execute.setDaemon(True)
    execute.start()
    start_server( applications=ui.render, port=9091, debug=True)

if __name__ == '__main__':
    start_web()

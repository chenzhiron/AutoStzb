import copy
import subprocess

from pywebio import start_server

from modules.web.components.Option import *
from modules.web.components.prop_all import *
from modules.web.components.MemuBar import MemuBar
from modules.web.components.Manager import Manager
from modules.web.components.Log import Log
from modules.web.components.State import State
from modules.web.components.Entry import Entry
from modules.web.components.web_config import WebConfig

class Web(WebConfig, Entry, MemuBar, Manager, Log, State):
    process = None
    def __init__(self):
        super().__init__()

    def get_data(self, key=None):
        if key is None:
            return copy.deepcopy(self.data)
        return copy.deepcopy(self.data[key])
    def set_data(self, key, value, keyid = None):
        if key == 'task':
            for v in self.data['task']:
                if v['id'] == keyid:
                    value.pop('state')
                    v.update(value)
        else:
            if type(value) == list and len(value) == 0:
                value = []
            self.data[key] = value

    def run_shell(self, cmd: str, output_func, encoding='utf8') -> int:
        self.process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        try:
            while True:
                out = self.process.stdout.readline()
                if out:
                    output_func(out.decode(encoding))

                if not out and self.process.poll() is not None:
                    break
        except Exception as e:
            output_func(e.decode(encoding))
            print('子进程运行退出', e)
        finally:
            if self.process != None:
                self.process.kill()
                self.process.stdout.close()
        self.data['state'] = 0
        self.render_state()
        return 0
    

ui = Web()

def start_web(): 
    start_server( ui.render, port=9091, debug=True)

if __name__ == '__main__':
    start_web()

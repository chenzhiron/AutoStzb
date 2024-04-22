import os

cwd = os.getcwd()
execute_path = os.path.join(cwd, 'modules', 'execute', 'main.py')
python_command = ''
res = os.environ['PATH'].split(';')
python_path = os.path.normpath('toolkit\\python.exe')
for v in res:
    if python_path in os.path.normpath(v):
        python_command = os.path.normpath(v)
        break
    else:
        python_command = 'python.exe'

import functools
from pywebio.output import use_scope,put_button, put_text

from modules.web.components.Option import *
from modules.web.components.prop_all import *

class State:
  def __init__(self) -> None:
    pass
  def change_state(self, state):
    self.data['state'] = state
    self.render_state()
    if self.data['state'] == 1 and self.process == None:
        self.run_shell(python_command + ' ' + execute_path, output_func=self.send_message, encoding='utf8')
    if self.data['state'] == 0 and self.process != None:
        self.process.kill()
        self.process.stdout.close()
        self.process = None
  
  @use_scope('state', clear=True)
  def render_state(self):
      put_text('调度器')
      if self.data['state'] == 0:
          put_button('启动', onclick= functools.partial(self.change_state, state = 1))
      if self.data['state'] == 1:
          put_button('停止', onclick= functools.partial(self.change_state, state = 0))

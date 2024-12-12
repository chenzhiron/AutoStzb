import time
from pywebio.session import register_thread, run_js, get_current_session
from threading import Thread
from pywebio.exceptions import SessionNotFoundException
class TaskConfig:
  def __init__(self, name):
    self.name = name

class StDispatch:
  def __init__(self):
    self.task_thraed = None
    self.last_len = 0
    self.pm = None
    self.i = 0

  def update_pm(self, pm):
    self.pm = pm

  def loop(self):
    while True:
      if self.pm != None and self.last_len != len(self.pm.log):
        log_message = self.pm.log.pop(0)
        try:
          run_js("let d = document.getElementById('pywebio-scope-log_area'); let v = d.innerHTML; d.innerHTML=`"+str(log_message) + '\n`')
        except SessionNotFoundException:
          print(get_current_session())
      time.sleep(0.5)

  def start(self):
    self.task_thraed = Thread(None, target=self.loop)
    self.task_thraed.start()

  def register(self):
    register_thread(self.task_thraed)

from pywebio.output import use_scope, put_column, put_text, put_button
from pywebio.session import register_thread
import threading
import time


stop_thread = False


class OverViewView:
  def __init__(self, log_instance = None): 
    self.log_instance = log_instance
    self.dispath_state = False
    self.dispath_thread = None

  def update_log_instance(self, log_instance):
    self.log_instance = log_instance

  def get_dispath_state(self):
    return self.dispath_state

  def set_dispath_state(self, state):
    self.dispath_state = state
    if self.dispath_state:
      self.dispath_thread = self.start_thread()
      register_thread(self.dispath_thread)
    else:
      self.kill_thread()
 
    
  def start_thread(self):
    global stop_thread
    stop_thread = True
    thread = threading.Thread(None,target=settimeout_out_log, args=(self.log_instance,))
    thread.start()
    return thread
  
  def kill_thread(self):
    global stop_thread
    stop_thread = False

  def anew_render(self):
      self.log_instance.add_info('调度器状态:%s' % ('启动' if self.get_dispath_state() else '停止'))
      self.set_dispath_state(not self.get_dispath_state())
      self.render()

  @use_scope('overview', clear=True)
  def render(self):
    put_column([
        put_text('调度器状态'),
        put_button(label='停止' if self.get_dispath_state()  else '启动', onclick=self.anew_render)
      ])


def settimeout_out_log(log_instance):
  global stop_thread
  i = 0
  while stop_thread:
    time.sleep(1)
    log_instance.add_info('子线程输出log'+str(i))
    i += 1
  print('子线程结束')  

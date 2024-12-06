from pywebio.session import register_thread
from threading import Thread
class StDispatch:
  def __init__(self):
    self.task_thread = Thread(None, target=self.loop)

  def task_threadfn(self):
    pass
  def loop(self):
    pass



class StHandle(StDispatch):
  def __init__(self):
    super().__init__()
    taskthread = self.task_thread
    register_thread(taskthread)


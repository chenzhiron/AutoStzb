from multiprocessing import Process
from queue import Queue
from threading import Thread
from typing import Dict
from .log import set_handle
from .setting import ShareData
import queue

class ProcessManage:
  _processes: Dict[str, "ProcessManage"] = {}

  def __init__(self, config_name='st'):
    self.st_thread = None
    self.st_log_queue = ShareData.manager.Queue()
    self.log_queue = []
    self.event_st_log_queue_thread = None

  def stop(self):
    self.st_thread.kill()
    self.st_thread = None
    if self.event_st_log_queue_thread is not None:
          self.event_st_log_queue_thread.join(timeout=1)

  def start(self):
    self.st_thread = Process(
      None,
      target=ProcessManage.run_st,
      args=(self.st_log_queue,)
      )
    print('st_thread:', self.st_thread)
    self.st_thread.start()
    self.event_st_log_queue_thread = Thread(target=self.thread_log_queue_handler)
    self.event_st_log_queue_thread.start()

  @property
  
  def state(self) -> int:
        if self.alive:
          return 1
        else:
          return 0

  
  def thread_log_queue_handler(self) -> None:
      print('logque:', self.st_log_queue)
      while self.alive:
          try:
              log = self.st_log_queue.get(timeout=1)
          except queue.Empty:
              continue
          print('thread_log_handle:', log)
          self.log_queue.append(log)

  def run_st(self, q:Queue):
    from st import St
    set_handle(q.put)
    St(q).loop()
  
  @property
  def alive(self) -> bool:
      if self.st_thread is not None:
          return self.st_thread.is_alive()
      else:
          return False
      
  @classmethod
  def get_manager(cls, config_name: str) -> "ProcessManage":
      """
      Create a new alas if not exists.
      """
      if config_name not in cls._processes:
          cls._processes[config_name] = ProcessManage(config_name)
      return cls._processes[config_name]

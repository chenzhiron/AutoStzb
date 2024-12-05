import threading
import time

class St:
  stop_event: threading.Event = None

  def __init__(self, log):
    self.custom = log
  
  def loop(self):
    i = 0;
    while not self.stop_event:
      i+=1
      self.custom.put(i)
      time.sleep(1)

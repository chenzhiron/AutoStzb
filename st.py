import threading
import time


from modules.log import info

class St:
  stop_event: threading.Event = None

  def __init__(self):
    pass

  def loop(self):
    i = 0;
    while not self.stop_event:
      i+=1
      info(str(i))
      time.sleep(1)

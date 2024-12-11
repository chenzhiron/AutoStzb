import threading
import time

from modules.log import info

class St:
  stop_event: threading.Event = None

  def __init__(self, teamprop):
    self.teamdata = teamprop
    print(id(self.teamdata))
  def loop(self):
    i = 0;
    while not self.stop_event:
      i+=1
      info(self.teamdata)
      time.sleep(1)

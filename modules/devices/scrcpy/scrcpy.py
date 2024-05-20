from modules.devices.scrcpy.core import Client
from PIL import Image
import numpy as np
import time
class Scrcpy:
  def __init__(self) -> None:
    self.client = Client(self.simulator,max_fps=5)
  def run(self):
    self.client.start(daemon_threaded=True)
  def getScreenshots(self):
    time.sleep(self.screen_await)
    return np.array(self.client.last_frame)
  

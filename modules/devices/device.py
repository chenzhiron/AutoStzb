import time

from adbutils import adb
import uiautomator2 as u2
import numpy as np
from modules.devices.automation import DroidCast
from modules.devices.scrcpy.scrcpy import Scrcpy
class Devices(Scrcpy):
    def __init__(self, config) -> None:
        self.simulator = config['simulator']
        self.screen_await = config['screen_await']
        print('simulator', self.simulator)
        adb.connect(self.simulator)
        super().__init__()
        self.run()
        self.d = u2.connect(self.simulator)
    
    def operateTap(self, x, y):
        self.d.click(x, y)

    def operateSwipe(self, points_list, steps=3):
        for v in points_list:
            x1, y1, x2, y2 = v
            self.d.swipe(x1, y1, x2, y2, steps=steps)
        time.sleep(0.3)
    def operateInput(self, txt):
        self.d.clear_text()
        self.d.send_keys(txt)
    
    def oprtateDrag(self, points_list):
            x1, y1, x2, y2 = points_list
            self.d.drag(x1, y1, x2, y2)

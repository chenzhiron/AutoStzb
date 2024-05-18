import time

from adbutils import adb
import uiautomator2 as u2
import numpy as np
from modules.devices.automation import DroidCast

class Devices:
    def __init__(self, config) -> None:
        super().__init__()
        simulator = config['simulator']
        print('simulator', simulator)
        adb.connect(simulator)
        self.screen_await = config['screen_await']
        self.d = u2.connect(simulator)
        # self.url = 'http://127.0.0.1:53516/preview?width=1600&height=900'
        self.url = ''


    def getScreenshots(self):
        time.sleep(self.screen_await)
        imgs = self.d.screenshot()
        res = np.array(imgs)
        return res
    
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

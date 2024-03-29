import time

import uiautomator2 as u2
import websocket
import adbutils
from PIL import Image
import io


class Devices:
    def __init__(self, config) -> None:
        simulator = config['Simulator']['url']
        print('simulator', simulator)
        self.d = u2.connect(simulator)
        lport = adbutils.adb.device(simulator).forward_port(7912)
        self.ws = websocket.WebSocket()
        self.ws.connect('ws://localhost:{}/minicap'.format(lport))

    def getScreenshots(self):
        return self.d.screenshot()
        # time.sleep(1)
        # while True:
        #     data = self.ws.recv()
        #     if not isinstance(data, (bytes, bytearray)):
        #         continue
        #     with open(time.strftime('%Y%m%d%H%M%S')+'.png', 'wb') as f:
        #         f.write(data)
        #     return Image.open(io.BytesIO(data))

    def operateTap(self, x, y):
        self.d.click(x, y)

    def operateSwipe(self, points_list):
        for v in points_list:
            x1, y1, x2, y2 = v
            self.d.swipe(x1, y1, x2, y2, steps=5)

    def operateInput(self, txt):
        self.d.clear_text()
        self.d.send_keys(txt)

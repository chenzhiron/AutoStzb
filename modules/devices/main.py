import uiautomator2 as u2

class Devices:
    def __init__(self, simulator):
        self.d = u2.connect(simulator)

    def click(self, x:int, y:int):
        print('click x:',x,'y',y)
        self.d.click(x, y)

    def swipe(self, origin_x, origin_y, next_x, next_y, times=1):
        self.d.swipe(origin_x, origin_y, next_x, next_y, times)

    def drag(self, sx, sy, ex, ey, duration=1):
        self.d.drag(sx, sy, ex, ey, duration)

    def screenshot(self):
        return self.d.screenshot()

    def copy_val(self):
        self.d.set_input_ime()
        return self.d.clipboard
    def input(self, v, clear=True):
        self.d.send_keys(v, clear)

if __name__ == "__main__":
    d = Devices("127.0.0.1:16384")
    d.drag(550, 500, 550,200 ,2)

import uiautomator2 as u2

class Devices:
    def __init__(self, simulator):
      self.d = u2.connect(simulator)

    def click(self, x, y):
      self.d.click(x, y)
    def swipe(self,origin_x, origin_y ,next_x, next_y, times = 1.5):
      self.d.swipe(origin_x,origin_y, next_x, next_y, times)
    
    def drag(self, sx, sy, ex, ey, duration=1.5):
      self.d.drag(sx, sy, ex, ey, duration)

    def screenshot(self):
      return self.d.screenshot()
    
    def copy_val(self):
      self.d.set_input_ime()
      return self.d.clipboard

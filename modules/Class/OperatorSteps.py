class OperatorSteps:
    x, y = 0, 0

    def __init__(self, area, txt, x=0, y=0):
        self.verify_txt = txt
        self.area = area
        if x == 0:
            self.x = (self.area[0] + self.area[2]) / 2
        if y == 0:
            self.y = (self.area[1] + self.area[3]) / 2

    def apply_click(self):
        print(self.area)
        print(self.area)
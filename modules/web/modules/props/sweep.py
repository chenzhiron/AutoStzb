class SweepProp:
  def __init__(self, index):
    self._index = index
    self.all_state = True
    self.name = ""
    self.next_time = ''
    self.x = 0
    self.y = 0

  def set_all_state(self, state):
    self.all_state = len(state) == 0
    print(self.all_state)

  def set_name(self, name):
    self.name = name

  def set_next_time(self, time):
    self.next_time = time

  def set_x(self, x):
    self.x = x
  
  def set_y(self, y):
    self.y = y

  def get_all_state(self):
    return self.all_state

  def get_name(self):
    return self.name

  def get_next_time(self):
    return self.next_time

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y

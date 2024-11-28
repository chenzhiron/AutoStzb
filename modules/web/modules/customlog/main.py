from pywebio.output import use_scope, put_text, clear

class StLog:
  def __init__(self):
    self.infos = []

  def add_info(self, info):
    self.infos.append(info)
    self.render(info)

  def get_infos(self):
    return self.infos
  
  @use_scope('function_area')
  def render(self, new_info = None):
    if new_info:
      put_text(new_info)
    else:
      clear('function_area')
      for info in self.infos:
        put_text(info)

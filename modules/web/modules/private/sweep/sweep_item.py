from pywebio.output import put_row,put_column,put_text
from pywebio.pin import pin_on_change, put_input, put_checkbox
from modules.web.modules.utils import def_lable_checkbox, explain_componet

class SweepItem:
  def __init__(self,prop):
    self.prop = prop

  def render(self):
    stall_all = 'stall_all' + self.prop._index
    next_time = 'next_time' + self.prop._index
    x = 'x' + self.prop._index
    y = 'y' + self.prop._index

    renders = [
      explain_componet(['状态'], def_lable_checkbox(put_checkbox(stall_all, options=[True], value=self.prop.get_all_state()))),
      
      explain_componet(['下次执行时间', '任务下一次执行的时间, 一般不需要手动更改'], put_input(next_time, value=self.prop.get_next_time())),
      explain_componet(['X坐标'], put_input(x,value=self.prop.get_x())),
      explain_componet(['Y坐标'], put_input(y,value=self.prop.get_y())),
    ]

    pin_on_change(stall_all, onchange=self.prop.set_all_state,clear=True)
    pin_on_change(next_time, onchange=self.prop.set_next_time,clear=True)
    return renders

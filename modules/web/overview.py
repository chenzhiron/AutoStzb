from pywebio.output import use_scope, put_column, put_text, put_button
from .process_mange import ProcessManage

class OverViewView:
  def __init__(self, st_process:ProcessManage): 
    self.st = st_process

  def set_dispath_state(self, state):
    if state:
      self.st.stop()
    else:
      self.st.start()
 

  def anew_render(self):
      self.set_dispath_state(self.st.state)
      self.render()

  @use_scope('overview', clear=True)
  def render(self):
    put_column([
        put_text('调度器状态'),
        put_button(label='停止' if self.st.state  else '启动', onclick=self.anew_render)
      ])


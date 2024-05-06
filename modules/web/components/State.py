
import functools
from pywebio.output import use_scope,put_button, put_text

from modules.web.components.Option import *
from modules.web.components.prop_all import *

class State:
  def __init__(self) -> None:
    pass
  def change_state(self, state):
    self.conf_data.set_key_data('state', {
       "value": state
    })
    self.render_state()
  
  @use_scope('state', clear=True)
  def render_state(self):
      put_text('调度器')
      if self.conf_data.get_key_data('state')['value'] == 0:
          put_button('启动', onclick= functools.partial(self.change_state, state = 1))
      if self.conf_data.get_key_data('state')['value'] == 1:
          put_button('停止', onclick= functools.partial(self.change_state, state = 0))

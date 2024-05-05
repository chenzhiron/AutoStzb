from pywebio.output import put_scope, use_scope
from pywebio_battery import put_logbox, logbox_append


class Log:
  def __init__(self) -> None:
      pass
  @use_scope('content', clear=True)
  def render_log(self):
      self.clear_area()
      put_scope('log_bar', [put_logbox('log', height=700)])
      for v in self.get_log():
          logbox_append('log', v)

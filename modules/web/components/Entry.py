import threading
from pywebio.output import put_scope, use_scope, put_button, clear
from pywebio import  config
from pywebio.session import set_env, register_thread

from modules.web.styles import style

class Entry:
  def __init__(self) -> None:
    pass
  config(css_style=style)
  def render(self):
      self.register_session()

      set_env(title="AutoStzb", output_max_width='100%')
      put_scope('top', [
                          put_scope('state', [])
                          ])
      self.render_state()
      put_scope('main', [
                  put_scope('module_bar', []),
                  put_scope('navigation_bar', []),
                  put_scope('content', []),
      ])
      self.render_module_bar()
      from modules.execute.main import stzb
      self.execute_thread = threading.Thread(target=stzb.loop)
      self.execute_thread.setDaemon(True)
      self.execute_thread.start()
      register_thread(self.execute_thread)
        


  def render_module_bar(self):
      with use_scope('module_bar', clear=True):
          put_button('日志', onclick=self.render_log)
          put_button('管理', onclick=self.manager)
          put_button('功能', onclick=self.render_navigation_bar)
  
  def clear_area(self, area_lists=['navigation_bar', 'content']):
    for v in area_lists:
        clear(v)
from pywebio.platform.tornado import start_server
from pywebio.output import put_scope, use_scope, put_scrollable
from pywebio.session import set_env
from pywebio import config

from .function import private, team, OverViewView
from .process_mange import ProcessManage
from .setting import ShareData

def server():
  ShareData.init()
  
  web = app().render
  
  start_server(web, port=10965, auto_open_webbrowser=True, static_dir='./modules/web/static')

class app:
  def __init__(self):
    self.st = ProcessManage.get_manager()

  def render(self):
    config(css_file='./static/style.css')
    self.set_config()
    self.init_scope()

    with use_scope('function',clear=True):
      OverViewView(self.st).render()
      private.render()
      team.render()

   
    while 1:
      if len(self.st.log) > 0:
        with use_scope('function_area',clear=True):
          put_scrollable(self.st.log.pop(0))

  def set_config(self):
    set_env(output_max_width='100%')

  def init_scope(self):
    put_scope('main', [
        put_scope('memu').style('width:100px;'),
          put_scope('function').style('width:200px;'),
          put_scope('function_area', ).style('flex:1;')
        ]).style('display:flex')
    
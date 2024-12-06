from pywebio.platform.tornado import start_server
from pywebio.output import put_scope, use_scope, put_scrollable, put_column, put_text, put_button,put_collapse
from pywebio.session import set_env
from pywebio import config

from .function import private
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
      self.render_process_btn()
      self.render_team()
      private.render()
   
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
  

  @use_scope('overview', clear=True)
  def render_process_btn(self):
    put_column([
          put_text('调度器状态'),
          put_button(label='停止' if self.st.state  else '启动', onclick=self.anew_render)
        ])
    
  def set_dispath_state(self, state):
    if state:
      self.st.stop()
    else:
      self.st.start()


  def anew_render(self):
      self.set_dispath_state(self.st.state)
      self.render_process_btn()


  @use_scope('team', clear=True)
  def render_team(self):
    put_collapse('同盟',[
      put_text('打城主力'),
      put_text('打城拆迁'),
      put_text('武勋'),
      put_text('敌军主力'),
      put_text('战场翻地/拆除'),
      put_text('我方出战/防守')
    ])

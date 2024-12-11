from pywebio.platform.tornado import start_server
from pywebio.output import put_scope, use_scope, put_column, put_text, put_button,put_collapse
from pywebio.session import set_env
from pywebio.pin import pin_on_change, put_checkbox
from pywebio import config

from modules.task import StDispatch
from modules.teamallprop import *
from modules.web.utils import def_lable_checkbox, explain_componet
from .function import private
from .process_mange import ProcessManage


stdispath = StDispatch()

def server():
  web = app().render
  
  start_server(web, port=10965, auto_open_webbrowser=True, static_dir='./modules/web/static')

class app:
  def __init__(self):
    self.st = ProcessManage.get_manager()
    stdispath.update_pm(self.st)
    stdispath.start()

  def render(self):
    stdispath.register()
    config(css_file='./static/style.css')
    self.set_config()
    self.init_scope()

    with use_scope('function',clear=True):
      self.render_process_btn()
      self.render_team()
      private.render()

  def set_config(self):
    set_env(output_max_width='100%')

  def init_scope(self):
    put_scope('main', [
        put_scope('memu').style('width:100px;'),
          put_scope('function').style('width:200px;'),
          put_scope('function_area').style('flex:1;'),
          put_scope('log_area').style('flex:1;')
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
      self.st.start(stteamprop)


  def anew_render(self):
      self.set_dispath_state(self.st.state)
      self.render_process_btn()


  @use_scope('team', clear=True)
  def render_team(self):
    put_collapse('同盟',[
      put_text('打城主力').onclick(self.render_besiegemain),
      put_text('打城拆迁').onclick(self.render_basiegedestory),
      put_text('武勋').onclick(self.render_exploit),
      put_text('敌军主力').onclick(self.render_enemymain),
      put_text('战场翻地/拆除').onclick(self.render_battledestory),
      put_text('我方出战/防守').onclick(self.render_myfight)
    ])
  @use_scope('function_area',clear=True)
  def render_besiegemain(self):
    explain_componet(['状态'], def_lable_checkbox(put_checkbox('state', options=[True], value= stteamprop[besiegemain_state])))
    pin_on_change("state", onchange=lambda v: updatecheckbox(stteamprop, besiegemain_state, v),clear=True)

  @use_scope('function_area',clear=True)
  def render_basiegedestory(self):
    explain_componet(['状态'], def_lable_checkbox(put_checkbox('state', options=[True], value=stteamprop[basiegedestory_state])))
    pin_on_change("state", onchange=lambda v: updatecheckbox(stteamprop, basiegedestory_state, v),clear=True)

  @use_scope('function_area',clear=True)
  def render_exploit(self):
    explain_componet(['状态'], def_lable_checkbox(put_checkbox('state', options=[True], value=stteamprop[exploit_state])))
    pin_on_change("state", onchange=lambda v: updatecheckbox(stteamprop, exploit_state, v),clear=True)

  @use_scope('function_area',clear=True)
  def render_enemymain(self):
    explain_componet(['状态'], def_lable_checkbox(put_checkbox('state', options=[True], value=stteamprop[enemymain_state])))
    pin_on_change("state", onchange=lambda v: updatecheckbox(stteamprop, enemymain_state, v),clear=True)

  @use_scope('function_area',clear=True)
  def render_battledestory(self):
    explain_componet(['状态'], def_lable_checkbox(put_checkbox('state', options=[True], value=stteamprop[battledestory_state])))
    pin_on_change("state", onchange=lambda v: updatecheckbox(stteamprop, battledestory_state, v),clear=True)

  @use_scope('function_area',clear=True)
  def render_myfight(self):
    explain_componet(['状态'], def_lable_checkbox(put_checkbox('state', options=[True], value=stteamprop[myfight_state])))
    pin_on_change("state", onchange=lambda v: updatecheckbox(stteamprop, myfight_state, v),clear=True)

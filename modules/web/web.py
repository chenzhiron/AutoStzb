import json
import os
import copy
import functools

from pywebio.output import put_row, put_scope, use_scope, put_collapse,put_button, put_text
from pywebio import start_server
from pywebio.session import set_env

from modules.web.components.Option import OptionPage
from modules.web.components.prop_all import *


current_file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录
current_dir_path = os.path.dirname(current_file_path)

# 拼接config.yaml的路径
config_file_path = os.path.join(current_dir_path, 'config.json')

print(config_file_path)

class WebConfig:
    def __init__(self):
        self.data = None
        self.config_file = config_file_path
        with open(self.config_file, 'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
            self.data = load_dict

class Web(WebConfig):

    def __init__(self):
        super().__init__()

    def get_data(self, key=None):
        if key is None:
            return copy.deepcopy(self.data)
        return copy.deepcopy(self.data[key])
    def set_data(self, key, value):
        if key == 'task':
            for v in range(len(self.data['task'])):
                self.data['task'][v].update(value[v])
        else:
            self.data[key] = value
    @use_scope('menu_bar', clear=True)
    def render_memu_bar(self, updata):
          OptionPage([updata, {
                    team: updata['team'],
                    skip_await: updata['skip_await'],
                    state: updata['state'],
                    explain: updata['explain'],
                    recruit_person:updata['recruit_person'],
                    going: updata['going'],
                    mopping_up: updata['mopping_up'],
                    await_time: updata['await_time'],
                    next_run_time: updata['next_run_time'],
                    delay: updata['delay'],
                    draw_txt: updata['draw_txt'],
                    residue_troops_person: updata['residue_troops_person'],
                    residue_troops_enemy: updata['residue_troops_enemy']
                }]).dispatch()
          
    @use_scope('navigation_bar', clear=True)
    def render_navigation_bar(self):
        tasks_render = []
        for v in self.data['task']:
            tasks_render.append(put_button('队伍', onclick= functools.partial(self.render_memu_bar, updata = v)))
        put_collapse('任务', tasks_render)
    
    def change_state(self, state):
        self.data['state'] = state
        self.render_state()

    @use_scope('state', clear=True)
    def render_state(self):
        put_text('调度器').style('display:inline-block')
        if self.data['state'] == 0:
            put_button('启动', onclick= functools.partial(self.change_state, state = 1)).style('display:inline-block')
        if self.data['state'] == 1:
            put_button('停止', onclick= functools.partial(self.change_state, state = 0)).style('display:inline-block')

    @use_scope('title', clear=True)
    def render_title(self, title):
        put_text(title).style('display:inline-block')

    def render(self):
        set_env(title="AutoStzb", output_max_width='100%')
        put_scope('topp', [put_scope('state', []), put_scope('title', [])]).style('display:flex')
        self.render_state()
        self.render_title('主页')
        put_row([
                    put_scope('navigation_bar', []),
                    put_scope('function_bar', []),
                    put_scope('menu_bar', []),
                    put_scope('log_bar', [])
                ]).style('display:flex')
        self.render_navigation_bar()

ui = Web()   

def start_web():
    start_server(ui.render, port=9091, debug=True)

# if __name__ == '__main__':
#     thread = threading.Thread(target=start_web)
#     thread.setDaemon(True)
#     thread.start()
#     time.sleep(5)
#     print('启动成功,请访问http://localhost:9091')
#     res = ui.get_data('task')
#     for v in res:
#         v['skip_await'] = True
#     ui.set_data('task', res)
#     print('next', res)
#     time.sleep(55)

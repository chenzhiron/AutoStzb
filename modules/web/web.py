import json
import os
import copy
import functools
import threading
import time

from pywebio.output import put_scope, use_scope, put_collapse,put_button, put_text, clear, put_image
from pywebio_battery import put_logbox, logbox_append
from pywebio import start_server, config
from pywebio.session import set_env, register_thread, defer_call

from modules.web.components.Option import *
from modules.web.components.prop_all import *
from modules.web.styles import style

current_file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录
current_dir_path = os.path.dirname(current_file_path)

# 拼接config.yaml的路径
config_file_path = os.path.join(current_dir_path, 'config.json')

print(config_file_path)

log_status = True
offset = 0

class WebConfig:
    def __init__(self):
        self.data = None
        self.config_file = config_file_path
        with open(self.config_file, 'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
            self.data = load_dict
        self.logs = []
    def add_log(self, msg):
        if len(self.logs) > 500:
            self.logs = self.logs[450:]
            offset = 0
        self.logs.append(msg)

class Web(WebConfig):

    def __init__(self):
        super().__init__()

    def get_data(self, key=None):
        if key is None:
            return copy.deepcopy(self.data)
        return copy.deepcopy(self.data[key])
    def set_data(self, key, value, keyid = None):
        if key == 'task':
            for v in self.data['task']:
                if v['id'] == keyid:
                    v.update(value)
        else:
            self.data[key] = value
    def clear_area(self, area_lists=['navigation_bar', 'content']):
        for v in area_lists:
            clear(v)

    @use_scope('navigation_bar', clear=True)
    def render_navigation_bar(self):
        self.clear_area()
        tasks_render = []
        for v in self.data['task']:
            tasks_render.append(put_button('主城部队', onclick= functools.partial(self.render_memu_bar, updata = v)))
        put_collapse('队伍', tasks_render)

    def change_state(self, state):
        self.data['state'] = state
        self.render_state()

    @use_scope('state', clear=True)
    def render_state(self):
        put_text('调度器')
        if self.data['state'] == 0:
            put_button('启动', onclick= functools.partial(self.change_state, state = 1))
        if self.data['state'] == 1:
            put_button('停止', onclick= functools.partial(self.change_state, state = 0))
    
    @use_scope('content', clear=True)
    def render_log(self):
        self.clear_area()
        put_scope('log_bar', [put_logbox('log', height=700)])


    @use_scope('content', clear=True)
    def render_memu_bar(self, updata):
          with use_scope('menu_bar', clear=True):
            OptionPage([updata, {
                        team: updata['team'],
                        state: updata['state'],
                        next_run_time: updata['next_run_time'],
                        x: updata['x'],
                        y: updata['y'],
                        recruit_person:updata['recruit_person'],
                        going: updata['going'],
                        mopping_up: updata['mopping_up'],
                        await_time: updata['await_time'],
                        residue_troops_person: updata['residue_troops_person'],
                        residue_troops_enemy: updata['residue_troops_enemy']
                    }]).dispatch()
            
          with use_scope('img_show', clear=True):
              put_text('战报记录')
              if len(updata['battle_info']) > 0:
                  updata['battle_info'].reverse()
                  for v in updata['battle_info']:
                    put_image(v, width='100%')

    def render(self):
        # 日志记录
        t = threading.Thread(target=log_thread)
        register_thread(t)
        
        # 用户访问 web 时，开启单独线程处理，必须使用 defer_call 用户关闭会话后，自动把输出log进程结束 
        # https://pywebio.readthedocs.io/zh-cn/latest/guide.html#thread-in-server-mode
        log_status = True
        @defer_call
        def clearlog():
            log_status = False

        set_env(title="AutoStzb", output_max_width='100%')
        config(css_style=style)
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
        t.start()
    
    @use_scope('navigation_bar', clear=True)
    def manager(self):
        self.clear_area()
        put_button('模拟器配置', onclick=self.render_manager_simulator)

    @use_scope('content', clear=True)
    def render_manager_simulator(self):
        with use_scope('menu_bar', clear=True):
            key = propall['simulator']
            Option([key.display_name], Component(key.name, self.data[key.name],
                                                key.option_type, functools.partial(
                                                    key.on_change_event,
                                                        origin=self.data,
                                                        origin_controller={key:self.data[key.name]}
                                                        ))
                ).options


    def render_module_bar(self):
        with use_scope('module_bar', clear=True):
            put_button('日志', onclick=self.render_log)
            put_button('管理', onclick=self.manager)
            put_button('功能', onclick=self.render_navigation_bar)


ui = Web()

# 日志输出函数
def log_thread():
    try:
        while log_status:
            if len(ui.logs) > 0 and offset < len(ui.logs):
                logbox_append('log', ui.logs[offset])
                offset += 1
            time.sleep(0.05)
    except Exception as e:
        print(e)
    print('thread end')

def start_web():
    start_server(ui.render, port=9091, debug=True)

if __name__ == '__main__':
    start_web()

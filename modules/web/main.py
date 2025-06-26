import threading
import time
from datetime import datetime
from queue import Queue

from pywebio import SessionNotFoundException, config
from pywebio.input import FLOAT
from pywebio.output import (
    put_scope,
    use_scope,
    put_column,
    put_text,
    put_button,
    put_collapse,
    put_scrollable, put_row, )
from pywebio.pin import put_checkbox, pin_on_change, put_input
from pywebio.platform.tornado import start_server
from pywebio.session import set_env, register_thread

from modules.db.dbinit import Db
from modules.static.config_key_descriptions import key_descriptions
from modules.static.config_keys import *
from modules.web.process_mange import ProcessManager
from modules.web.utils import def_label_checkbox


def server():
    start_server(
        App().render, port=10965, auto_open_webbrowser=True, static_dir="./modules/web/static"
    )


class SessionManager:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = object.__new__(cls)
            cls.session_queues = []
        return cls.instance

    def run_in_all_sessions(self, func):
        for queue in self.session_queues:
            queue.put(func)

    def register(self, func):

        def decorator(*args, **kwargs):
            update_thread = threading.Thread(target=self.update_session, daemon=True)
            register_thread(update_thread)
            update_thread.start()

            res = func(*args, **kwargs)
            return res

        return decorator

    def update_session(self):
        try:
            queue = Queue()
            self.session_queues.append(queue)
            while True:
                func = queue.get()
                func()
        except SessionNotFoundException:
            print('关闭网页的一个链接了')


def update():
    pm = ProcessManager.get_instance()  # 获取 ProcessManager 单例
    last_index = len(pm.renderables)  # 初始化上次检查的索引
    while True:
        current_length = len(pm.renderables)

        # 情况1: 有新日志追加
        if current_length > last_index:
            new_logs = pm.renderables[last_index:current_length]
            # 处理新增的日志（例如发送到UI）
            for log in new_logs:
                put_text(log)
            last_index = current_length  # 更新索引

            # 情况2: 日志被裁剪（例如从400条裁剪到80条）
        elif current_length < last_index:
            new_logs = pm.renderables
            for log in new_logs:
                put_text(log)
            last_index = current_length
        time.sleep(0.5)  # 根据实际需求调整休眠时间


def output_fn():
    while True:
        SessionManager().run_in_all_sessions(update)
        time.sleep(1)


d = threading.Thread(target=output_fn, daemon=True)
d.start()


class App:
    def __init__(self):
        self.st = ProcessManager.get_instance()
        self.webdb = Db("task.db")

    @SessionManager().register
    def render(self):
        self.set_config()
        self.init_scope()
        with use_scope("log_area"):
            put_scrollable(put_scope("log"), height=600, keep_bottom=True)

        with use_scope("function", clear=True):
            self.render_process_btn()
            self.render_config()
            self.render_team()

    def set_config(self):
        set_env(output_max_width="100%")
        config(css_file='./static/style.css')

    def init_scope(self):
        put_scope(
            "main",
            [
                put_scope("memu").style("width:100px;"),
                put_scope("function").style("width:200px;"),
                put_scope("function_area").style("flex:1;"),
                put_scope("log_area").style("flex:1;"),
            ],
        ).style("display:flex")

    @use_scope("overview", clear=True)
    def render_process_btn(self):
        put_column(
            [
                put_text("调度器状态"),
                put_button(
                    label="停止" if self.st.alive else "启动", onclick=self.anew_render
                ),
            ]
        )

    def set_dispath_state(self, state):
        if state:
            self.st.stop()
        else:
            self.st.start()

    def anew_render(self):
        self.set_dispath_state(self.st.alive)
        self.render_process_btn()

    @use_scope("config", clear=True)
    def render_config(self):
        put_collapse("配置", [put_text("模拟器").onclick(self.render_simulator)])

    @use_scope("team", clear=True)
    def render_team(self):
        put_collapse('个人', [
            put_collapse('扫荡', [
                put_text('扫荡').onclick(self.render_practice_land),
                put_text('扫荡1').onclick(self.render_practice_land_1),
                put_text('扫荡2').onclick(self.render_practice_land_2),
                put_text('扫荡3').onclick(self.render_practice_land_3),
                put_text('扫荡4').onclick(self.render_practice_land_4),
            ]),
            put_collapse('出征', [
                put_text('出征').onclick(self.render_attack_land),
                put_text('出征1').onclick(self.render_attack_land_1),
                put_text('出征2').onclick(self.render_attack_land_2),
                put_text('出征3').onclick(self.render_attack_land_3),
                put_text('出征4').onclick(self.render_attack_land_4),
            ]),
            put_text('斯巴达模式').onclick(self.render_sparta_attack_land),
            put_text('打城').onclick(self.render_besiege),
            put_text('演武').onclick(self.render_martial_arts)
        ])
        put_collapse(
            "同盟",
            [
                put_text("武勋").onclick(self.render_exploit),
                put_text("排行榜数据").onclick(self.render_rangking),
                put_text("主力查询").onclick(self.render_enemy),
                put_text("战场翻地/拆除").onclick(self.render_battledestory),
                put_text("我方出战/防守").onclick(self.render_myfight),
            ],
        )

    @use_scope('function_area', clear=True)
    def render_martial_arts(self):
        current_config = self.webdb.select(ConfigSections.MartialArts)
        self.render_config_form(current_config, ConfigSections.MartialArts)

    @use_scope('function_area', clear=True)
    def render_practice_land(self):
        current_config = self.webdb.select(ConfigSections.PRACTICE_LAND)
        self.render_config_form(current_config, ConfigSections.PRACTICE_LAND)

    @use_scope('function_area', clear=True)
    def render_practice_land_1(self):
        current_config = self.webdb.select(ConfigSections.PRACTICE_LAND_1)
        self.render_config_form(current_config, ConfigSections.PRACTICE_LAND_1)

    @use_scope('function_area', clear=True)
    def render_practice_land_2(self):
        current_config = self.webdb.select(ConfigSections.PRACTICE_LAND_2)
        self.render_config_form(current_config, ConfigSections.PRACTICE_LAND_2)

    @use_scope('function_area', clear=True)
    def render_practice_land_3(self):
        current_config = self.webdb.select(ConfigSections.PRACTICE_LAND_3)
        self.render_config_form(current_config, ConfigSections.PRACTICE_LAND_3)

    @use_scope('function_area', clear=True)
    def render_practice_land_4(self):
        current_config = self.webdb.select(ConfigSections.PRACTICE_LAND_4)
        self.render_config_form(current_config, ConfigSections.PRACTICE_LAND_4)

    @use_scope('function_area', clear=True)
    def render_attack_land(self):
        current_config = self.webdb.select(ConfigSections.ATTACK_LAND)
        self.render_config_form(current_config, ConfigSections.ATTACK_LAND)

    @use_scope('function_area', clear=True)
    def render_attack_land_1(self):
        current_config = self.webdb.select(ConfigSections.ATTACK_LAND_1)
        self.render_config_form(current_config, ConfigSections.ATTACK_LAND_1)

    @use_scope('function_area', clear=True)
    def render_attack_land_2(self):
        current_config = self.webdb.select(ConfigSections.ATTACK_LAND_2)
        self.render_config_form(current_config, ConfigSections.ATTACK_LAND_2)

    @use_scope('function_area', clear=True)
    def render_attack_land_3(self):
        current_config = self.webdb.select(ConfigSections.ATTACK_LAND_3)
        self.render_config_form(current_config, ConfigSections.ATTACK_LAND_3)

    @use_scope('function_area', clear=True)
    def render_attack_land_4(self):
        current_config = self.webdb.select(ConfigSections.ATTACK_LAND_4)
        self.render_config_form(current_config, ConfigSections.ATTACK_LAND_4)

    @use_scope('function_area', clear=True)
    def render_sparta_attack_land(self):
        current_config = self.webdb.select(ConfigSections.SPARTA_ATTACK_LAND)
        self.render_config_form(current_config, ConfigSections.SPARTA_ATTACK_LAND)

    @use_scope('function_area', clear=True)
    def render_simulator(self):
        current_config = self.webdb.select('simulator')
        self.render_config_form(current_config, 'simulator')

    def is_date_string(self, s: str) -> bool:
        """检查字符串是否可以转换为日期时间"""
        try:
            datetime.strptime(s, "%Y/%m/%d %H:%M:%S")
            return True
        except ValueError:
            return False

    def render_config_form(self, config, name, scope='function_area'):
        config_dict = config[name]

        def render_bool(key, value):
            put_row([
                put_text(key_descriptions.get(key, '')),
                def_label_checkbox(put_checkbox(key, options=[True], value=value if value else []))
            ])
            pin_on_change(key, onchange=lambda v: self.update_checkbox(name, key, v), clear=True)

        def render_number(key, value):
            put_row([
                put_text(key_descriptions.get(key, '')),
                put_input(key, type=FLOAT, value=value)
            ])
            pin_on_change(key, onchange=lambda v: self.update_input(name, key, v), clear=True)

        def render_datetime(key, value):
            put_row([
                put_text(key_descriptions.get(key, '')),
                put_input(key, type='datetime-local',
                          value=datetime.strptime(value, "%Y/%m/%d %H:%M:%S").strftime("%Y-%m-%dT%H:%M"))
            ])
            pin_on_change(key, onchange=lambda v: self.update_datetime(name, key, v), clear=True)

        def render_string(key, value):
            put_row([
                put_text(key_descriptions.get(key, '')),
                put_input(key, value=value)
            ])
            pin_on_change(key, onchange=lambda v: self.update_input(name, key, v), clear=True)

        # 类型处理映射
        type_handlers = {
            bool: render_bool,
            int: render_number,
            float: render_number,
            str: lambda k, v: render_datetime(k, v) if self.is_date_string(v) else render_string(k, v)
        }

        with use_scope(scope):
            for key, value in config_dict.items():
                handler = type_handlers.get(type(value))
                if handler:
                    handler(key, value)

    @use_scope("function_area", clear=True)
    def render_besiege(self):
        current_config = self.webdb.select(ConfigSections.BESIEGE)
        self.render_config_form(current_config, ConfigSections.BESIEGE)

    @use_scope("function_area", clear=True)
    def render_exploit(self):
        current_config = self.webdb.select(ConfigSections.EXPLOIT)
        self.render_config_form(current_config, ConfigSections.EXPLOIT)

    @use_scope("function_area", clear=True)
    def render_rangking(self):
        current_config = self.webdb.select(ConfigSections.RANKING)
        self.render_config_form(current_config, ConfigSections.RANKING)

    @use_scope("function_area", clear=True)
    def render_enemy(self):
        current_config = self.webdb.select(ConfigSections.ENEMY)
        self.render_config_form(current_config, ConfigSections.ENEMY)

    @use_scope("function_area", clear=True)
    def render_battledestory(self):
        current_config = self.webdb.select(ConfigSections.BATTLEDESTORY)
        self.render_config_form(current_config, ConfigSections.BATTLEDESTORY)

    @use_scope("function_area", clear=True)
    def render_myfight(self):
        current_config = self.webdb.select(ConfigSections.MYFIGHT)
        self.render_config_form(current_config, ConfigSections.MYFIGHT)

    def update_input(self, task_name, prop, v):
        res = self.webdb.select_format(task_name)
        res.update({prop: v})
        self.webdb.update(task_name, res)

    def update_datetime(self, task_name, prop, v):
        dt = datetime.strptime(v, "%Y-%m-%dT%H:%M").strftime("%Y/%m/%d %H:%M:%S")
        res = self.webdb.select_format(task_name)
        res.update({prop: dt})
        self.webdb.update(task_name, res)

    def update_checkbox(self, config_name, prop, v):
        res = self.webdb.select_format(config_name)
        value = {prop: False}
        if len(v) == 1:
            value[prop] = True
        res.update(value)
        self.webdb.update(config_name, res)

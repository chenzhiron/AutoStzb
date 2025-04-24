import threading
import time
from queue import Queue

from pywebio import SessionNotFoundException
from pywebio.output import (
    put_scope,
    use_scope,
    put_column,
    put_text,
    put_button,
    put_collapse,
    put_scrollable,
)
from pywebio.platform.tornado import start_server
from pywebio.session import set_env, register_thread

from modules.db.dbinit import Db
from modules.web.process_mange import ProcessManager
from modules.web.utils import (
    render_checkbox,
    render_datetime,
    render_input,
    render_number
)


def server():
    web = app().render
    start_server(
        web, port=10965, auto_open_webbrowser=True, static_dir="./modules/web/static"
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

        # 降低CPU占用
        time.sleep(0.5)  # 根据实际需求调整休眠时间


def output_fn():
    while True:
        SessionManager().run_in_all_sessions(update)
        time.sleep(1)


d = threading.Thread(target=output_fn, daemon=True)
d.start()


class app:
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

    @use_scope("function_area", clear=True)
    def render_simulator(self):
        render_input(
            "simulator",
            "模拟器地址",
            "address",
            self.webdb.select_format("simulator"),
            self.update_input,
        )

    def update_input(self, taskname, prop, v):
        res = self.webdb.select_format(taskname)
        res.update({prop: v})
        self.webdb.update(taskname, res)

    def updatecheckbox(self, taskname, prop, v):
        res = self.webdb.select_format(taskname)
        value = {prop: False}
        if len(v) == 1:
            value[prop] = True
        res.update(value)
        self.webdb.update(taskname, res)

    @use_scope("team", clear=True)
    def render_team(self):
        put_collapse(
            "同盟",
            [
                put_text("打城主力拆迁").onclick(self.render_besiege),
                put_text("武勋").onclick(self.render_exploit),
                put_text("排行榜数据").onclick(self.render_rangking),
                put_text("敌军主力").onclick(self.render_enemymain),
                put_text("战场翻地/拆除").onclick(self.render_battledestory),
                put_text("我方出战/防守").onclick(self.render_myfight),
            ],
        )

    # 主力跟拆迁一起统计，因为他们的配置和执行是一样的
    @use_scope("function_area", clear=True)
    def render_besiege(self):
        render_checkbox(
            "besiege",
            "状态",
            "state",
            self.webdb.select_format("besiege"),
            self.updatecheckbox,
        )
        render_datetime(
            "besiege",
            "下一次运行时间",
            "nexttime",
            self.webdb.select_format("besiege"),
            self.update_input,
        )

    @use_scope("function_area", clear=True)
    def render_exploit(self):
        render_checkbox(
            "exploit",
            "状态",
            "state",
            self.webdb.select_format("exploit"),
            self.updatecheckbox,
        )

    @use_scope("function_area", clear=True)
    def render_rangking(self):
        render_checkbox(
            "ranking",
            "状态",
            "state",
            self.webdb.select_format("ranking"),
            self.updatecheckbox,
        )

    @use_scope("function_area", clear=True)
    def render_enemymain(self):
        render_checkbox(
            "enemy",
            "状态",
            "state",
            self.webdb.select_format("enemy"),
            self.updatecheckbox,
        )
        render_datetime(
            "enemy",
            "下一次运行时间",
            "nexttime",
            self.webdb.select_format("enemy"),
            self.update_input,
        )
        render_input(
            "enemy",
            "等待多少分钟开启下一次扫描",
            "looptime",
            self.webdb.select_format("enemy"),
            self.update_input,
        )
        render_datetime(
            "enemy",
            "结束统计时间",
            "endtime",
            self.webdb.select_format("enemy"),
            self.update_input,
        )

    @use_scope("function_area", clear=True)
    def render_battledestory(self):
        render_checkbox(
            "battledestory",
            "状态",
            "state",
            self.webdb.select_format("battledestory"),
            self.updatecheckbox,
        )
        render_datetime(
            "battledestory",
            "下一次运行时间",
            "nexttime",
            self.webdb.select_format("battledestory"),
            self.update_input,
        )
        render_number(
            "battledestory",
            "等待多少分钟开启下一次扫描",
            "looptime",
            self.webdb.select_format("battledestory"),
            self.update_input,
        )
        render_datetime(
            "battledestory",
            "结束统计时间",
            "endtime",
            self.webdb.select_format("battledestory"),
            self.update_input,
        )

    @use_scope("function_area", clear=True)
    def render_myfight(self):
        render_checkbox(
            "myfight",
            "状态",
            "state",
            self.webdb.select_format("myfight"),
            self.updatecheckbox,
        )
        render_datetime(
            "myfight",
            "下一次运行时间",
            "nexttime",
            self.webdb.select_format("myfight"),
            self.update_input,
        )
        render_datetime(
            "myfight",
            "结束统计时间",
            "endtime",
            self.webdb.select_format("myfight"),
            self.update_input,
        )

from pywebio.platform.tornado import start_server
from pywebio.output import (
    put_scope,
    use_scope,
    put_column,
    put_text,
    put_button,
    put_collapse,
    put_scrollable,
)
from pywebio.session import set_env, register_thread
from pywebio import config


from db import Db
from modules.web.logthread import LogThread
from modules.static.propname import *
from modules.web.utils import (
    render_checkbox,
    render_datetime,
    render_input,
    render_number,
)

from modules.web.process_mange import ProcessManage


def server():
    web = app().render
    start_server(
        web, port=10965, auto_open_webbrowser=True, static_dir="./modules/web/static"
    )


class app:
    def __init__(self):
        self.webdb = Db("task.db")
        self.webdb.init_conn()

        self.st = ProcessManage.get_manager()

    def render(self):
        config(css_file="./static/style.css")
        _logthread = LogThread()

        self.set_config()
        self.init_scope()
        with use_scope("log_area"):
            put_scrollable(put_scope("log"), height=600, keep_bottom=True)

        with use_scope("function", clear=True):
            self.render_process_btn()
            self.render_config()
            self.render_team()

        register_thread(_logthread.log_thread)
        _logthread.start()

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
                    label="停止" if self.st.state else "启动", onclick=self.anew_render
                ),
            ]
        )

    def set_dispath_state(self, state):
        if state:
            self.st.stop()
        else:
            self.st.start()

    def anew_render(self):
        self.set_dispath_state(self.st.state)
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

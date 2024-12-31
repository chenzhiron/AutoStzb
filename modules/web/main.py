from pywebio.platform.tornado import start_server
from pywebio.output import (
    put_scope,
    use_scope,
    put_column,
    put_text,
    put_button,
    put_collapse,
)
from pywebio.session import set_env
from pywebio import config


from modules.web.taskState import basic
from modules.static.propname import *
from modules.web.utils import (
    render_checkbox,
    render_datetime,
    render_input,
    render_number,
)

# from modules.web.function import private
from modules.web.process_mange import ProcessManage

def server():
    web = app().render

    start_server(
        web, port=10965, auto_open_webbrowser=True, static_dir="./modules/web/static"
    )


class app(basic):
    def __init__(self):
        super().__init__()
        self.st = ProcessManage.get_manager()

    def render(self):
        self.initialze()
        config(css_file="./static/style.css")
        self.set_config()
        self.init_scope()

        with use_scope("function", clear=True):
            self.render_process_btn()
            self.render_config()
            self.render_team()
            # private.render()

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
            "模拟器地址", "address", self.taskConfig["simulator"], self.update_input
        )

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
        c_obj = self.taskConfig["besiege"]
        render_checkbox("状态", "state", c_obj, self.update_checkbox)
        render_datetime("下一次运行时间", "nexttime", c_obj, self.update_input)

    @use_scope("function_area", clear=True)
    def render_exploit(self):
        c_obj = self.taskConfig["exploit"]
        render_checkbox("状态", "state", c_obj, self.update_checkbox)

    @use_scope("function_area", clear=True)
    def render_rangking(self):
        c_obj = self.taskConfig["ranking"]
        render_checkbox("状态", "state", c_obj, self.update_checkbox)

    @use_scope("function_area", clear=True)
    def render_enemymain(self):
        c_obj = self.taskConfig["enemy"]
        render_checkbox("状态", "state", c_obj, self.update_checkbox)
        render_datetime("下一次运行时间", "nexttime", c_obj, self.update_input)
        render_input("等待多少分钟开启下一次扫描", "looptime", c_obj, self.update_input)
        render_datetime("结束统计时间", "endtime", c_obj, self.update_input)

    @use_scope("function_area", clear=True)
    def render_battledestory(self):
        c_obj = self.taskConfig["battledestory"]
        render_checkbox("状态", "state", c_obj, self.update_checkbox)
        render_datetime("下一次运行时间", "nexttime", c_obj, self.update_input)
        render_number(
            "等待多少分钟开启下一次扫描", "looptime", c_obj, self.update_input
        )
        render_datetime("结束统计时间", "endtime", c_obj, self.update_input)

    @use_scope("function_area", clear=True)
    def render_myfight(self):
        c_obj = self.taskConfig["myfight"]
        render_checkbox("状态", "state", c_obj, self.update_checkbox)
        render_datetime("下一次运行时间", "nexttime", c_obj, self.update_input)
        render_datetime("结束统计时间", "endtime", c_obj, self.update_input)

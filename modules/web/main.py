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
from pywebio.pin import pin_on_change, put_checkbox, put_input
from pywebio import config

from modules.web.taskState import StDispatch
from modules.static.propname import *
from modules.allprop import allprops, update, updatecheckbox
from modules.web.utils import def_lable_checkbox, explain_componet
from .function import private
from .process_mange import ProcessManage


stdispath = StDispatch()


def server():
    web = app().render

    start_server(
        web, port=10965, auto_open_webbrowser=True, static_dir="./modules/web/static"
    )


class app:
    def __init__(self):
        self.st = ProcessManage.get_manager()
        stdispath.update_pm(self.st)
        stdispath.start()

    def render(self):
        stdispath.register()
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
            self.st.start(allprops)

    def anew_render(self):
        self.set_dispath_state(self.st.state)
        self.render_process_btn()

    @use_scope("config", clear=True)
    def render_config(self):
        put_collapse("配置", [put_text("模拟器").onclick(self.render_simulator)])

    @use_scope("function_area", clear=True)
    def render_simulator(self):
        explain_componet(
            ["模拟器地址"],
            put_input(simulator_address, value=allprops[simulator_address]),
        )
        pin_on_change(
            simulator_address, onchange=lambda v: update(allprops, simulator_address, v)
        )

    @use_scope("team", clear=True)
    def render_team(self):
        put_collapse(
            "同盟",
            [
                put_text("打城主力").onclick(self.render_besiegemain),
                put_text("打城拆迁").onclick(self.render_basiegedestory),
                put_text("武勋").onclick(self.render_exploit),
                put_text("排行榜数据").onclick(self.render_rangking),
                put_text("敌军主力").onclick(self.render_enemymain),
                put_text("战场翻地/拆除").onclick(self.render_battledestory),
                put_text("我方出战/防守").onclick(self.render_myfight),
            ],
        )

    @use_scope("function_area", clear=True)
    def render_besiegemain(self):
        explain_componet(
            ["状态"],
            def_lable_checkbox(
                put_checkbox(
                    besiegemain_state, options=[True], value=allprops[besiegemain_state]
                )
            ),
        )
        pin_on_change(
            besiegemain_state,
            onchange=lambda v: updatecheckbox(allprops, besiegemain_state, v),
            clear=True,
        )

    @use_scope("function_area", clear=True)
    def render_basiegedestory(self):
        explain_componet(
            ["状态"],
            def_lable_checkbox(
                put_checkbox(
                    basiegedestory_state,
                    options=[True],
                    value=allprops[basiegedestory_state],
                )
            ),
        )
        pin_on_change(
            basiegedestory_state,
            onchange=lambda v: updatecheckbox(allprops, basiegedestory_state, v),
            clear=True,
        )

    @use_scope("function_area", clear=True)
    def render_exploit(self):
        explain_componet(
            ["状态"],
            def_lable_checkbox(
                put_checkbox(
                    exploit_state, options=[True], value=allprops[exploit_state]
                )
            ),
        )
        pin_on_change(
            exploit_state,
            onchange=lambda v: updatecheckbox(allprops, exploit_state, v),
            clear=True,
        )

    @use_scope("function_area", clear=True)
    def render_rangking(self):
        explain_componet(
            ["状态"],
            def_lable_checkbox(
                put_checkbox(
                    ranking_state, options=[True], value=allprops[ranking_state]
                )
            ),
        )
        pin_on_change(
            ranking_state,
            onchange=lambda v: updatecheckbox(allprops, ranking_state, v),
            clear=True,
        )

    @use_scope("function_area", clear=True)
    def render_enemymain(self):
        explain_componet(
            ["状态"],
            def_lable_checkbox(
                put_checkbox(
                    enemymain_state, options=[True], value=allprops[enemymain_state]
                )
            ),
        )
        pin_on_change(
            enemymain_state,
            onchange=lambda v: updatecheckbox(allprops, enemymain_state, v),
            clear=True,
        )

    @use_scope("function_area", clear=True)
    def render_battledestory(self):
        explain_componet(
            ["状态"],
            def_lable_checkbox(
                put_checkbox(
                    battledestory_state,
                    options=[True],
                    value=allprops[battledestory_state],
                )
            ),
        )
        pin_on_change(
            battledestory_state,
            onchange=lambda v: updatecheckbox(allprops, battledestory_state, v),
            clear=True,
        )

    @use_scope("function_area", clear=True)
    def render_myfight(self):
        explain_componet(
            ["状态"],
            def_lable_checkbox(
                put_checkbox(
                    myfight_state, options=[True], value=allprops[myfight_state]
                )
            ),
        )
        pin_on_change(
            myfight_state,
            onchange=lambda v: updatecheckbox(allprops, myfight_state, v),
            clear=True,
        )
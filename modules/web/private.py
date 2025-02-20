from pywebio.output import use_scope, put_collapse, put_text

from pywebio.output import use_scope, put_tabs
from pywebio.pin import pin_on_change, put_input, put_checkbox
from modules.web.utils import def_lable_checkbox, explain_componet


class SweepProp:
    def __init__(self, index):
        self._index = index
        self.all_state = True
        self.name = ""
        self.next_time = ""
        self.x = 0
        self.y = 0

    def set_all_state(self, state):
        self.all_state = len(state) == 0
        print(self.all_state)

    def set_name(self, name):
        self.name = name

    def set_next_time(self, time):
        self.next_time = time

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_all_state(self):
        return self.all_state

    def get_name(self):
        return self.name

    def get_next_time(self):
        return self.next_time

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class SweepItem:
    def __init__(self, prop):
        self.prop = prop

    def render(self):
        stall_all = "stall_all" + self.prop._index
        next_time = "next_time" + self.prop._index
        x = "x" + self.prop._index
        y = "y" + self.prop._index

        renders = [
            explain_componet(
                ["状态"],
                def_lable_checkbox(
                    put_checkbox(
                        stall_all, options=[True], value=self.prop.get_all_state()
                    )
                ),
            ),
            explain_componet(
                ["下次执行时间", "任务下一次执行的时间, 一般不需要手动更改"],
                put_input(next_time, value=self.prop.get_next_time()),
            ),
            explain_componet(["X坐标"], put_input(x, value=self.prop.get_x())),
            explain_componet(["Y坐标"], put_input(y, value=self.prop.get_y())),
        ]

        pin_on_change(stall_all, onchange=self.prop.set_all_state, clear=True)
        pin_on_change(next_time, onchange=self.prop.set_next_time, clear=True)
        return renders


class SweepArea:
    def __init__(self, prop_objs):
        self.prop_objs = prop_objs

    @use_scope("function_area", clear=True)
    def render(self):
        put_tabs(
            [
                {"title": "队伍1", "content": SweepItem(self.prop_objs[0]).render()},
                {"title": "队伍2", "content": SweepItem(self.prop_objs[1]).render()},
                {"title": "队伍3", "content": SweepItem(self.prop_objs[2]).render()},
                {"title": "队伍4", "content": SweepItem(self.prop_objs[3]).render()},
                {"title": "队伍5", "content": SweepItem(self.prop_objs[4]).render()},
            ]
        ).style("width:500px;")


sweep_props = [
    SweepProp("1"),
    SweepProp("2"),
    SweepProp("3"),
    SweepProp("4"),
    SweepProp("5"),
]
sweeps = SweepArea(sweep_props)


class Private:
    def __init__(self):
        pass

    @use_scope("private", clear=True)
    def render(self):
        put_collapse(
            "势力",
            [
                put_text("扫荡").onclick(sweeps.render),
                put_text("出征"),
                put_text("征兵"),
            ],
        )

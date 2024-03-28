from pywebio.output import put_column, put_text, put_row
from pywebio.pin import put_input, put_checkbox, put_select

class Component:
    def __init__(self, key, value, types, args=None) -> None:
        self.key = key
        self.value = value
        self.types = types
        self.args = args
        self.controller = None
        self.dispatch()

    def dispatch(self):
        if self.types == 'int':
            self.controller = put_input(self.key, value=str(self.value))
        if self.types == 'str':
            self.controller = put_input(self.key, value=self.value)
        if self.types == 'bool':
            self.controller = put_checkbox(self.key, value=[self.value], options=[self.value])
            res = self.controller.spec['input']['options']
            for v in res:
                v['label'] = ''
        if self.types == 'options':
            self.controller = put_select(self.key, value=self.value, options=self.args)
    def listen(self):
        pass



class Option:
    def __init__(self, explain:list, component: Component) -> None:
        self.options = None
        self.explain = explain
        self.component = component
        self.dispatch()

    def dispatch(self):
        self.options = put_row(
            [
                put_column(list(map(lambda v: put_text(v), self.explain))),
                self.component.controller
            ]
           )


class OptionPage:
    def __init__(self, currentobj) -> None:
        self.currentobj = currentobj
        
    def dispatch(self):
        for key, values in self.currentobj.items():
            Option([key.display_name], Component(key.name, values, key.option_type, args=key.options)).options

# 示例
#   OptionPage({
#         team: 1,
#         skip_await: False,
#         state: False,
#         explain: '',
#         await_time: 0,
#         next_run_time: '2024-01-01 00:00:00',
#         mopping_up: False,
#         delay: 0,
#         draw_txt: '',
#         residue_troops_person: 0.5,
#         residue_troops_enemy: 0.5
#     }).dispatch()

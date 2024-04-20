import functools

from pywebio.output import put_column, put_text, put_row
from pywebio.pin import put_input, put_checkbox, put_select, pin_on_change

class Component:
    def __init__(self, key, value, types, event, args=None) -> None:
        self.key = key
        self.value = value
        self.types = types
        self.event = event
        self.args = args
        self.controller = None
        self.dispatch()

    def dispatch(self):
        if self.types == 'int':
            self.controller = put_input(self.key, value=str(self.value))
        if self.types == 'str':
            self.controller = put_input(self.key, value=self.value)
        if self.types == 'bool':
            # True or False
            # conversions 
            # value True or None ;;; options [True] 
            self.controller = put_checkbox(self.key, 
                                           value= self.value if self.value else None,
                                           options= [self.value] if self.value else [True])
            res = self.controller.spec['input']['options']
            for v in res:
                v['label'] = ''
        if self.types == 'options':
            self.controller = put_select(self.key, value=self.value, options=self.args)
        pin_on_change(self.key, self.event, True)

class Option:
    def __init__(self, explain:list, component: Component) -> None:
        self.options = None
        self.explain = explain
        self.component = component
        self.dispatch()

    def dispatch(self):
        self.options = put_row(
            [
                put_column(list(map(lambda v: put_text(v), self.explain)), size='20px').style('font-size: 15px;'),
                self.component.controller
            ]
           )


class OptionPage:
    def __init__(self, datalists) -> None:
        self.origin_data = datalists[0]
        self.datalists = datalists[1]
        
    def dispatch(self):
        for key, values in self.datalists.items():
            Option(
                key.display_name, Component(key.name, values, key.option_type,
                                                  event=functools.partial(
                                                      key.on_change_event,
                                                      origin_controller=self.datalists,
                                                      origin=self.origin_data
                                                    ), 
                                            args=key.options)
                                        ).options

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

import functools

from pywebio.output import put_column, put_text, put_row
from pywebio.pin import put_input, put_checkbox, put_select, pin_on_change

from modules.web.components.prop_all import propall

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
    def render(self):
        self.options


class OptionPage:
    def __init__(self, datalists) -> None:
        self.data = datalists
        
    def dispatch(self):
        for key, values in self.data.items():
            if key == 'battle_info' or key == 'steps':
                continue
            prop_component = propall[key]
            Option(
                prop_component.display_name, 
                Component(prop_component.name, values, prop_component.option_type,
                          event=functools.partial(prop_component.on_change_event, origin=self.data,keyss=key),
                          args=prop_component.options)
                                        ).render()

import time

import pywebio
from pywebio import start_server

from pywebio.output import put_button, use_scope, put_collapse, put_text, put_scope, clear, remove
from pywebio.pin import put_input, put_checkbox, pin_on_change

from modules.web.config import WebConfig
from modules.store.store import store
from modules.devices.device import Devices

pywebio.config(css_style="""
    * {
        margin: 0 ;
        padding: 0 ;
    }
    .container {padding:0;
    margin:0;
    max-width: 100%;
    }
    .pywebio {
        padding:0;
    }
    .footer{
        display: none;
        }
""")


class WebConfigUI(WebConfig):
    def __init__(self):
        super().__init__()
        self.state = False
        self.store = store

    def get_state(self):
        return self.state

    def start(self):
        start_server(self.init, port=9091, auto_open_webbrowser=True, debug=True)

    def init(self):
        self.format_com([self.config_data, self.main_data])
        while 1:
            res = self.store.get_store()
            if bool(res):
                self.update_main_data(res)
                remove('aside')
                remove('collapse')
                remove('center')
                self.format_com([self.config_data, self.main_data])
            time.sleep(5)

    def update_main_refresh(self, new_data):
        """更新数据并刷新UI视图。"""
        super().update_main_data(new_data)
        self.refresh_view()

    def update_config_refresh(self, new_data):
        """更新数据并刷新UI视图。"""
        super().update_config_data(new_data)
        self.refresh_view()

    def refresh_view(self):
        self.init()  # 重新初始化视图

    def change_config(self):
        self.state = not self.state

    def format_com(self, data):

        aside_elements = [self.components_aside(v) for v in data]
        with use_scope('scheduler', clear=True):
            put_text('调度器状态').style('display:inline-block;'),
            put_button('运行中' if self.state else '启动', onclick=self.change_config).style(
                'display:inline-block;')
        with use_scope('st', clear=True):
            put_scope('aside', aside_elements).style('width:100px;display:inline-block;')
            put_scope('collapse', []).style('width:200px;display:inline-block;')
            put_scope('center', []).style('flex:1;display:inline-block;')

    def components_aside(self, aside):
        return put_button(aside['name'], onclick=self.components_collapse(aside['children'], aside['name']))

    def components_collapse(self, collapse, title):
        def render():
            collapse_group = [self.cvcomponents_aside(v) for v in collapse]
            for v in collapse:
                clear(v['scope'])
            for v in collapse:
                with use_scope(v['scope'], clear=True):
                    put_collapse(title, collapse_group)

        return render

    def cvcomponents_aside(self, aside):
        return put_button(aside['name'], onclick=self.components_collapse_button(aside['children']))

    def components_collapse_button(self, aside):
        def render():
            with use_scope('center', clear=True):
                for key, value in aside.items():
                    if value['show'] or value['value'] is not None:
                        if isinstance(value['value'], bool):
                            with use_scope(key, clear=True):
                                put_text(value['explain']),
                                put_checkbox(key, [{'label': '', 'value': True}], value=[value['value']]
                                             ).style('display:grid;grid-template-columns:auto auto;')
                            pin_on_change(key, self.pin_change_bool(self, value), clear=True)
                        else:
                            with use_scope(key, clear=True):
                                put_text(value['explain']),
                                put_input(key, value=str(value['value']), readonly=value['readonly']
                                          ).style('display:grid;grid-template-columns:auto auto;')
                            pin_on_change(key, self.reg_str(self, value), clear=True)
                    else:
                        put_text(value['explain'])

        return render

    @staticmethod
    def pin_change_bool(self, v):
        def render(i):
            if len(i) > 0:
                v['value'] = True
            else:
                v['value'] = False

        return render

    @staticmethod
    def reg_str(self, item):
        def render(v):
            if v is None:
                return None
            item['value'] = v

        return render

    # @staticmethod
    # def clear(scope_name):
    #     # 实现清除作用域的静态方法
    #     clear(scope_name)


ui = WebConfigUI()

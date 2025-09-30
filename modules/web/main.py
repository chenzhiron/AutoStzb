from datetime import datetime
from functools import partial

from pywebio import config
from pywebio.input import FLOAT
from pywebio.output import (
    put_scope,
    use_scope,
    put_column,
    put_text,
    put_button,
    put_collapse,
    put_row, put_buttons, scroll_to, )
from pywebio.pin import put_checkbox, pin_on_change, put_input, put_select
from pywebio.platform.tornado import start_server
from pywebio.session import set_env

from modules.db.dbinit import Db
from modules.static.config_keys import *
from modules.static.web_render_config import web_render_config, field_categories
from modules.web.process_mange import ProcessManager
from modules.web.utils import def_label_checkbox


def server():
    config(css_file='./static/style.css')
    start_server(
        App().render, port=10965, auto_open_webbrowser=True, static_dir="./modules/web/static",
    )


class App:
    def __init__(self):
        self.st = ProcessManager.get_instance()
        self.webdb = Db("task.db")

    def render(self):
        self.set_config()
        self.init_scope()

        with use_scope("memu", clear=True):
            self.render_process_btn()
            self.render_config()
            self.render_team()

    def set_config(self):
        set_env(output_max_width="100%")

    def init_scope(self):
        put_scope(
            "main",
            [
                put_scope("memu").style("width:200px;"),
                put_scope("function_area").style("width:900px;padding:20px;"),
            ],
        ).style("width:1200px;display:flex;margin:0 auto;")

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
            put_text('打城').onclick(self.render_fight_city),
            put_text('演武').onclick(self.render_martial_arts)
        ])

    @use_scope('function_area', clear=True)
    def render_martial_arts(self):
        current_config = self.webdb.select(ConfigSections.MartialArts)
        self.render_config_form(current_config, ConfigSections.MartialArts,
                                web_render_config[ConfigSections.MartialArts])

    @use_scope('function_area', clear=True)
    def render_practice_land(self):
        current_config = self.webdb.select(ConfigSections.PRACTICE_LAND)
        self.render_config_form(current_config, ConfigSections.PRACTICE_LAND,
                                web_render_config[ConfigSections.PRACTICE_LAND])

    @use_scope('function_area', clear=True)
    def render_practice_land_1(self):
        current_config = self.webdb.select(ConfigSections.PRACTICE_LAND_1)
        self.render_config_form(current_config, ConfigSections.PRACTICE_LAND_1,
                                web_render_config[ConfigSections.PRACTICE_LAND_1])

    @use_scope('function_area', clear=True)
    def render_practice_land_2(self):
        current_config = self.webdb.select(ConfigSections.PRACTICE_LAND_2)
        self.render_config_form(current_config, ConfigSections.PRACTICE_LAND_2,
                                web_render_config[ConfigSections.PRACTICE_LAND_2])

    @use_scope('function_area', clear=True)
    def render_practice_land_3(self):
        current_config = self.webdb.select(ConfigSections.PRACTICE_LAND_3)
        self.render_config_form(current_config, ConfigSections.PRACTICE_LAND_3,
                                web_render_config[ConfigSections.PRACTICE_LAND_3])

    @use_scope('function_area', clear=True)
    def render_practice_land_4(self):
        current_config = self.webdb.select(ConfigSections.PRACTICE_LAND_4)
        self.render_config_form(current_config, ConfigSections.PRACTICE_LAND_4,
                                web_render_config[ConfigSections.PRACTICE_LAND_4])

    @use_scope('function_area', clear=True)
    def render_attack_land(self):
        current_config = self.webdb.select(ConfigSections.ATTACK_LAND)
        self.render_config_form(current_config, ConfigSections.ATTACK_LAND,
                                web_render_config[ConfigSections.ATTACK_LAND])

    @use_scope('function_area', clear=True)
    def render_attack_land_1(self):
        current_config = self.webdb.select(ConfigSections.ATTACK_LAND_1)
        self.render_config_form(current_config, ConfigSections.ATTACK_LAND_1,
                                web_render_config[ConfigSections.ATTACK_LAND_1])

    @use_scope('function_area', clear=True)
    def render_attack_land_2(self):
        current_config = self.webdb.select(ConfigSections.ATTACK_LAND_2)
        self.render_config_form(current_config, ConfigSections.ATTACK_LAND_2,
                                web_render_config[ConfigSections.ATTACK_LAND_2])

    @use_scope('function_area', clear=True)
    def render_attack_land_3(self):
        current_config = self.webdb.select(ConfigSections.ATTACK_LAND_3)
        self.render_config_form(current_config, ConfigSections.ATTACK_LAND_3,
                                web_render_config[ConfigSections.ATTACK_LAND_3])

    @use_scope('function_area', clear=True)
    def render_attack_land_4(self):
        current_config = self.webdb.select(ConfigSections.ATTACK_LAND_4)
        self.render_config_form(current_config, ConfigSections.ATTACK_LAND_4,
                                web_render_config[ConfigSections.ATTACK_LAND_4])

    @use_scope('function_area', clear=True)
    def render_sparta_attack_land(self):
        current_config = self.webdb.select(ConfigSections.SPARTA_ATTACK_LAND)
        self.render_config_form(current_config, ConfigSections.SPARTA_ATTACK_LAND,
                                web_render_config[ConfigSections.SPARTA_ATTACK_LAND])

    @use_scope('function_area', clear=True)
    def render_simulator(self):
        current_config = self.webdb.select(ConfigSections.SIMULATOR)
        self.render_config_form(current_config, ConfigSections.SIMULATOR, web_render_config[ConfigSections.SIMULATOR])

    def is_date_string(self, s: str) -> bool:
        """检查字符串是否可以转换为日期时间"""
        try:
            datetime.strptime(s, "%Y/%m/%d %H:%M:%S")
            return True
        except ValueError:
            return False

    def render_config_form(self, config, name, web_config, scope='function_area'):
        config_dict = config[name]

        def render_checkbox(key, value):
            put_row([
                put_column([
                    put_text(web_config['fields'][key]['display_name']).style('font-size:18px;font-width:600;'),
                    put_text(web_config['fields'][key]['description']).style('color:#777'),
                ]),
                def_label_checkbox(put_checkbox(key, options=[True], value=value if value else []))
            ])
            pin_on_change(key, onchange=lambda v: self.update_checkbox(name, key, v), clear=True)

        def render_number(key, value):
            put_row([
                put_column([
                    put_text(web_config['fields'][key]['display_name']).style('font-size:18px;font-width:600;'),
                    put_text(web_config['fields'][key]['description']).style('color:#777'),
                ]),
                put_input(key, type=FLOAT, value=value)
            ])
            pin_on_change(key, onchange=lambda v: self.update_input(name, key, v), clear=True)

        def render_datetime(key, value):
            put_row([
                put_column([
                    put_text(web_config['fields'][key]['display_name']).style('font-size:18px;font-width:600;'),
                    put_text(web_config['fields'][key]['description']).style('color:#777'),
                ]),
                put_input(key, type='datetime-local',
                          value=datetime.strptime(value, "%Y/%m/%d %H:%M:%S").strftime("%Y-%m-%dT%H:%M"))
            ])
            pin_on_change(key, onchange=lambda v: self.update_datetime(name, key, v), clear=True)

        def render_string(key, value):
            put_row([
                put_column([
                    put_text(web_config['fields'][key]['display_name']).style('font-size:18px;font-width:600;'),
                    put_text(web_config['fields'][key]['description']).style('color:#777'),
                ]),
                put_input(key, value=value)
            ])
            pin_on_change(key, onchange=lambda v: self.update_input(name, key, v), clear=True)

        def render_select(key, value):
            put_row([
                put_column([
                    put_text(web_config['fields'][key]['display_name']).style('font-size:18px;font-width:600;'),
                    put_text(web_config['fields'][key]['description']).style('color:#777'),
                ]),
                put_select(key, web_config['fields'][key]['option'], value=value)
            ])
            pin_on_change(key, onchange=lambda v: self.update_input(name, key, v), clear=True)

        # 类型处理映射
        type_handlers = {
            "checkbox": render_checkbox,
            "str": render_string,
            "option": render_select,
            "datetime": render_datetime,
            "number": render_number,
        }

        with use_scope(scope):
            fields_group = {}
            fields_sorted_group = []
            for k, v in web_config['fields'].items():
                if v['category'] in fields_group:
                    fields_group[v['category']].append(k)
                else:
                    fields_group[v['category']] = [k]
                    fields_sorted_group.append(v['category'])
            fields_sorted_group.sort(key=self.filed_sort)
            render_fields_group = []
            render_fields_event = []
            for k in fields_sorted_group:
                render_fields_group.append({
                    "label": field_categories[k]['display_name'],
                    "value": field_categories[k]
                })
                render_fields_event.append(partial(self.go_to_area, v=k))

            with use_scope('title'):
                put_text(web_config['display_name']).style('font-size:30px;font-size:700;'),
                put_text(web_config['description']).style(''),
                put_buttons(render_fields_group, onclick=render_fields_event)

            for v in fields_sorted_group:
                with use_scope(v):
                    put_text(field_categories[v]['display_name']).style('font-size:24px;font-size:700;'),
                    for k in fields_group[v]:
                        handle = type_handlers.get(web_config['fields'][k]['input_type'], None)
                        if handle:
                            handle(k, config_dict[k])

    def go_to_area(self, v):
        scroll_to(v)

    def filed_sort(self, elem):
        return field_categories[elem]['order']

    @use_scope("function_area", clear=True)
    def render_fight_city(self):
        current_config = self.webdb.select(ConfigSections.FIGHT_CITY)
        self.render_config_form(current_config, ConfigSections.FIGHT_CITY, web_render_config[ConfigSections.FIGHT_CITY])

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

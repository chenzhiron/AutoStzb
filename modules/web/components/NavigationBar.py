from pywebio.output import put_row, put_scope
from pywebio import start_server
import functools
from pywebio.output import put_button, put_collapse,  use_scope
from Option import OptionPage
from prop_all import * 


class NavigationBar:
    def __init__(self):
        self.config = {
            'buttons': [
                {'label': '主城', 'onclick': self.function_bar},
            ]
        }

    def function_bar(self):
        with use_scope('function_bar',clear=True):
            put_collapse('编队', [
                put_row([
                    put_button('编队一', onclick= self.menu_bar),
                ])
            ])

    def menu_bar(self):
        with use_scope('menu_bar',clear=True):
                OptionPage({
                    team: 1,
                    skip_await: False,
                    state: False,
                    explain: '',
                    await_time: 0,
                    next_run_time: '2024-01-01 00:00:00',
                    mopping_up: False,
                    delay: 0,
                    draw_txt: '',
                    residue_troops_person: 0.5,
                    residue_troops_enemy: 0.5
                }).dispatch()

    def init(self):
        put_row([
            put_scope('navigation_bar', []),
            put_scope('function_bar', []),
            put_scope('menu_bar', []),
            put_scope('log_bar', [])
        ]).style('display:flex')
        self.render_navigation_bar()

    def render_navigation_bar(self):
        with use_scope('navigation_bar', clear=True):
            put_collapse('任务', [
                put_row([
                    put_button(button['label'], onclick=button['onclick']) for button in self.config['buttons']
                ])
            ])
def init():
    # To use the NavigationBar class
    nav_bar = NavigationBar()
    nav_bar.init()

if __name__=='__main__':
    start_server(init, port=9091, debug=True)

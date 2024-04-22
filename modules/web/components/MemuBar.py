import functools
from pywebio.output import use_scope, put_collapse,put_button, put_text, put_image

from modules.web.components.Option import *
from modules.web.components.prop_all import *


class MemuBar:
    def __init__(self):
        pass
    @use_scope('navigation_bar', clear=True)
    def render_navigation_bar(self):
        self.clear_area()
        tasks_render = []
        for v in self.data['task']:
            tasks_render.append(put_button('主城部队', onclick= functools.partial(self.render_memu_bar, updata = v)))
        put_collapse('队伍', tasks_render)

    @use_scope('content', clear=True)
    def render_memu_bar(self, updata):
          with use_scope('menu_bar', clear=True):
            OptionPage([updata, {
                        state: updata['state'],
                        next_run_time: updata['next_run_time'],
                        team: updata['team'],
                        standby_max: updata['standby_max'],
                        outset: updata['outset'],
                        recruit_person:updata['recruit_person'],
                        going: updata['going'],
                        mopping_up: updata['mopping_up'],
                        x: updata['x'],
                        y: updata['y'],
                        await_time: updata['await_time'],
                        residue_troops_person: updata['residue_troops_person'],
                        residue_troops_enemy: updata['residue_troops_enemy']
                    }]).dispatch()
            
          with use_scope('img_show', clear=True):
              put_text('战报记录')
              if len(updata['battle_info']) > 0:
                  updata['battle_info'].reverse()
                  for v in updata['battle_info']:
                    put_image(v)

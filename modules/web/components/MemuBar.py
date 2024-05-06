import functools
from pywebio.output import use_scope, put_collapse,put_button, put_text, put_image

from modules.web.components.Option import *
from modules.web.components.prop_all import *


class MemuBar:
    def __init__(self):
        pass
    @use_scope('navigation_bar', clear=True)
    def render_func_bar(self):
        self.clear_area()
        put_collapse('队伍', [put_button(f'主城部队{i}', onclick=functools.partial(self.render_memu_bar, keys=f'troop{i}')) for i in range(1, 6)])
        put_collapse('同盟', [put_button('武勋统计', onclick=functools.partial(self.render_feat, keys='feat'))])

    @use_scope('content', clear=True)
    def render_memu_bar(self, keys):
          with use_scope('menu_bar', clear=True):
            current_data = self.conf_data.get_key_data(keys)
            OptionPage(current_data).dispatch()
            
          with use_scope('img_show', clear=True):
              put_text('战报记录')
              if len(current_data['battle_info']) > 0:
                  current_data['battle_info'].reverse()
                  for v in current_data['battle_info']:
                    put_image(v)
    @use_scope('content', clear=True)
    def render_feat(self, keys):
        with use_scope('feat', clear=True):
            current_data = self.conf_data.get_key_data(keys)
            feat = propall['feat']
            Option(feat.display_name, Component(feat.name, current_data[feat.name],
                                                feat.option_type, functools.partial(
                                                    feat.on_change_event,
                                                        origin=current_data,
                                                        keyss=feat.name
                                                        ))
                ).options
            feat_sum = propall['feat_sum']
            Option(feat_sum.display_name, Component(feat_sum.name, current_data[feat_sum.name],
                                                feat_sum.option_type, functools.partial(
                                                    feat_sum.on_change_event,
                                                        origin=current_data,
                                                        keyss=feat_sum.name
                                                        )))
            feat_type = propall['feat_type']
            Option(feat_type.display_name, Component(feat_type.name, current_data[feat_type.name],
                                                feat_type.option_type,
                                                  functools.partial(
                                                    feat_type.on_change_event,
                                                        origin=current_data,
                                                        keyss=feat_type.name
                                                        ),
                                                         args=feat_type.options
                                                        ))

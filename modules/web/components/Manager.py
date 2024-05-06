import functools
from pywebio.output import use_scope, put_button

from modules.web.components.Option import *
from modules.web.components.prop_all import *


class Manager:
  def __init__(self):
    pass

  @use_scope('navigation_bar', clear=True)
  def manager(self):
      self.clear_area()
      put_button('模拟器配置', onclick=functools.partial(self.render_manager_simulator, keys=['simulator', 'screen_await']))

  @use_scope('content', clear=True)
  def render_manager_simulator(self, keys):
      with use_scope('menu_bar', clear=True):
          for v in keys:
            data = self.conf_data.get_key_data(v)
            if v == 'simulator':
                prop_component = propall['simulator']
                Option(prop_component.display_name, Component(prop_component.name, data['value'],
                                                    prop_component.option_type,
                                                      functools.partial(
                                                        prop_component.on_change_event,
                                                            origin=data,
                                                            keyss='value'
                                                            ))
                    ).options
            elif v == 'screen_await':
                  prop_component = propall['screen_await']
                  Option(prop_component.display_name, Component(prop_component.name, data['value'],
                                                      prop_component.option_type,args=prop_component.options,
                                                        event=functools.partial(
                                                          prop_component.on_change_event,
                                                              origin=data,
                                                              keyss='value'
                                                              ))
                      ).options

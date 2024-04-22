import functools
from pywebio.output import use_scope, put_button

from modules.web.components.Option import *
from modules.web.components.prop_all import *


class NavigationBar:
  def __init__(self):
    pass

  @use_scope('navigation_bar', clear=True)
  def manager(self):
      self.clear_area()
      put_button('模拟器配置', onclick=self.render_manager_simulator)

  @use_scope('content', clear=True)
  def render_manager_simulator(self):
      with use_scope('menu_bar', clear=True):
          key = propall['simulator']
          Option(key.display_name, Component(key.name, self.data[key.name],
                                              key.option_type, functools.partial(
                                                  key.on_change_event,
                                                      origin=self.data,
                                                      origin_controller={key:self.data[key.name]}
                                                      ))
              ).options
          screen_await = propall['screen_await']
          Option(screen_await.display_name, Component(screen_await.name, self.data[screen_await.name],
                                              screen_await.option_type,args=screen_await.options,
                                                event=functools.partial(
                                                  screen_await.on_change_event,
                                                      origin=self.data,
                                                      origin_controller={screen_await:self.data[screen_await.name]}
                                                      ))
              ).options
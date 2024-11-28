from pywebio.output import use_scope, put_tabs
from .sweep_item import SweepItem

class SweepArea:
  def __init__(self, prop_objs):
    self.prop_objs = prop_objs
  
  @use_scope('function_area', clear=True)
  def render(self):
    put_tabs([
      {'title': '队伍1','content': SweepItem(self.prop_objs[0]).render()},
      {'title': '队伍2','content': SweepItem(self.prop_objs[1]).render()},
      {'title': '队伍3','content': SweepItem(self.prop_objs[2]).render()},
      {'title': '队伍4','content': SweepItem(self.prop_objs[3]).render()},
      {'title': '队伍5','content': SweepItem(self.prop_objs[4]).render()}
    ]).style('width:500px;')

from pywebio.output import use_scope,put_collapse,put_text

from .sweep import SweepArea, SweepProp

sweep_props = [SweepProp('1'),SweepProp('2'),SweepProp('3'),SweepProp('4'),SweepProp('5')]
sweeps = SweepArea(sweep_props)

class Private:
  def __init__(self):
    pass
  
  @use_scope('private', clear=True)
  def render(self):
    put_collapse('势力', [
      put_text('扫荡').onclick(sweeps.render),
      put_text('出征'),
      put_text('征兵')  
    ])


from .sweep_area import SweepArea
from pywebio.output import use_scope,put_collapse,put_text

from ...props.main import sweep_props

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


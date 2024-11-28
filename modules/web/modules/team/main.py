from pywebio.output import put_collapse,use_scope,put_text

class Team:
  def __init__(self):
    pass

  @use_scope('team', clear=True)
  def render(self):
    put_collapse('同盟',[
      put_text('打城主力'),
      put_text('打城拆迁'),
      put_text('武勋'),
      put_text('敌军主力'),
      put_text('战场翻地/拆除'),
      put_text('我方出战/防守')
    ])

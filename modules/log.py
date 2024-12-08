f = None
def set_handle(fn):
  global f
  f = fn

def info(v):
   v = 'info: v' + v
   f(v)

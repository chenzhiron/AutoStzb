f = None
def set_handle(fn):
  global f
  f = fn

def info(v):
   f(v)

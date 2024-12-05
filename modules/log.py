# from threading import Thread


# class ForMatLog:
#   _slog = None

#   def __init__(self) -> None:
#     pass

#   def update_instance(self, instalce):
#     pass

#   def thread_log_queue_handler(self) -> None:
#     pass


#   def add_handle(self, handle):
#     self.log_handle = handle      

#   def info(self, v):
#     print('info:', v)

# slogging = ForMatLog()


f = None
def set_handle(fn):
  global f
  f = fn

def info(v):
   v = 'info: v' + v
   f(v)

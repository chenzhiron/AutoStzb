from modules.manager.main import conf
from modules.utils.utils import wait_until
class OperatorInit:
   def __init__(self, device, task_key) -> None:
      self.device = device
      self.task_key = conf.get_key_data(task_key)

class OperatorTroops(OperatorInit):
  def __init__(self, device, task_key) -> None:
      super().__init__(device, task_key)
  # 校验任务
  def verify_task(self):
      if wait_until(self.task_conf['next_run_time']):
         return False
      if self.task_conf['steps'] == 1:
         pass
      elif self.task_conf['steps'] == 2:
         pass
      elif self.task_conf['steps'] == 3:
         pass
      elif self.task_conf['steps'] == 4:
         pass
      if self.task_conf['going']:
      #   return ChuZheng
        pass
      if self.task_conf['mopping_up']:
         pass


  # 校验征兵时间
  def pre_check(self):
     pass
  
  def run(self):
    if self.pre_check():
       return 
    while self.verify_task():
       pass
    return

class OperatorFeat(OperatorInit):
   def __init__(self, device, task_key):
      super().__init__(device, task_key)
   def run():
      pass   

import json
import pprint
import time

from loguru import logger

from modules.db.dbinit import Db


class TaskScheduler:
    def __init__(self):
        self.db = Db("task.db")
        self._cache = {
            "last_check": 0,
            "valid_tasks": []
        }
    
    def get_next_task(self, latest=False):
        """优化查询策略"""
        if not latest:
            if time.time() - self._cache["last_check"] < 5:
                return self._cache["valid_tasks"].pop(0) if self._cache["valid_tasks"] else None

        fresh_data = self.db.select_task_execute()
        current_ts = time.time()
        simulator, tasks = "", []
        logger.info(pprint.pformat(fresh_data))
        for key, value in fresh_data.items():
            if key == "simulator":
                simulator = value['address']
                continue

            if value.get("state"):
                time_tuple = time.strptime(value["nexttime"], "%Y/%m/%d %H:%M:%S")
                if current_ts > time.mktime(time_tuple):
                    tasks.append((key, value) )

        if simulator and tasks:
            self._cache = {
                "last_check": time.time(),
                "valid_tasks": [(simulator, task[0], task[1]) for task in tasks]
            }
            return self._cache["valid_tasks"].pop(0)
        return None


from contextlib import contextmanager
from modules.devices.main import DeviceManager, DeviceOperator

class TaskFactory:
    # import 
    _task_map = {
    }

    @classmethod
    def create_task(cls, task_name, operator, config):
        logger.info(f'task_name: {task_name}')
        task_class = cls._task_map.get(task_name)
        if not task_class:
            raise ValueError(f"Invalid task name: {task_name} and config: {pprint.pformat(config)}")
        logger.info(f"Creating task: {task_name}")
        return task_class(operator, config)


class St:
    def __init__(self):
        self.scheduler = TaskScheduler()
    
    @contextmanager
    def _device_context(self, simulator_name):
        """带资源管理的设备上下文"""
        dm = DeviceManager(simulator_name)
        try:
            yield DeviceOperator(dm)
        finally:
            dm.release()
    
    def run_task(self, simulator_name, task_name, config):
        with self._device_context(simulator_name) as operator:
            task = TaskFactory.create_task(task_name, operator, config)
            logger.info(f"Starting {task_name} on {simulator_name}")
            task.execute()
            logger.success(f"Completed {task_name}")
    
    def loop(self):
        while True:
            task_data = self.scheduler.get_next_task()
            logger.info(f'{pprint.pprint(task_data)}')
            if task_data:
                self.run_task(*task_data)
            time.sleep(1)  # 降低CPU占用
            logger.info('12345')

if __name__ == "__main__":
    system = St()
    system.loop()

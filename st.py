import time
from functools import wraps
from pprint import pprint

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
        # if not latest:
        #     if time.time() - self._cache["last_check"] < 5:
        #         return self._cache["valid_tasks"].pop(0) if self._cache["valid_tasks"] else None

        fresh_data = self.db.select_task_execute()
        current_ts = time.time()
        simulator, tasks = "", []
        for key, value in fresh_data.items():
            if key == "simulator":
                simulator = value['device_address']
                continue

            if value.get("state"):
                time_tuple = time.strptime(value["nexttime"], "%Y/%m/%d %H:%M:%S")
                if current_ts > time.mktime(time_tuple):
                    tasks.append((key, value))

        if simulator and tasks:
            self._cache = {
                "last_check": time.time(),
                "valid_tasks": [(simulator, task[0], task[1]) for task in tasks]
            }
            return self._cache["valid_tasks"].pop(0)
        return None

    def set_new_config(self, key, config):
        self.db.update(key, config)


from modules.devices.main import DeviceManager, DeviceOperator


class St:
    def __init__(self):
        self.scheduler = TaskScheduler()
        self._device_cache = {}

    def get_device(self, simulator_name):
        if simulator_name not in self._device_cache:
            self._device_cache[simulator_name] = DeviceOperator(DeviceManager(simulator_name))
        return self._device_cache[simulator_name]

    def _execute_practice_task(self, task_name, device, config):
        from modules.taskfn.practice_land import PracticeLand
        result = PracticeLand(device, config).run()
        pprint(result)
        config.update(result)
        self.scheduler.set_new_config(task_name, config)
        return result

    def _execute_attack_task(self, task_name, device, config):
        from modules.taskfn.attack_land import AttackLand
        result = AttackLand(device, config).run()
        pprint(result)
        config.update(result)
        self.scheduler.set_new_config(task_name, config)
        return result

    def practice_task(func):
        """装饰器处理Capture类任务的公共逻辑"""

        @wraps(func)
        def wrapper(self, task_name, device, config):
            task_name = func.__name__
            logger.info(f"Starting {task_name}")
            try:
                result = self._execute_practice_task(config, task_name)
                logger.success(f"Completed {task_name}; {config}")
                return result
            except Exception as e:
                logger.error(f"Error in {task_name}: {str(e)}")
                raise

        return wrapper

    def attack_task(func):
        """装饰器处理Attack类任务的公共逻辑"""

        @wraps(func)
        def wrapper(self, device, config):
            task_name = func.__name__
            logger.info(f"Starting {task_name}")
            try:
                result = self._execute_attack_task(task_name, device, config)
                logger.success(f"Completed {task_name}; {config}")
                return result
            except Exception as e:
                logger.error(f"Error in {task_name}: {str(e)}")
                raise

        return wrapper

    @practice_task
    def practice_land(self, device, config):
        pass

    @practice_task
    def practice_land_1(self, device, config):
        pass

    @practice_task
    def practice_land_2(self, device, config):
        pass

    @practice_task
    def practice_land_3(self, device, config):
        pass

    @practice_task
    def practice_land_4(self, device, config):
        pass

    @attack_task
    def attack_land(self, device, config):
        pass

    @attack_task
    def attack_land_1(self, device, config):
        pass

    @attack_task
    def attack_land_2(self, device, config):
        pass

    @attack_task
    def attack_land_3(self, device, config):
        pass

    @attack_task
    def attack_land_4(self, device, config):
        pass

    def martial_arts(self, device, config):
        from modules.taskfn.MartialArts import MartialArts
        result = MartialArts(device,config).run()
        config.update(result)
        self.scheduler.set_new_config('MartialArts', config)


    def run_task(self, simulator_name, task_name, config):
        """执行指定任务"""
        try:
            device = self.get_device(simulator_name)
            if hasattr(self, task_name):
                method = getattr(self, task_name)
                return method(device, config)
            else:
                logger.error(f"Method {task_name} not found")
                raise AttributeError(f"Method {task_name} not found")
        except Exception as e:
            logger.error(f"Error running task {task_name}: {str(e)}")
            raise

    def loop(self):
        while True:
            task_data = self.scheduler.get_next_task()
            if task_data:
                self.run_task(*task_data)
            time.sleep(1)
            # logger.info('12345')


if __name__ == "__main__":
    st = St()
    st.loop()

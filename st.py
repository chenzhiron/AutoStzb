import time
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

    def practice_land(self, device, config):
        from modules.taskfn.capture import Capture
        result = Capture(device, config).run()
        pprint(result)
        config.update(result)
        self.scheduler.set_new_config('practice_land', config)

    def run_task(self, simulator_name, task_name, config):
        device = DeviceOperator(DeviceManager(simulator_name))
        logger.info(f"Starting {task_name} on {simulator_name}")
        if hasattr(self, task_name):
            method = getattr(self, task_name)
            method(device, config)
            logger.success(f"Completed {task_name}; {config}")
        else:
            print(f"Method {task_name} not found in St class.")


    def loop(self):
        while True:
            task_data = self.scheduler.get_next_task()
            if task_data:
                self.run_task(*task_data)
            time.sleep(1)
            # logger.info('12345')


if __name__ == "__main__":
    system = St()
    system.loop()

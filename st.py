import time
import json
from modules.db.dbinit import Db
from modules.db.logdb import LogDb

import time


class St:
    def __init__(self):
        self.db = Db("task.db")
        self.log = LogDb("log.db")
        self.log.init_conn()

    def get_next_task(self):
        while True:
            rows = self.db.select_task_execute()
            current_timestamp = time.time()
            simulatorName = ""
            taskName = ""
            
            for v in rows:
                if v[0] == "simulator":
                    simulatorName = v[1]
                    continue

                config = json.loads(v[1])
                if config["state"]:
                    format_str = "%Y/%m/%d %H:%M:%S"
                    time_tuple = time.strptime(config["nexttime"], format_str)
                    timestamp = time.mktime(time_tuple)
                    if current_timestamp > timestamp:
                        taskName = v[0]
                        break
            if len(simulatorName) > 0 and len(taskName) > 0:
                return (simulatorName, taskName, config)
            time.sleep(1)

    def devices(self, simulatorname):
        from modules.devices.main import Devices

        # d = Devices(simulatorname).d
        d = None
        return d

    def myfight(self, d, config):
        from modules.taskfn.myfight import Myfight

        Myfight(self, d, config).execute()

    def exploit(self, d, config):
        from modules.taskfn.exploit import Exploit

        Exploit(d, config).execute()

    def fliplists(self, d, config):
        from modules.taskfn.flip_lists import FlipLists

        FlipLists(d, config).execute()

    def ranking(self, d, config):
        from modules.taskfn.ranking import Ranking

        Ranking(d, config).execute()

    def rolelists(self, d, config):
        from modules.taskfn.role_lists import role_lists

        pass

    def siegebattles(self, d, config):
        from modules.taskfn.siege_battles import SiegeBattles

        SiegeBattles(d, config).execute()

    def loop(self):
        while True:
            simulatorName, taskname, config = self.get_next_task()
            print(simulatorName, taskname, config)
            if hasattr(self, taskname):
                d = self.devices(simulatorName)
                method = getattr(self, taskname)
                method(d, config)
            else:
                print(f"Method {taskname} not found in St class.")
            time.sleep(1)


if __name__ == "__main__":
    s = St()
    s.loop()

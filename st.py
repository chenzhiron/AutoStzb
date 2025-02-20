import time
from db import Db
from logdb import LogDb
class St:
    def __init__(self):
        self.db = Db("task.db")
        self.log = LogDb("log.db")
        self.log.init_conn()
        
    def get_next_task(self):
        return self.db.select()

    def devices(self, config):
        from modules.devices.main import Devices

        d = Devices(config).d
        return d

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
            r = self.get_next_task()
            if r is None:
                continue
            # self.log.write('1234', 0)
            time.sleep(1)

from st import St
class Myfight:
    def __init__(self, s: St, d):
        self.origin = s
        self.d = d
        self.config = None
        print(type(self.config))

    def execute(self):
        self.config.update({"state": False, "nexttime": "2025/02/25 00:00:00"})
        self.origin.db.update("myfight", self.config)
        v2 = self.origin.db.select_task_execute()
        for r in v2:
            print('2:',r)

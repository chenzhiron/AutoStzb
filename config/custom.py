class CustomConfig:
    def __init__(self, time_sleep):
        self.time_sleep = time_sleep

    def changeTimesleep(self, time_sleep):
        try:
            if float(time_sleep) <= 0:
                v = 1
            self.time_sleep = float(time_sleep)
        except:
            self.time_sleep = float(time_sleep)
        from device.Class.AutoMation import change_automation_timeSleep
        change_automation_timeSleep(self.time_sleep)

    def getTimesleep(self):
        return self.time_sleep


customConfig = CustomConfig(1.0)

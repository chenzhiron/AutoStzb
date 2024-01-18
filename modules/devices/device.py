from modules.devices.Class.AutoMationClass import Automation
from modules.devices.pyminitouch.actions import MNTDevice


class Devices(Automation, MNTDevice):

    def __init__(self, config):
        adb = config['Adb']['executable']
        automation_serial = config['Simulator']['url']
        automation_port = config['Simulator']['screenshot_tcp_port']
        device_id = config['Simulator']['url']
        operate_change_port = config['Simulator']['touch_port']
        sleep = config['Simulator']['screenshot_sleep']
        Automation.__init__(self, adb, automation_serial, automation_port, sleep)
        MNTDevice.__init__(self, device_id, adb, operate_change_port)

    def startDevices(self):
        super().run_adb(["connect", self.device_serial])
        super().run_automate_in_thread()
        super().start()

    def closeDevice(self):
        super().stop()
        super().disconnect()

    def getScreenshots(self):
        return super().getScreenshots()

    def operateTap(self, x, y):
        self.tap([(x, y)])
        return True

    def operateSwipe(self, x1, y1, x2, y2):
        self.ext_smooth_swipe([(x1, y1), (x2, y2)],
                              duration=1000,
                              pressure=50
                              )

# if __name__ == '__main__':
#     test = Devices(globalConfig)
#     print(test.close)

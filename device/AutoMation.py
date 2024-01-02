from config.paths import adb
from config.const import automation_serial, automation_port, screenshot_url

from device.Class.AutoMationClass import Automation

automation = Automation(adb, automation_serial, automation_port, screenshot_url, 1)


def change_automation_timeSleep(v):
    automation.changeTimeSleep(v)

from config.custom import customConfig

from config.paths import adb
from config.const import automation_serial, automation_port, screenshot_url

from device.Class.AutoMationClass import Automation

automation = Automation(adb, automation_serial, automation_port, screenshot_url, customConfig.getTimesleep())


def change_automation_timeSleep(v):
    automation.changeTimeSleep('sleep', v)

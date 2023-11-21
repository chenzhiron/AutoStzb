from config.custom import customConfig

from config.paths import adb
from config.const import automation_serial, automation_port, screenshot_url

from device.Class.AutoMationClass import Automation

automation = None


def init(adb=adb, automation_serial=automation_serial,
         automation_port=automation_port, screenshot_url=screenshot_url, time_sleep=customConfig.getTimesleep()):
    global automation
    automation = Automation(adb, automation_serial, automation_port, screenshot_url, time_sleep)


init()


def change_automation_timeSleep(v):
    automation.changeTimeSleep('sleep', v)

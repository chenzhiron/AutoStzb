from apscheduler.triggers.cron import CronTrigger
import json
from config.paths import tasks

tasks_result = json.load(open(tasks))

trigger = CronTrigger(day_of_week='mon-sun')

import asyncio
import logging
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_SCHEDULER_STARTED
from apscheduler.schedulers.background import BlockingScheduler

# 创建调度器
scheduler = BlockingScheduler()
scheduler.configure(misfire_grace_time=60 * 60, max_instances=1)

scheduler_status = {
    "status": True
}


def set_scheduler_status(event):
    scheduler_status['status'] = False


def get_scheduler_status():
    return scheduler_status['status']


async def set_scheduler_state(event):
    from communication.comsumer import return_client_websocket, get_task
    client_websocket = return_client_websocket()
    logging.error('event:::::::::' + str(event) + '\n\r')
    await client_websocket.send(get_task)


def change_scheduler_state(event):
    scheduler_status['status'] = True
    asyncio.run(set_scheduler_state(event))


def start_scheduler():
    # 启动调度器
    scheduler.start()
    return scheduler


def return_scheduler():
    return scheduler


def scheduler_add_listener():
    from dispatcher.general import battle_dispose_result, zhengbing_dispose_result
    scheduler.add_listener(set_scheduler_status, EVENT_SCHEDULER_STARTED)
    scheduler.add_listener(change_scheduler_state, EVENT_JOB_EXECUTED)
    scheduler.add_listener(battle_dispose_result, EVENT_JOB_EXECUTED)
    scheduler.add_listener(zhengbing_dispose_result, EVENT_JOB_EXECUTED)


scheduler_add_listener()

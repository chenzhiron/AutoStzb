import asyncio
import json
import logging
import subprocess
import threading
import time

import websockets


# 配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='UTF-16')
from device.main_device import connect_device
from tasks.task_queue import return_task_queue

d = connect_device()


async def handle_connection(websocket):
    try:
        logging.info('success')
        while True:
            message = await websocket.recv()
            message = json.loads(message)
            if message:
                queue = return_task_queue()
                queue.put(message)
            # 发送心跳消息
            await websocket.send('1')
            time.sleep(5)
    except websockets.exceptions.ConnectionClosedOK:
        print('WebSocket connection closed')
        subprocess.kill()
        # await asyncio.sleep(5)
        # await run_websocket()


def run_websocket():
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    # 创建WebSocket服务器
    start_server = websockets.serve(handle_connection, 'localhost', 22333)
    # 运行WebSocket服务器
    new_loop.run_until_complete(start_server)
    try:
        new_loop.run_forever()
    finally:
        new_loop.close()


def start_run_websocket_thread():
    websocket_thread = threading.Thread(target=run_websocket)
    websocket_thread.start()
    # run_websocket()
    # start_queue_thread()

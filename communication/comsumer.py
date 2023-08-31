import asyncio
import json
import logging
import threading
import websockets
from pip._internal.utils import subprocess

# 配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='UTF-16')
from device.main_device import connect_device
from tasks.task_queue import return_task_queue

d = connect_device()


async def handle_connection(websocket, path):
    try:
        queue = return_task_queue()
        while True:
            message = await websocket.recv()
            message = json.loads(message)
            logging.info(':%s', message)
            if message:
                queue.put(message)
                logging.info(queue.qsize())

            # 发送心跳消息
            await websocket.send('1')
            await asyncio.sleep(5)  # 5秒发送一次心跳消息
    except websockets.exceptions.ConnectionClosedOK:
        print('WebSocket connection closed')
        subprocess.kill()
        # await asyncio.sleep(5)
        # await run_websocket()


def run_websocket():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # 创建WebSocket服务器
    start_server = websockets.serve(handle_connection, 'localhost', 22333)

    # 运行WebSocket服务器
    loop.run_until_complete(start_server)
    loop.run_forever()


def start_run_websocket_thread():
    websocket_thread = threading.Thread(target=run_websocket)
    websocket_thread.start()

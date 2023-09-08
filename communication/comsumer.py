import time

import asyncio
import json
import subprocess
import threading
import websockets
import logging
from communication.dispose_task import dispose_task


logging.getLogger().setLevel(logging.ERROR)
# 配置日志记录器
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(message)s')
from device.main_device import connect_device

connect_device()

get_task = 'get_task'
start_task = 'start_task'

client_websocket = 0


def return_client_websocket():
    return client_websocket


async def handle_connection(websocket):
    global client_websocket
    client_websocket = websocket
    try:
        logging.error('success')
        await websocket.send(get_task)
        while True:
            message = await websocket.recv()
            message = json.loads(message)
            await dispose_task(websocket, message)
            # 发送心跳消息
            await websocket.send('1')
            time.sleep(5)
    except websockets.exceptions.ConnectionClosedOK:
        print('WebSocket connection closed')
        subprocess.kill()


def run_websocket():
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    # 创建WebSocket服务器
    start_server = websockets.serve(handle_connection, 'localhost', 22333)
    # 运行WebSocket服务器
    new_loop.run_until_complete(start_server)
    logging.info('初始化websocket')
    try:
        new_loop.run_forever()
    finally:
        new_loop.close()


def start_run_websocket_thread():
    websocket_thread = threading.Thread(target=run_websocket)
    websocket_thread.start()

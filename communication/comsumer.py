import asyncio
import websockets
import logging
import json
# 配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='UTF-16')
from device.main_device import connect_device
from tasks.main import execute_tasks

d = connect_device()


async def handle_connection(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            message = json.loads(message)
            logging.info(':%s', message)
            if type(message) is dict:
                if message['zhengbing'] is not None:
                    execute_tasks(message)
            # 发送心跳消息
            await websocket.send('1')
            await asyncio.sleep(5)  # 5秒发送一次心跳消息
    except websockets.exceptions.ConnectionClosedOK:
        print('WebSocket connection closed')


def run_websocket():
    # 创建WebSocket服务器
    start_server = websockets.serve(handle_connection, 'localhost', 22333)

    # 运行WebSocket服务器
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

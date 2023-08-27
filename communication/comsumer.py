import asyncio
import websockets
import logging

# 配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='UTF-16')
from tasks.saodang import saodang
from device.main_device import connect_device
from tasks.zhengbing import zhengbing

d = connect_device()


async def handle_connection(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            task = message.split(',')
            logging.info(':%s', task)
            if len(task) == 4 and int(task[0]) == 1:
                zhengbing(task[1])
            elif len(task) == 4 and int(task[0]) == 2:
                saodang(task[1])
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

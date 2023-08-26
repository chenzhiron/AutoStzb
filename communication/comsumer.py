import asyncio
import websockets
import logging

#
# 配置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


async def handle_connection(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            logging.info('Received message from client:', message)

            # 发送心跳消息
            await websocket.send('1')
            await asyncio.sleep(5)  # 5秒发送一次心跳消息
    except websockets.exceptions.ConnectionClosedOK:
        print('WebSocket connection closed')


# 创建WebSocket服务器
start_server = websockets.serve(handle_connection, 'localhost', 33333)

# 运行WebSocket服务器
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

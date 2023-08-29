import {PORT} from "./property";

let socket = null

async function run_server() {
    socket = await new WebSocket('ws://localhost:' + PORT);
    // 创建WebSocket连接
    // 当连接建立时

    await socket.addEventListener('open', function (event) {
        // 发送消息给服务器
        socket.send('connect success');
    });

    // 当接收到来自服务器的消息时
    await socket.addEventListener('message', function (event) {
        // 处理接收到的消息
        console.log('脚本执行信息', event.data);
    });
    await socket.addEventListener('close', function (event) {
        console.log('脚本关闭')
    })

    return socket
}

export default run_server

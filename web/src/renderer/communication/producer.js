// import {PORT} from "./property";
// import {createServer} from "http";
// import {Server} from "socket.io";
//
// const httpServer = createServer();
// const io = new Server(httpServer, {
//     cors: {
//         origin: '*'
//     }
// });
//
//
// // 当有新的Socket.IO连接建立时
// let py_client = null
// io.on('connection', function (socket) {
//     console.log('New Socket.IO connection');
//     console.log(socket.id)
//     socket.emit('tasks', 'hello,client', (response) => {
//         console.log(response)
//     })
//     // py_client = socket
// })
//
// function run_server() {
//     httpServer.listen(PORT);
//     return io
// }
//
// export default run_server
let socket = null
function run_server() {
    socket = new WebSocket('ws://localhost:33333');
    // 创建WebSocket连接
    // 当连接建立时
    socket.addEventListener('open', function (event) {
        // 发送消息给服务器
        socket.send('Hello from JavaScript!');
                // 定时发送消息给服务端
          setInterval(function() {
            socket.send(0);
          }, 5000); // 每5秒发送一次消息
    });

// 当接收到来自服务器的消息时
    socket.addEventListener('message', function (event) {
        // 处理接收到的消息
        console.log('Received message from server:', event.data);
    });
    socket.addEventListener('close', function (event){
        console.log('111111111', 'end')
    })

    return socket
}

export default run_server

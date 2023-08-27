<template>
  <div class="wrapper">
    <div>
      <button @click="start_python">启动</button>
      <button @click="send_task">发送任务</button>
      <div>{{ current_path }}</div>
      <div>
        <div>目前仅支持选项1</div>
        任务
        <select v-model="options[0]">
          <option v-for="(v,k) in tasks_number" :key="k">{{ v }}</option>
        </select>
        <span>Selected: {{ options[0] }}</span>
      </div>
      <div>
        编队
        <select v-model="options[1]">
          <option v-for="(v,k) in tasks_number" :key="k">{{ v }}</option>
        </select>
      </div>
    </div>
    <div>
      <h4 class="top">日志</h4>
      <div class="log">
        <div v-for="(v,k) in log" :key="k" class="item">
          {{ v }}
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import {spawn} from "child_process"
import path from 'path'
import run_server from "../communication/producer";

export default {
  name: 'landing-page',
  data() {
    return {
      pythonSourcePath: "main.py",
      pythonExcutePath: "",
      pythonCwdPath: "",
      log: [],
      current_path: '',
      pathSeparator: path.sep,
      options: [0, 0, 0, 0],
      tasks_number: [1, 2, 3, 4, 5],
      troop_number: [1, 2, 3, 4, 5],
      producer: null,
      time: 0
    }
  },
  methods: {
    send_task() {
      console.log(this.producer)
      this.producer.send(this.options)
    },
    async start_socket_server() {
      this.producer = await run_server()
    },
    start_python: function () {
      const pythonProcess = spawn(
          this.pythonExcutePath,
          [
            this.pythonSourcePath,
          ], {
            cwd: this.pythonCwdPath
          })
      // 监听Python进程的stdout流
      pythonProcess.stdout.on('data', data => {
        console.log('data', data.toString().trim())
        const logMessage = data.toString().trim();
        this.log.push(logMessage);
        // 在这里处理Python的日志输出，比如将其显示在Electron应用的界面上
      });

      // 监听Python进程的stderr流
      pythonProcess.stderr.on('data', data => {
        console.log('data', data.toString().trim())
        const errorMessage = data.toString().trim();
        this.log.push(errorMessage);
        // 在这里处理Python的错误日志输出
      });

      // 监听Python进程的退出事件
      pythonProcess.on('close', code => {
        console.log('Python process exited with code', code);
        // 在这里处理Python进程退出的逻辑
      });
      this.time = setInterval(() => {
        if ((!this.producer) || (!this.producer.url)) {
          this.start_socket_server();
          if (this.producer && !this.producer.url) {
            clearInterval(this.time);
          }
        } else {
          clearInterval(this.time);
        }
      }, 500);

    }
  },
  mounted() {
    const mapPath = path.resolve(__dirname)
    const pathArray = mapPath.split(this.pathSeparator)
    let max = 0
    for (let i = pathArray.length - 1; i >= 0; i--) {
      if (pathArray[i] === 'auto_stzb') {
        max = i
        break;
      }
    }
    this.pythonCwdPath = path.join(...pathArray.slice(0, max + 1))
    this.pythonExcutePath = path.join(this.pythonCwdPath, 'tookit', 'python.exe')
    this.start_python()
  }
}
</script>

<style scoped>
.wrapper {
  display: flex;
  justify-content: space-evenly;
}

.wrapper > div {
  flex: 1;
}

.log {
  height: 400px;
  overflow: auto;
}

.item {
  margin: 10px 0;
}
</style>

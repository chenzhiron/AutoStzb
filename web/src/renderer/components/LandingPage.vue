<template>
  <div class="wrapper">
    <div>
      <button @click="start_python">启动</button>
      <button @click="demo">demo</button>
      <button @click="start_socket_server">启动服务</button>
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
      producer: null
    }
  },
  methods: {
    demo() {
      console.log(this.producer)
      // console.log(this.producer)
      this.producer.send([0,1,2,3,4,5])
    },
    start_socket_server() {
      this.producer = run_server()
    },
    start_python: function () {
      const pythonProcess = spawn(
          this.pythonExcutePath,
          [
            this.pythonSourcePath,
            ...this.options
            // 1, //任务类型编号
            // 3, //任务操作的队伍，1-5
            // 2  //任务的次数 0代表无线次数
          ], {
            cwd: this.pythonCwdPath
          })
      // 监听Python进程的stdout流
      pythonProcess.stdout.on('data', data => {
        const logMessage = data.toString().trim();
        this.log.push(logMessage);
        // 在这里处理Python的日志输出，比如将其显示在Electron应用的界面上
      });

      // 监听Python进程的stderr流
      pythonProcess.stderr.on('data', data => {
        const errorMessage = data.toString().trim();
        this.log.push(errorMessage);
        // 在这里处理Python的错误日志输出
      });

      // 监听Python进程的退出事件
      pythonProcess.on('close', code => {
        console.log('Python process exited with code', code);
        // 在这里处理Python进程退出的逻辑
      });
    },
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

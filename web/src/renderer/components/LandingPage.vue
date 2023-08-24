<template>
  <div class="wrapper">
    <div>
      <button @click="start_python">启动</button>
      <button @click="demo()">demo_path</button>
      <div>{{current_path}}</div>
    </div>
    <div>
      <h4 class="top">日志</h4>
      <div class="log">
        <div v-for="(v,k) in log" :key="k" class="item">
          {{v}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { spawn } from "child_process"
export default {
  name: 'landing-page',
  data() {
    return {
      pythonSourcePath: "main.py",
      pythonExcutePath: "G:\\czr\\demo\\auto_stzb\\tookit\\python.exe",
      pythonCwdPath: 'G:\\czr\\demo\\auto_stzb',
      log: [],
      current_path: ''
    }
  },
  watch: {
    log: val => {
      if(val.length > 10){
        this.log.shift()
      }
    }
  },
  methods: {
    start_python: function () {
      const pythonProcess = spawn(
          this.pythonExcutePath,
          [
            this.pythonSourcePath,
              '0', //任务类型编号
              '1', //任务操作的队伍，1-5
              '2'  //任务的次数 0代表无线次数
          ], {
            cwd: this.pythonCwdPath
          })
      pythonProcess.stdout.on("data", data => {
        this.log.push(data)
      })

      // 监听 Python 进程的错误输出
      pythonProcess.stderr.on("data", data => {
        this.log.push(data)
      })
      // 监听 Python 进程的退出事件
      pythonProcess.on("close", code => {
        this.log.push(code)
      })
    },
    demo() {
     this.current_path = __dirname
    }
  },
}
</script>

<style scoped>
.wrapper {
  display: flex;
  justify-content: space-evenly;
}
.log {
  height: 400px;
  position: relative;
  top: 0;
  overflow: hidden;
}
.item {
  height: 40px;
  line-height: 40px;
}
</style>

<template>
  <div class="wrapper">
    <!-- <el-button @click="start_python">链接模拟器</el-button> -->
     <el-button @click="start_socket_server">创建通信</el-button>
    <div>
      <el-tabs
        tab-position="top"
        style="height: 200px"
        v-model="activeName"
        v-if="Object.keys(task_config).length > 0"
      >
        <el-tab-pane
          v-for="(v, k, index) in task_config"
          :key="index"
          :label="task_name[k].name"
          :name="task_name[k].value"
        >
          <el-row
            :gutter="20"
            v-for="(item, key, index) in v"
            :key="index"
          >
            <template v-if="key == 'status'">
              <el-col :span="6">
                <div class="grid-content bg-purple">任务</div>
              </el-col>
              <el-col :span="18">
                <div class="grid-content bg-purple">
                  <el-button @click="send_task">发送</el-button>
                </div>
              </el-col>
            </template>
            <template v-if="key == 'team'">
              <el-col :span="6">
                <div class="grid-content bg-purple">部队</div>
              </el-col>
              <el-col :span="18">
                <div class="grid-content bg-purple">
                  <el-select
                    v-model="task_config[k].team"
                    placeholder="请选择"
                  >
                    <el-option
                      v-for="item in options"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value"
                    >
                    </el-option>
                  </el-select>
                </div>
              </el-col>
            </template>
           <template v-if="key == 'number'">
              <el-col :span="6">
                <div class="grid-content bg-purple">次数</div>
              </el-col>
              <el-col :span="18">
                <div class="grid-content bg-purple">
                  <el-input-number
                    v-model="task_config[k].number"
                    controls-position="right"
                  ></el-input-number>
                </div>
              </el-col>
            </template>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="调度器">调度器</el-tab-pane>
      </el-tabs>
    </div>
    <div>
      <h4 class="top">日志</h4>
      <div class="log">
        <div
          v-for="(v, k) in log"
          :key="k"
          class="item"
        >
          <div v-html="v"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { spawn } from "child_process"
  import path from "path"
  import run_server from "../communication/producer"
  import read_task from "../config/task"

  export default {
    name: "landing-page",
    data() {
      return {
        pathSeparator: path.sep,
        pythonSourcePath: "main.py",
        pythonExcutePath: "",
        pythonCwdPath: "",
        current_path: "",
        log: [],

        activeName: "zhengbing",
        task_name: {
          zhengbing: {
            name: "征兵",
            value: "zhengbing",
          },
          saodang: {
            name: "扫荡",
            value: "saodang",
          },
        },
        task_config: {},

        producer: null,
        time: 0,

        troop_number: [1, 2, 3, 4, 5],

        options: [
          {
            value: "1",
            label: "主城队伍1",
          },
          {
            value: "2",
            label: "主城队伍2",
          },
          {
            value: "3",
            label: "主城队伍3",
          },
          {
            value: "4",
            label: "主城队伍4",
          },
          {
            value: "5",
            label: "主城队伍5",
          },
        ],
      }
    },
    methods: {
      send_task() {
        console.log(this.producer)
        const data = this.task_config[this.activeName]
        this.producer.send(
          JSON.stringify({
            [this.activeName]: data
          })
        )
      },
      async start_socket_server() {
        this.producer = await run_server()
      },
      start_python: function () {
        const pythonProcess = spawn(
          this.pythonExcutePath,
          [this.pythonSourcePath],
          {
            cwd: this.pythonCwdPath,
          }
        )
        // 监听Python进程的stdout流
        pythonProcess.stdout.on("data", data => {
          const logMessage = data.toString().trim()
          this.log.push(logMessage)
          // 在这里处理Python的日志输出，比如将其显示在Electron应用的界面上
        })

        // 监听Python进程的stderr流
        pythonProcess.stderr.on("data", data => {
          const errorMessage = data.toString().trim()
          this.log.push(errorMessage)
          // 在这里处理Python的错误日志输出
        })

        // 监听Python进程的退出事件
        pythonProcess.on("close", code => {
          console.log("进程退出", code)
          // 在这里处理Python进程退出的逻辑
        })
        // this.time = setInterval(() => {
        //   if (!this.producer || !this.producer.url) {
        //     this.start_socket_server()
        //     if (this.producer && !this.producer.url) {
        //       clearInterval(this.time)
        //     }
        //   } else {
        //     clearInterval(this.time)
        //   }
        // }, 5000)
      },
    },
    created() {
      const mapPath = path.resolve(__dirname)
      const pathArray = mapPath.split(this.pathSeparator)
      let max = 0
      for (let i = pathArray.length - 1; i >= 0; i--) {
        if (pathArray[i] === "auto_stzb") {
          max = i
          break
        }
      }
      this.pythonCwdPath = path.join(...pathArray.slice(0, max + 1))
      this.pythonExcutePath = path.join(
        this.pythonCwdPath,
        "toolkit",
        "python.exe"
      )
      const tasks_config = path.join(this.pythonCwdPath, "config", "tasks.json")
      this.task_config = read_task(tasks_config)
      this.start_python()
    },
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
  .top {
    text-align: center;
  }
  .log {
    height: 400px;
    overflow: auto;
  }

  .item {
    margin: 10px 0;
  }
</style>

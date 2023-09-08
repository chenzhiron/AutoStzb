<template>
  <div class="wrapper">
    <el-button @click="start_socket_server">创建通信</el-button>
    <div>
      <el-tabs tab-position="left" v-if="Object.keys(task_config).length > 0">
        <template v-if="Object.keys(task_config.module_zhengbing).length > 0">
          <template v-for="v in task_config.module_zhengbing">
            <el-tab-pane :label="v.id" :key="v.id">
              <div>
                启动
                <el-checkbox
                  v-model="v.status"
                  @change="(value) => change_task(value, v)"
                ></el-checkbox>
              </div>
              <div>
                次数 <el-input-number v-model="v.number"></el-input-number>
              </div>
              <div>
                无限执行 <el-checkbox v-model="v.infinite"></el-checkbox>
              </div>
            </el-tab-pane>
          </template>
        </template>
        <template v-if="Object.keys(task_config.module_saodang).length > 0">
          <template v-for="v in task_config.module_saodang">
            <el-tab-pane :label="v.id" :key="v.id">
              <div>
                启动
                <el-checkbox
                  v-model="v.status"
                  @change="(value) => change_task(value, v)"
                ></el-checkbox>
              </div>
              <div>
                次数 <el-input-number v-model="v.number"></el-input-number>
              </div>
              <div>
                平局是否等待
                <el-checkbox v-model="v.battle_result.await"></el-checkbox>
              </div>
              <div>平局时，如果我方兵力低于该值，则自动撤退</div>
              <div>
                平局我方兵力
                <el-input-number
                  v-model="v.battle_result.num"
                ></el-input-number>
              </div>
            </el-tab-pane>
          </template>
        </template>
      </el-tabs>
      <div>
        <el-tabs>
          <el-tab-pane label="调度器">
            {{ start_task_list }}
          </el-tab-pane>
        </el-tabs>
      </div>
    </div>
    <div>
      <h4 class="top">日志</h4>
      <div class="log" ref="scrollContainer">
          <div v-for="(v, k) in log" :key="k" class="item">
            <div v-html="v"></div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import { spawn } from "child_process";
import path from "path";
import run_server from "../communication/producer";
import read_task from "../config/task";

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

      start_task_list: [],

      task_config: {},

      producer: null,
    };
  },
  watch: {
    log: {
      handler: function (val, oldVal) {
        this.$nextTick(() => {
          const container = this.$refs.scrollContainer;
          container.scrollTop = container.scrollHeight;
        });
      },
    },
  },
  methods: {
    change_task(value, task_config) {
      if (value) {
        this.start_task_list.push(task_config);
      } else {
        let index = this.start_task_list.find((v) => v.id === task_config.id);
        if (index !== -1) {
          this.start_task_list.splice(index, 1);
        } else {
          this.$message.error("任务没有找到或者没有启动");
        }
      }
    },
    send_task(producer) {
      if (this.start_task_list.length === 0) {
        producer.send(JSON.stringify(0));
        return false;
      } else {
        producer.send(JSON.stringify(this.start_task_list.shift()));
        return true;
      }
    },
    async start_socket_server() {
      this.producer = await run_server();
      this.producer.addEventListener("message", (event) => {
        console.log(event.data);
        if (event.data === "get_task") {
          this.send_task(this.producer);
        }
      });
    },
    start_python: function () {
      const pythonProcess = spawn(
        this.pythonExcutePath,
        [this.pythonSourcePath],
        {
          cwd: this.pythonCwdPath,
        }
      );
      // 监听Python进程的stdout流
      pythonProcess.stdout.on("data", (data) => {
        const logMessage = data.toString().trim();
        this.log.push(logMessage);
      });

      // 监听Python进程的stderr流
      pythonProcess.stderr.on("data", (data) => {
        const errorMessage = data.toString().trim();
        this.log.push(errorMessage);
      });

      // 监听Python进程的退出事件
      pythonProcess.on("close", (code) => {
        console.log("进程退出", code);
      });
    },
  },
  created() {
    const mapPath = path.resolve(__dirname);
    const pathArray = mapPath.split(this.pathSeparator);
    let max = 0;
    for (let i = pathArray.length - 1; i >= 0; i--) {
      if (pathArray[i] === "auto_stzb") {
        max = i;
        break;
      }
    }
    this.pythonCwdPath = path.join(...pathArray.slice(0, max + 1));
    this.pythonExcutePath = path.join(
      this.pythonCwdPath,
      "toolkit",
      "python.exe"
    );
    const tasks_config = path.join(this.pythonCwdPath, "config", "tasks.json");
    this.task_config = read_task(tasks_config);
    console.log(this.task_config);
    this.start_python();
  },
};
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

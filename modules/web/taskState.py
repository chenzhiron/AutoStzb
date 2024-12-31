from datetime import datetime
import time
from pywebio.output import put_code, use_scope
from pywebio.session import register_thread
from threading import Thread
import json
import os
import time


class TaskReadManager:

    def __init__(self):
        # path ??
        self.file_path = "config.json" 
        self.last_mtime = None
        self.cache = None
        self.last_check = 0
        self.refresh_interval = 1
        self.taskConfig = {}
        self.init_json()

    def _load_json(self):
        """内部方法：从文件加载 JSON 数据"""
        with open(self.file_path, "r") as f:
            return json.load(f)

    def init_json(self):
        self.cache = self._load_json()
        self.last_mtime = os.path.getmtime(self.file_path)
        self.taskConfig = self.cache

    def get_json_data(self):
        """获取 JSON 数据，使用缓存"""
        current_time = time.time()

        # 控制检查频率
        if current_time - self.last_check < self.refresh_interval:
            return self.cache

        self.last_check = current_time
        mtime = os.path.getmtime(self.file_path)

        # 如果文件没有修改，则返回缓存
        if self.cache is not None and mtime == self.last_mtime:
            return self.cache

        # 文件被修改，重新加载
        self.last_mtime = mtime
        self.cache = self._load_json()
        self.taskConfig = self.cache
        return self.cache

    def update_json_data(self):
        """更新 JSON 数据并刷新文件"""
        self.last_mtime = time.time()  # 模拟文件修改时间更新
        with open(self.file_path, "w") as f:
            json.dump(self.taskConfig, f, indent=4)

    def get_next_task(self):
        pass


class TaskLoop(TaskReadManager):
    loopthread = None

    def __init__(self):
        super().__init__()
        self.padding = []
        # self.execute = []
        self.appinitialze()

    def updatecheckbox(self, obj, k, v):
        if len(v) == 0:
            result = False
        else:
            result = True

        obj[k] = result
        self.update_json_data()

    def update(self, obj, k, v):
        obj[k] = v
        print("k-v:", obj[k])
        self.update_json_data()

    def appinitialze(self):
        if TaskLoop.loopthread is None:
            TaskLoop.loopthread = Thread(None, target=self.eventloop)
            TaskLoop.loopthread.setDaemon(True)
            TaskLoop.loopthread.start()

    def eventloop(self):
        while 1:
            self.padding = []
            config = self.get_json_data()
            for k, v in config.items():
                statev = v.get("state", None)
                if statev is None or not statev:
                    continue
                if k in self.padding:
                    continue
                self.padding.append(k)

                self.padding.sort(
                    key=lambda x: datetime.strptime(
                        config[x]["nexttime"], "%Y/%m/%d %H:%M:%S"
                    )
                )
            with use_scope("log_area", clear=True):
                put_code(content=self.padding)
            time.sleep(1)


class basic(TaskLoop):

    def initialze(self):
        super().__init__()
        register_thread(self.loopthread)

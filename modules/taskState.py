import json
import os
import time


class taskState:

    def __init__(self):
        self.taskConfig = {}
        self.executing = []
        self.padding = []
        self.file_path = "./config/config.json"
        self.last_mtime = None
        self.cache = None
        self.last_check = 0
        self.refresh_interval = 1
        self.init_json()

    def _load_json(self):
        """内部方法：从文件加载 JSON 数据"""
        with open(self.file_path, "r") as f:
            return json.load(f)

    def init_json(self):
        self.cache = self._load_json()
        self.last_mtime = os.path.getmtime(self.file_path)
        self.taskConfig = self.cache

    def get_data(self):
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
        return self.cache

    def update_checkbox(self, obj, k, v):
        if len(v) == 0:
            result = False
        else:
            result = True

        obj[k] = result
        self.update_data()

    def update_input(self, obj, k, v):
        obj[k] = v
        self.update_data()

    def update_data(self):
        """更新 JSON 数据并刷新文件"""
        self.last_mtime = time.time()  # 模拟文件修改时间更新
        with open(self.file_path, "w") as f:
            json.dump(self.taskConfig, f, indent=4)

    def getTask(self):
        if len(self.padding) > 0:
            task = self.padding.pop(0)
            self.executing.append(task)
            return task
        else:
            return None

    def addTask(self, task):
        self.padding.append(task)

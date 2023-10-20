import json
from config.paths import tasks


def execute(tasks_config):
    for key, value in tasks_config.items():

        print(f"键: {key}")
        print(f"值: {value}")
        print("---")


if __name__ == '__main__':
    with open(tasks, 'r') as f:
        tasks_config = json.load(f)
        execute(tasks_config)

# 将配置读取，生成配置对象，生成ui, 当ui生成 并触发修改后，修改配置对象，并加入调度器
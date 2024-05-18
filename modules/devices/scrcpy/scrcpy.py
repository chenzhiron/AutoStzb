import subprocess
from modules.devices.adb import AdbRun
class Scrcpy(AdbRun):
    def __init__(self) -> None:
        super().__init__()

    def run(self):
          # 使用subprocess调用scrcpy命令，指定截图分辨率和文件名
        command = ["scrcpy", "--output-format", "jpeg", "--size", "1600:900", "--no-display", "--turn-screen-off", "--max-size", "100", "-"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)

        # 读取stdout中的二进制数据
        screenshot_data = process.stdout.read()

        # 将截图数据写入文件
        with open("screenshot.jpg", "wb") as f:
            f.write(screenshot_data)

        print("Screenshot captured successfully.")

import subprocess

class AdbRun:
  def __init__(self) -> None:
    # 添加adb路径
    pass
   
  def run_adb(self, args):
        process = subprocess.Popen([str(arg) for arg in args],  encoding='utf-8')
        stdout, stderr = process.communicate()
        return process.returncode, stdout, stderr

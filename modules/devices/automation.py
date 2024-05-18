import time
from modules.devices.adb import AdbRun

class DroidCast(AdbRun):
    def __init__(self) -> None:
        super().__init__()
        
    def droidCast_locate_apk_path(self):
        return_code, output, _ = self.run_adb(["shell", "pm", "path", "ink.mol.droidcast_raw"])
        if return_code or output == "":
            return_code2 = self.run_adb(['install', './toolkit/adb/DroidCast_raw-release-1.1.apk'])
        print(return_code2)
        time.sleep(1)
        return_code, output, _ = self.run_adb(["shell", "pm", "path", "ink.mol.droidcast_raw"])
        prefix = "package:"
        postfix = ".apk"
        begin_index = output.index(prefix, 0)
        end_index = output.rfind(postfix)
        return "CLASSPATH=" + output[begin_index + len(prefix):(end_index + len(postfix))].strip()
    
    def run(self):
            return_code, _, _ = self.run_adb(['connect', self.simulator])
            print(return_code, _, _)
            class_path = self.droidCast_locate_apk_path()

            return_code, _, _ = self.run_adb(["forward", "tcp:53516", "tcp:53516"])
            print(">>> adb forward tcp:53516", return_code)

            arguments = ["shell", class_path, "app_process", "/", "ink.mol.droidcast_raw.Main", "--port=53516"]
            self.run_adb(arguments)

import os
import subprocess
import time
import requests
from PIL import Image
from io import BytesIO


class Automation:
    def __init__(self, adb_path, device_serial, port, screenshot_url, time_sleep):
        self.adb_path = adb_path
        self.device_serial = device_serial
        self.port = port
        self.screenshot_url = screenshot_url
        self.time_sleep = time_sleep

    def changeTimeSleep(self, time_sleep):
        self.time_sleep = time_sleep

    def run_adb(self, cmd, return_output=False):
        adb_cmd = [self.adb_path]
        if self.device_serial:
            adb_cmd.extend(['-s', self.device_serial])
        adb_cmd.extend(cmd)

        proc = subprocess.Popen(adb_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        if return_output:
            return stdout.decode('utf-8').strip(), stderr.decode('utf-8').strip()
        else:
            return proc.returncode == 0

    def locate_apk_path(self):
        (rc, out, _) = self.run_adb(["shell", "pm", "path", "com.rayworks.droidcast"])
        if rc or out == "":
            current_dir = os.path.dirname(os.path.abspath(__file__))  # get the directory of current script
            apk_path = os.path.join(current_dir, 'DroidCast.apk')
            (install_rc, _, _) = self.run_adb(["install", apk_path])
            if install_rc:
                raise RuntimeError("Failed to install the apk, please check the apk file.")
            else:
                print("Apk installed successfully.")
                (rc, out, _) = self.run_adb(["shell", "pm", "path", "com.rayworks.droidcast"])
                if rc or out == "":
                    raise RuntimeError("Still cannot locate the apk after installation, please check the device.")
        prefix = "package:"
        postfix = ".apk"
        beg = out.index(prefix, 0)
        end = out.rfind(postfix)
        return "CLASSPATH=" + out[beg + len(prefix):(end + len(postfix))].strip()

    def identify_device(self):
        (rc, out, _) = self.run_adb(["devices"])
        if rc:
            raise RuntimeError("Fail to find devices")
        else:
            device_serial_no = self.device_serial
            devicesInfo = str(out)
            deviceCnt = devicesInfo.count('device') - 1

            if deviceCnt < 1:
                raise RuntimeError("Fail to find devices")

            if deviceCnt > 1 and (not device_serial_no):
                raise RuntimeError(
                    "Please specify the serial number of target device you want to use ('-s serial_number').")

    def automate(self):
        # Example of how to use run_adb with the updated device_serial handling
        self.identify_device()
        self.locate_apk_path()
        self.run_adb(['forward', f'tcp:{self.port}', f'tcp:{self.port}'])
        self.run_adb(
            ['shell', 'CLASSPATH=/data/local/tmp/scrcpy-server', 'app_process', '/', 'com.genymobile.scrcpy.Server'])

    def getScreenshots(self):
        time.sleep(self.time_sleep)
        response = requests.get(self.screenshot_url)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        else:
            print('截图失败')
            return None

    def disconnect(self):
        # Example of how to use run_adb with the updated device_serial handling
        self.run_adb(['disconnect'])

# automation = Automation(adb_path, device_serial, port, screenshot_url)
# automation.automate()
# # Now if you need to change the device serial just update the property
# automation.device_serial = 'new_serial_number'
# # The next adb commands will use the new device serial

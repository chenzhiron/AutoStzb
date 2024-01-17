import os
import subprocess
import time
import requests
from PIL import Image
from io import BytesIO
import threading


class Automation:
    def __init__(self, adb, device_serial, port, sleep):
        self.adb = adb
        self.device_serial = device_serial
        self.auto_mation_port = port
        self.screenshot_url = "http://127.0.0.1:%d/screenshot" % port
        self.sleep = sleep

    def changeTimeSleep(self, key, v):
        setattr(self, key, v)

    def run_adb(self, args, pipeOutput=True):
        if self.device_serial:
            args = [self.adb] + ['-s' + self.device_serial] + args
            print('exec cmd : %s' % self.device_serial)
        else:
            args = [self.adb] + args

        out = None
        if (pipeOutput):
            out = subprocess.PIPE
        p = subprocess.Popen([str(arg) for arg in args], stdout=out, encoding='utf-8')
        stdout, stderr = p.communicate()
        return p.returncode, stdout, stderr

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
        # self.run_adb(["connect", self.device_serial])
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

    def run_automate_in_thread(self):
        automate_thread = threading.Thread(target=self.automate)
        automate_thread.daemon = True  # Set the thread as a daemon thread
        automate_thread.start()

    def automate(self):
        try:
            self.identify_device()
            class_path = self.locate_apk_path()
            (code, _, err) = self.run_adb(
                ["forward", "tcp:%d" % self.auto_mation_port, "tcp:%d" % self.auto_mation_port])
            print(">>> adb forward tcp:%d " % self.auto_mation_port, code)

            args = ["shell",
                    class_path,
                    "app_process",
                    "/",
                    "com.rayworks.droidcast.Main",
                    "--port=%d" % self.auto_mation_port]

            self.run_adb(args, pipeOutput=False)

        except Exception as e:
            print('截图方案出错了', e)

    def getScreenshots(self):
        time.sleep(self.sleep)
        response = requests.get(self.screenshot_url)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))
        else:
            print('截图失败')
            return None

    def disconnect(self, device_serial=None):
        if device_serial is None:
            device_serial = self.device_serial

        if device_serial is not None:
            self.run_adb(["disconnect", device_serial])
        else:
            print("No device serial number provided.")

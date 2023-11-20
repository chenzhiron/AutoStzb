import subprocess
import time
import requests
from PIL import Image
from io import BytesIO


class Automation:
    def __init__(self, adb, device_serial, port, screenshot_url, sleep):
        self.adb = adb
        self.device_serial = device_serial
        self.port = port
        self.screenshot_url = screenshot_url
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
            raise RuntimeError(
                "Locating apk failure, have you installed the app successfully?")

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
        try:
            self.identify_device()
            class_path = self.locate_apk_path()
            (code, _, err) = self.run_adb(
                ["forward", "tcp:%d" % self.port, "tcp:%d" % self.port])
            print(">>> adb forward tcp:%d " % self.port, code)

            args = ["shell",
                    class_path,
                    "app_process",
                    "/",
                    "com.rayworks.droidcast.Main",
                    "--port=%d" % self.port]

            self.run_adb(args, pipeOutput=False)

        except Exception as e:
            print('截图方案出错了', e)

    def get_screenshots(self):
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
            
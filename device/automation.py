import subprocess
import time
from io import BytesIO

import numpy as np
import requests
from PIL import Image

from config.paths import adb
from config.const import auto_mation, screenshot_url


def run_adb(args, pipeOutput=True):
    if auto_mation['device_serial']:
        args = [adb] + ['-s' + auto_mation['device_serial']] + args
        print('exec cmd : %s' % auto_mation['device_serial'])
    else:
        args = [adb] + args

    # print('exec cmd : %s' % args)
    out = None
    if (pipeOutput):
        out = subprocess.PIPE
    p = subprocess.Popen([str(arg)
                          for arg in args], stdout=out, encoding='utf-8')
    p = subprocess.Popen(args, stdout=out, encoding='utf-8')
    stdout, stderr = p.communicate()
    return p.returncode, stdout, stderr


def locate_apk_path():
    (rc, out, _) = run_adb(["shell", "pm",
                            "path",
                            "com.rayworks.droidcast"])
    if rc or out == "":
        raise RuntimeError(
            "Locating apk failure, have you installed the app successfully?")

    prefix = "package:"
    postfix = ".apk"
    beg = out.index(prefix, 0)
    end = out.rfind(postfix)
    return "CLASSPATH=" + out[beg + len(prefix):(end + len(postfix))].strip()


def identify_device():
    (rc, out, _) = run_adb(["devices"])
    if (rc):
        raise RuntimeError("Fail to find devices")
    else:
        # Output as following:
        # List of devices attached
        # 6466eb0c	device
        device_serial_no = auto_mation['device_serial']

        devicesInfo = str(out)
        deviceCnt = devicesInfo.count('device') - 1

        if deviceCnt < 1:
            raise RuntimeError("Fail to find devices")

        if (deviceCnt > 1 and (not device_serial_no)):
            raise RuntimeError(
                "Please specify the serial number of target device you want to use ('-s serial_number').")


def automate():
    try:
        identify_device()
        class_path = locate_apk_path()
        (code, _, err) = run_adb(
            ["forward", "tcp:%d" % auto_mation['port'], "tcp:%d" % auto_mation['port']])
        print(">>> adb forward tcp:%d " % auto_mation['port'], code)

        args = ["shell",
                class_path,
                "app_process",
                "/",  # unused
                "com.rayworks.droidcast.Main",
                "--port=%d" % auto_mation['port']]

        run_adb(args, pipeOutput=False)

    except (Exception) as e:
        print('截图方案出错了', e)


# http 截图方案

def get_screenshot(area):
    response = requests.get(screenshot_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content)).crop(area)
        return np.array(image)
    else:
        print('截图失败')
        return None


def get_screenshots():
    time.sleep(0.3)
    response = requests.get(screenshot_url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        print('截图失败')
        return None
# if __name__ == '__main__':
#     try:
#         automate()
#     except Exception as e:
#         print(e)

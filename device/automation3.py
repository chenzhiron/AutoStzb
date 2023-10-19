#!/usr/local/bin/python -u

# Script (generated for Python 3.6+) to automate the configurations to show the screenshot on your
# default web browser.
# To get started, simply run : 'python ./automation.py'

import subprocess
import signal

from config.paths import adb

# adb = './device/adb/adb.exe'
devices = 0
screenshot_url = ''

args_in = {
    'device_serial': '127.0.0.1:62001',
    'port': 53515
}


def run_adb(args, pipeOutput=True):
    if args_in['device_serial']:
        args = [adb] + ['-s' + args_in['device_serial']] + args
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
    return (p.returncode, stdout, stderr)


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
        device_serial_no = args_in['device_serial']

        devicesInfo = str(out)
        deviceCnt = devicesInfo.count('device') - 1

        if deviceCnt < 1:
            raise RuntimeError("Fail to find devices")

        if (deviceCnt > 1 and (not device_serial_no)):
            raise RuntimeError(
                "Please specify the serial number of target device you want to use ('-s serial_number').")


def print_url():
    # ip route:
    # e.g. 192.168.0.0/24 dev wlan0 proto kernel scope link src 192.168.0.125
    (rc, out, _) = run_adb(
        ["shell", "ip route | awk '/wlan*/{ print $9 }'| tr -d '\n'"])
    screenshot_url = ('http://' +
                      '127.0.0.1'  # str(out)
                      + ':' + str(args_in['port']) + '/screenshot')


def handler(signum, frame):
    print('\n>>> Signal caught: ', signum)
    (code, out, err) = run_adb(
        ["forward", "--remove", "tcp:%d" % args_in['port']])
    print(">>> adb unforward tcp:%d " % args_in['port'], code)


def automate(port):
    # handle the keyboard interruption explicitly
    signal.signal(signal.SIGINT, handler)
    try:
        identify_device()

        class_path = locate_apk_path()

        (code, _, err) = run_adb(
            ["forward", "tcp:%d" % args_in['port'], "tcp:%d" % args_in['port']])
        print(">>> adb forward tcp:%d " % args_in['port'], code)

        print_url()

        args = ["shell",
                class_path,
                "app_process",
                "/",  # unused
                "com.rayworks.droidcast.Main",
                "--port=%d" % args_in['port']]

        # delay opening the web page
        # t = Timer(2, open_browser)
        # t.start()

        # event loop starts
        run_adb(args, pipeOutput=False)

    except (Exception) as e:
        print(e)


def return_device():
    global devices
    return devices


def return_url():
    return screenshot_url


def connect_device(port='127.0.0.1:62001'):
    adb_command = [adb, '-s', port]
    global devices
    # devices = subprocess.run(adb_command)
    devices = subprocess.run(adb_command)
    print(devices)
    automate(args_in['port'])
    return devices


if __name__ == '__main__':
    connect_device()

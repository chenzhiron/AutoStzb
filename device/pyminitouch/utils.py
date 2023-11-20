import socket
import subprocess

from device.pyminitouch import config


def str2byte(content):
    """ compile str to byte """
    return content.encode(config.DEFAULT_CHARSET)


def is_port_using(port_num):
    """ if port is using by others, return True. else return False """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        result = s.connect_ex((config.DEFAULT_HOST, port_num))
        # if port is using, return code should be 0. (can be connected)
        return result == 0
    finally:
        s.close()


def restart_adb():
    """ restart adb server """
    _ADB = config.ADB_EXECUTOR
    subprocess.check_call([_ADB, "kill-server"])
    subprocess.check_call([_ADB, "start-server"])


def is_device_connected(device_id):
    """ return True if device connected, else return False """
    _ADB = config.ADB_EXECUTOR
    try:
        device_name = subprocess.check_output(
            [_ADB, "-s", device_id, "shell", "getprop", "ro.product.model"]
        )
        device_name = (
            device_name.decode(config.DEFAULT_CHARSET)
            .replace("\n", "")
            .replace("\r", "")
        )
    except subprocess.CalledProcessError:
        return False
    return True

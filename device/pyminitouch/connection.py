import subprocess
import socket
import time
import os
from loguru import logger
from device.pyminitouch import config


def str2byte(content):
    """ compile str to byte """
    return content.encode(config.DEFAULT_CHARSET)


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


_ADB = config.ADB_EXECUTOR


class MNTInstaller(object):
    """ install minitouch for android devices """

    def __init__(self, device_id, adb):
        self._ADB = adb
        self.device_id = device_id
        self.abi = self.get_abi()
        if self.is_mnt_existed():
            logger.info("minitouch already existed in {}".format(device_id))
        else:
            self.download_target_mnt()

    def get_abi(self):
        abi = subprocess.getoutput(
            "{} -s {} shell getprop ro.product.cpu.abi".format(self._ADB, self.device_id)
        )
        logger.info("device {} is {}".format(self.device_id, abi))
        return abi

    def download_target_mnt(self):
        abi = self.get_abi()
        # 获取当前文件的绝对路径
        current_path = os.path.abspath(__file__)
        # 获取当前文件的目录
        dir_path = os.path.dirname(current_path)
        # 拼接获取 libs 目录下文件的绝对路径
        file_path = os.path.join(dir_path, 'libs', '{}', 'minitouch')
        mnt_path = file_path.format(abi)

        # push and grant
        subprocess.check_call(
            [self._ADB, "-s", self.device_id, "push", mnt_path, config.MNT_HOME]
        )
        subprocess.check_call(
            [self._ADB, "-s", self.device_id, "shell", "chmod", "777", config.MNT_HOME]
        )
        logger.info("minitouch already installed in {}".format(config.MNT_HOME))

    def is_mnt_existed(self):
        file_list = subprocess.check_output(
            [self._ADB, "-s", self.device_id, "shell", "ls", "/data/local/tmp"]
        )
        return "minitouch" in file_list.decode(config.DEFAULT_CHARSET)


class MNTServer(object):
    _PORT_SET = config.PORT_SET

    def __init__(self, device_id, adb, port):
        assert is_device_connected(device_id)
        self._ADB = adb
        self.device_id = device_id
        logger.info("searching a usable port ...")
        self.port = port
        logger.info("device {} bind to port {}".format(device_id, self.port))

        # check minitouch
        self.installer = MNTInstaller(device_id, adb)

        # keep minitouch alive
        self._forward_port()
        self.mnt_process = None
        self._start_mnt()

        # make sure it's up
        time.sleep(1)
        assert (
            self.heartbeat()
        ), "minitouch did not work. see https://github.com/williamfzc/pyminitouch/issues/11"

    def stop(self):
        self.mnt_process and self.mnt_process.kill()
        self._PORT_SET.add(self.port)
        logger.info("device {} unbind to {}".format(self.device_id, self.port))

    def _forward_port(self):
        """ allow pc access minitouch with port """
        command_list = [
            self._ADB,
            "-s",
            self.device_id,
            "forward",
            "tcp:{}".format(self.port),
            "localabstract:minitouch",
        ]
        logger.debug("forward command: {}".format(" ".join(command_list)))
        output = subprocess.check_output(command_list)
        logger.debug("output: {}".format(output))

    def _start_mnt(self):
        command_list = [
            self._ADB,
            "-s",
            self.device_id,
            "shell",
            "/data/local/tmp/minitouch",
        ]
        logger.info("start minitouch: {}".format(" ".join(command_list)))
        self.mnt_process = subprocess.Popen(command_list, stdout=subprocess.DEVNULL)

    def heartbeat(self):
        exit_cde = self.mnt_process.poll()
        return self.mnt_process.poll() is None


class MNTConnection(object):
    """ manage socket connection between pc and android """

    _DEFAULT_HOST = config.DEFAULT_HOST
    _DEFAULT_BUFFER_SIZE = config.DEFAULT_BUFFER_SIZE

    def __init__(self, port):
        self.port = port
        # build connection
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self._DEFAULT_HOST, self.port))
        self.client = client

        # get minitouch server info
        socket_out = client.makefile()

        # v <version>
        # protocol version, usually it is 1. needn't use this
        socket_out.readline()

        # ^ <max-contacts> <max-x> <max-y> <max-pressure>
        _, max_contacts, max_x, max_y, max_pressure, *_ = (
            socket_out.readline().replace("\n", "").replace("\r", "").split(" ")
        )
        self.max_contacts = max_contacts
        self.max_x = max_x
        self.max_y = max_y
        self.max_pressure = max_pressure

        # $ <pid>
        _, pid = socket_out.readline().replace("\n", "").replace("\r", "").split(" ")
        self.pid = pid

        logger.info(
            "minitouch running on port: {}, pid: {}".format(self.port, self.pid)
        )
        logger.info(
            "max_contact: {}; max_x: {}; max_y: {}; max_pressure: {}".format(
                max_contacts, max_x, max_y, max_pressure
            )
        )

    def disconnect(self):
        self.client and self.client.close()
        self.client = None
        logger.info("minitouch disconnected")

    def send(self, content):
        """ send message and get its response """
        byte_content = str2byte(content)
        self.client.sendall(byte_content)
        return self.client.recv(self._DEFAULT_BUFFER_SIZE)

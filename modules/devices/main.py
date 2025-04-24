import uiautomator2 as u2
from loguru import logger


class DeviceManager:
    def __init__(self, simulator_name):
        self.simulator = simulator_name
        self._device = None

    @property
    def device(self):
        if not self._device:
            self._connect()
        return self._device

    def _connect(self):
        """ADB连接管理"""
        try:
            self._device = u2.connect(self.simulator)
            logger.info(f"Connected to {self.simulator}")
        except Exception as e:
            logger.error(f"Connection failed: {str(e)}")
            raise

    def release(self):
        """资源释放"""
        if self._device:
            self._device.service("uiautomator").stop()
            self._device = None
            logger.info(f"Released {self.simulator}")


class DeviceOperator:
    def __init__(self, device_manager):
        self.d = device_manager.device

    def click(self, x: int, y: int):
        logger.debug(f"Click at ({x}, {y})")
        self.d.click(x, y)

    def swipe(self, origin_x, origin_y, next_x, next_y, times=1):
        logger.debug(f"Swipe from ({origin_x}, {origin_y}) to ({next_x}, {next_y})")
        self.d.swipe(origin_x, origin_y, next_x, next_y, times)

    def drag(self, sx, sy, ex, ey, duration=1):
        logger.debug(f"Drag from ({sx}, {sy}) to ({ex}, {ey}) with duration {duration}")
        self.d.drag(sx, sy, ex, ey, duration)

    def screenshot(self):
        logger.debug("Taking screenshot")
        return self.d.screenshot()

    def copy_val(self):
        self.d.set_input_ime()
        return self.d.clipboard

    def input(self, v:str, clear=True):
        logger.debug(f"Input value: {v}, clear: {clear}")
        self.d.send_keys(v, clear)


if __name__ == "__main__":
    d = DeviceOperator(DeviceManager("127.0.0.1:16384"))
    d.click(100,200)

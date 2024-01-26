import time

from modules.devices.pyminitouch.connection import MNTConnection, MNTServer
from modules.devices.pyminitouch import config


class CommandBuilder(object):

    def __init__(self):
        self._content = ""
        self._delay = 0

    def append(self, new_content):
        self._content += new_content + "\n"

    def commit(self):
        """ add minitouch command: 'c\n' """
        self.append("c")

    def wait(self, ms):
        """ add minitouch command: 'w <ms>\n' """
        self.append("w {}".format(ms))
        self._delay += ms

    def up(self, contact_id):
        """ add minitouch command: 'u <contact_id>\n' """
        self.append("u {}".format(contact_id))

    def down(self, contact_id, x, y, pressure):
        """ add minitouch command: 'd <contact_id> <x> <y> <pressure>\n' """
        self.append("d {} {} {} {}".format(contact_id, x, y, pressure))

    def move(self, contact_id, x, y, pressure):
        """ add minitouch command: 'm <contact_id> <x> <y> <pressure>\n' """
        self.append("m {} {} {} {}".format(contact_id, x, y, pressure))

    def publish(self, connection):
        """ apply current commands (_content), to your device """
        self.commit()
        final_content = self._content
        connection.send(final_content)
        self.reset()

    def reset(self):
        """ clear current commands (_content) """
        self._content = ""
        self._delay = 0


class MNTDevice(object):
    def __init__(self, device_id, adb, port, client_host='127.0.0.1'):
        self.host = client_host
        self._ADB = adb
        self.device_id = device_id
        self.port = port
        self.server = None
        self.connection = None

    def reset(self):
        self.stop()
        self.start()

    def change_device(self, new_device_id):
        self.device_id = new_device_id
        self.reset()

    def start(self):
        try:
            # prepare for connection
            self.server = MNTServer(self.device_id, self._ADB, self.port)
            # real connection
            self.connection = MNTConnection(self.server.port, self.host)
        except Exception as e:
            print('点击方案出错', e)

    def stop(self):
        print(dir(self.connection))
        self.connection.disconnect()
        self.server.stop()

    def tap(self, points, pressure=100, duration=None, no_up=None):
        points = [list(map(int, each_point)) for each_point in points]

        _builder = CommandBuilder()
        for point_id, each_point in enumerate(points):
            x, y = each_point
            _builder.down(point_id, x, y, pressure)
        _builder.commit()

        # apply duration
        if duration:
            _builder.wait(duration)
            _builder.commit()

        # need release?
        if not no_up:
            for each_id in range(len(points)):
                _builder.up(each_id)

        _builder.publish(self.connection)

    def swipe(self, points, pressure=100, duration=None, no_down=None, no_up=None):
        points = [list(map(int, each_point)) for each_point in points]

        _builder = CommandBuilder()
        point_id = 0

        # tap the first point
        if not no_down:
            x, y = points.pop(0)
            _builder.down(point_id, x, y, pressure)
            _builder.publish(self.connection)

        # start swiping
        for each_point in points:
            x, y = each_point
            _builder.move(point_id, x, y, pressure)

            # add delay between points
            if duration:
                _builder.wait(duration)
            _builder.commit()

        _builder.publish(self.connection)

        # release
        if not no_up:
            _builder.up(point_id)
            _builder.publish(self.connection)

    # extra functions' name starts with 'ext_'
    def ext_smooth_swipe(
            self, points, pressure=100, duration=None, part=None, no_down=None, no_up=None
    ):

        if not part:
            part = 30

        points = [list(map(int, each_point)) for each_point in points]
        for each_index in range(len(points) - 1):
            cur_point = points[each_index]
            next_point = points[each_index + 1]

            offset = (
                int((next_point[0] - cur_point[0]) / part),
                int((next_point[1] - cur_point[1]) / part),
            )
            new_points = [
                (cur_point[0] + i * offset[0], cur_point[1] + i * offset[1])
                for i in range(part + 1)
            ]
            self.swipe(
                new_points,
                pressure=pressure,
                duration=duration,
                no_down=no_down,
                no_up=no_up,
            )

# if __name__ == "__main__":
#
#     _DEVICE_ID = "4df189487c7b6fef"
#
#     with safe_connection(_DEVICE_ID) as d:
#         builder = CommandBuilder()
#         builder.down(0, 400, 400, 50)
#         builder.commit()
#         builder.move(0, 500, 500, 50)
#         builder.commit()
#         builder.move(0, 800, 400, 50)
#         builder.commit()
#         builder.up(0)
#         builder.commit()
#         builder.publish(d)
#
#     with safe_device(_DEVICE_ID) as d:
#         builder = CommandBuilder()
#         builder.down(0, 400, 400, 50)
#         builder.commit()
#         builder.move(0, 500, 500, 50)
#         builder.commit()
#         builder.move(0, 800, 400, 50)
#         builder.commit()
#         builder.up(0)
#         builder.commit()
#         builder.publish(d.connection)
#
#     # option1:
#     device = MNTDevice(_DEVICE_ID)
#     device.tap([(400, 500), (500, 500)], duration=1000)
#
#     # you should control time delay by yourself
#     # otherwise when connection lost, action will never stop.
#     time.sleep(1)
#
#     device.stop()
#
#     # option2:
#     with safe_device(_DEVICE_ID) as device:
#         device.tap([(400, 500), (500, 500)])
#         device.swipe([(400, 500), (500, 500)], duration=500)
#         time.sleep(0.5)

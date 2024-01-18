import yaml
from pywebio.output import use_scope, put_button, put_text, put_scope
from pywebio.pin import put_input, pin_on_change
from config.config import globalConfig


def set_new_data(instance, key):
    def set_data(val):
        instance.data['Simulator'][key] = val
        instance.write()
    return set_data


class LoadConfig:
    def __init__(self, data, path):
        self.data = data
        self.path = path

    def write(self):
        with open(self.path, 'w') as f:
            yaml.dump(self.data, f)

    def renderConfig(self):
        with use_scope('center', clear=True):
            put_scope('simulator', [put_text('模拟器配置'), put_input('simulator', value=self.data['Simulator']['url'])])
            put_scope('screenshot_sleep',
                      [put_text('截图等待'), put_input('screenshot_sleep', value=self.data['Simulator']['screenshot_sleep'])])
        pin_on_change('simulator', set_new_data(self, 'url'), clear=True)
        pin_on_change('screenshot_sleep', set_new_data(self, 'screenshot_sleep'), clear=True)

    def render(self):
        return put_button('配置', onclick=self.renderConfig)


change_config = LoadConfig(globalConfig, globalConfig['Simulator']['path'])

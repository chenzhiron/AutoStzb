from datetime import datetime

import pytz
from pywebio.output import put_row, put_column, put_text, put_collapse
from pywebio.pin import put_checkbox, put_input


def def_lable_checkbox(component):
    for v in component.spec["input"]["options"]:
        v["label"] = ""
    return component


def explain_componet(texts, component):
    text_components = []
    for k, v in enumerate(texts):
        if k > 0:
            text_components.append(put_text(v).style("font-size:14px"))
        else:
            text_components.append(put_text(v))

    return put_row(
        [
            put_column(text_components).style("display:block;"),
            component,
        ]
    ).style("margin-bottom:15px;")


def render_checkbox(taksname, explaintext, checkboxkey, props, updatecheckbox):
    explain_componet(
        [explaintext],
        def_lable_checkbox(
            put_checkbox(checkboxkey, options=[True], value=props[checkboxkey])
        ),
    )
    pin_on_change(
        checkboxkey,
        onchange=lambda v: updatecheckbox(taksname, checkboxkey, v),
        clear=True,
    )


def render_input(taksname, explaintext, inputkey, props, inputfn):
    explain_componet(
        [explaintext],
        put_input(inputkey, value=props[inputkey]),
    )
    pin_on_change(
        inputkey, onchange=lambda v: inputfn(taksname, inputkey, v), clear=True
    )


def formatdate(v):
    v = datetime.fromisoformat(v).replace(tzinfo=pytz.UTC)
    ts = v.timestamp()
    return int(ts)


def render_number(taksname, explaintext, inputkey, allprops, numberfn):
    explain_componet(
        [explaintext],
        put_input(inputkey, value=allprops[inputkey], type="number"),
    )
    pin_on_change(
        inputkey, onchange=lambda v: numberfn(taksname, inputkey, v), clear=True
    )


def render_datetime(
        taksname, explaintext, inputkey, allprops, datetimefn, formatfn=formatdate
):
    explain_componet(
        [explaintext],
        put_input(inputkey, value=allprops[inputkey], type="datetime-local"),
    )
    pin_on_change(
        inputkey,
        onchange=lambda v: datetimefn(taksname, inputkey, formatfn(v)),
        clear=True,
    )


from typing import Any, Callable, Dict, Type
from pywebio.pin import pin_update, pin_on_change


class ConfigProperty:
    """配置属性基类"""

    def __init__(self, name: str, prop_type: Type, default: Any, label: str = None):
        self.name = name
        self.prop_type = prop_type
        self.value = default
        self.label = label or name
        self._on_change_callbacks = []

    def render(self, parent_name: str):
        """渲染组件到页面"""
        raise NotImplementedError

    def update(self, value: Any):
        """更新属性值"""
        self.value = value
        self._notify_change()

    def on_change(self, callback: Callable[[Any], None]):
        """添加值变更回调"""
        self._on_change_callbacks.append(callback)

    def _notify_change(self):
        """通知所有变更回调"""
        for callback in self._on_change_callbacks:
            callback(self.value)


class BooleanProperty(ConfigProperty):
    """布尔类型属性"""

    def render(self, parent_name: str):
        full_name = f"{parent_name}_{self.name}"
        put_checkbox(full_name, options=[{'label': self.label, 'value': True}],
                     value=[True] if self.value else [])

        def handle_change(value):
            self.update(bool(value))

        pin_on_change(full_name, onchange=handle_change)


class StringProperty(ConfigProperty):
    """字符串类型属性"""

    def render(self, parent_name: str):
        full_name = f"{parent_name}_{self.name}"
        put_input(full_name, label=self.label, value=self.value)

        def handle_change(value):
            self.update(str(value))

        pin_on_change(full_name, onchange=handle_change)


class NumberProperty(ConfigProperty):
    """数字类型属性"""

    def render(self, parent_name: str):
        full_name = f"{parent_name}_{self.name}"
        put_input(full_name, label=self.label, value=self.value, type='number')

        def handle_change(value):
            try:
                self.update(int(value))
            except (ValueError, TypeError):
                pass

        pin_on_change(full_name, onchange=handle_change)


class DateTimeProperty(ConfigProperty):
    """日期时间类型属性"""

    def render(self, parent_name: str):
        full_name = f"{parent_name}_{self.name}"
        put_input(full_name, label=self.label, value=self.value, type='datetime-local')

        def handle_change(value):
            self.update(value)  # 实际应用中可能需要转换为时间戳

        pin_on_change(full_name, onchange=handle_change)


class TaskConfig:
    """任务配置封装类"""
    PROPERTY_TYPES = {
        bool: BooleanProperty,
        str: StringProperty,
        int: NumberProperty,
        float: NumberProperty,
        # 可以添加更多类型映射
    }

    def __init__(self, name: str, config_data: Dict):
        self.name = name
        self.properties = {}

        for prop_name, prop_value in config_data.items():
            prop_type = type(prop_value)
            if isinstance(prop_value, dict):
                # 处理嵌套配置
                self.properties[prop_name] = NestedConfigProperty(prop_name, prop_value)
            else:
                property_class = self.PROPERTY_TYPES.get(prop_type, StringProperty)
                self.properties[prop_name] = property_class(prop_name, prop_type, prop_value)

    def render(self):
        """渲染所有属性组件"""
        for prop in self.properties.values():
            prop.render(self.name)

    def update_property(self, prop_name: str, value: Any):
        """更新属性值并刷新UI"""
        if prop_name in self.properties:
            self.properties[prop_name].update(value)
            # 使用pin_update刷新UI
            full_name = f"{self.name}_{prop_name}"
            pin_update(full_name, value=value)

    def get_property(self, prop_name: str) -> Any:
        """获取属性值"""
        return self.properties[prop_name].value if prop_name in self.properties else None


class NestedConfigProperty(ConfigProperty):
    """嵌套配置属性"""

    def __init__(self, name: str, config_data: Dict):
        super().__init__(name, dict, config_data)
        self.task_config = TaskConfig(name, config_data)

    def render(self, parent_name: str):
        put_collapse(self.label, [
            lambda: self.task_config.render()
        ])

    def update(self, value: Dict):
        """更新嵌套配置"""
        if isinstance(value, dict):
            for k, v in value.items():
                if k in self.task_config.properties:
                    self.task_config.properties[k].update(v)
            self._notify_change()

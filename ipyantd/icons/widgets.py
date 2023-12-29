import traitlets
import ipyreact
from . import module as _icon_module  # noqa: F401


class Icon(ipyreact.Widget):
    _module = traitlets.Unicode("@ant-design/icons").tag(sync=True)

    def __init__(self, name, **kwargs):
        super().__init__(**{"_type": name, **kwargs})

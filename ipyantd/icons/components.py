from . import widgets
import reacton


def Icon(
    name: str,
    props={},
    events={},
    children=[],
):
    widget_cls = widgets.Icon
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return reacton.core.Element(comp, kwargs={"name": name, "props": props, "events": events, "children": children})

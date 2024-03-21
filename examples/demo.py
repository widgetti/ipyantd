# run as: $ solara run examples/demo.py
import ipyantd.components as antd
import ipyantd.icons.components as icons

import solara
import ipyreact


message = solara.reactive(None)
dialog = solara.reactive(False)
slider = solara.reactive(0)
slider_range = solara.reactive([20, 70])
select = solara.reactive("pear")
multi_select = solara.reactive(["apple", "pear"])
switch = solara.reactive(False)


def dialog_open(event_data):
    message.value = "Modal opened"
    dialog.value = True


def dialog_close(event_data):
    message.value = "Modal closed"
    dialog.value = False


def report_click(event_data=None):
    message.value = "Clicked"


options = [
    dict(label="Apple", value="apple"),
    dict(label="Pear", value="pear"),
    dict(label="Cherry", value="cherry"),
]

menu_items = [
    dict(
        key="1",
        label=ipyreact.Widget.element(_type="div", children=["Click me 1"], events={"onClick": report_click}),
    ),
    dict(
        key="2",
        label=ipyreact.Widget.element(_type="div", children=["Click me 2"], events={"onClick": report_click}),
    ),
]
text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. 
Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. 
Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. 
Duis semper.
Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue.
"""


@solara.component
def Page():
    with ipyreact.Widget.element(_type="div"):
        with antd.Row(props=dict(gutter=[48, 48], style={"padding": "100px"})):
            # buttons
            with antd.Col(props=dict(span=8, style={"boxSizing": "border-box"})):
                with ipyreact.Widget.element(_type="div"):
                    antd.Button(children=["Button"], props=dict(type="primary"), events={"onClick": report_click})
                    antd.Button(children=["Button"])
            with antd.Col(props=dict(span=8)):
                antd.Button(children=["Button"], props=dict(type="primary", shape="round"))
                antd.Button(props=dict(type="primary", shape="circle", icon=icons.Icon("SearchOutlined")))
                antd.Button(props=dict(shape="circle", icon=icons.Icon("SearchOutlined")))
            with antd.Col(props=dict(span=8)):
                antd.Button(children=["Button"], props=dict(type="text"))
            with antd.Col(props=dict(span=8)):
                antd.Button(children=["Button"], props=dict(type="primary", size="small"))
                antd.Button(children=["Button"], props=dict(size="small"))
            with antd.Col(props=dict(span=8)):
                antd.Button(children=["Button"], props=dict(type="primary", shape="round", size="small"))
                antd.Button(props=dict(type="primary", shape="circle", icon=icons.Icon("SearchOutlined"), size="small"))
                antd.Button(props=dict(shape="circle", icon=icons.Icon("SearchOutlined"), size="small"))
            with antd.Col(props=dict(span=8)):
                antd.Button(children=["Button"], props=dict(type="text", size="small"))

            # sliders
            with antd.Col(props=dict(span=8)):
                antd.Slider(value=slider.value, on_value=slider.set, props=dict(min=0, max=100))
            with antd.Col(props=dict(span=8)):
                antd.Slider(value=slider_range.value, on_value=slider_range.set, props=dict(min=0, max=100, range=True))
            with antd.Col(props=dict(span=8)):
                antd.Slider(value=slider.value, on_value=slider.set, props=dict(min=0, max=100, tooltip=dict(open=True)))

            # select
            with antd.Col(props=dict(span=8)):
                antd.Select(value=select.value, on_value=select.set, props=dict(options=options, style=dict(width="120px")))
            with antd.Col(props=dict(span=8)):
                antd.Select(value=multi_select.value, on_value=multi_select.set, props=dict(options=options, style=dict(width="220px"), mode="multiple"))
            with antd.Col(props=dict(span=8)):
                pass
                # only supported in 5.31+
                # antd.Select(value="pear", props=dict(options=options, variant="filled", style=dict(width="120px"))),

            # misc
            with antd.Col(props=dict(span=8)):
                antd.Switch(value=switch.value, on_value=switch.set)
            with antd.Col(props=dict(span=8)):
                with antd.Dropdown(props=dict(menu=dict(items=menu_items), trigger=["click"])):
                    ipyreact.Widget.element(_type="span", children=["Menu"])
            with antd.Col(props=dict(span=8)):
                with antd.Modal(value=dialog.value, events={"onOk": dialog_close, "onCancel": dialog_close}):
                    ipyreact.Widget.element(_type="div", children=[text])
                antd.Button(children=["Dialog"], props=dict(type="primary"), events={"onClick": dialog_open})

    solara.Preformatted(f"message: {message.value or ''}")
    solara.Preformatted(f"slider: {slider.value}")
    solara.Preformatted(f"slider_range: {slider_range.value}")
    solara.Preformatted(f"select: {select.value}")
    solara.Preformatted(f"multi_select: {multi_select.value}")
    solara.Preformatted(f"switch: {switch.value}")

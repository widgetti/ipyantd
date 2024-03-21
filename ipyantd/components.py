import ipyreact
import reacton
from . import widgets
from .types import (
    ButtonProps,
    ButtonPropsEvents,
    SliderSingleProps,
    SliderSinglePropsEvents,
    ColorPickerProps,
    ColorPickerPropsEvents,
    FlexProps,
    FlexPropsEvents,
    ColorModel,
    RGB1,
    RGBA1,
    HSB,
    HSBA,
    RowProps,
    RowPropsEvents,
    ColProps,
    ColPropsEvents,
    DatePickerProps,
    SelectProps,
    SelectPropsEvents,
    SwitchProps,
    SwitchPropsEvents,
    DropdownProps,
    DropdownPropsEvents,
    ModalProps,
    ModalPropsEvents,
)
from typing import Dict, List, Union, Optional, Callable, Any


ChildType = Union[ipyreact.Widget, str]
ChildrenType = Union[ChildType, List[ChildType]]


# not sure why this is not generated in typing
DatePickerPropsEvents = Dict


def Button(
    props: ButtonProps = {},
    events: ButtonPropsEvents = {},
    children: ChildrenType = [],
):
    widget_cls = widgets.Button
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return reacton.core.Element(comp, kwargs={"props": props, "events": events, "children": children})


def Slider(
    value: Union[float] = 0,
    on_value: Callable[[Union[float]], None] = lambda x: None,
    props: SliderSingleProps = {},
    events: SliderSinglePropsEvents = {},
    children: ChildrenType = [],
):
    return widgets.Slider.element(value=value, on_value=on_value, props=props, events=events, children=children)


def Flex(props: FlexProps = {}, events: FlexPropsEvents = {}, children: ChildrenType = []):
    widget_cls = widgets.Flex
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return reacton.core.Element(comp, kwargs={"props": props, "children": children})


def Row(props: RowProps = {}, events: RowPropsEvents = {}, children: ChildrenType = []):
    widget_cls = widgets.Row
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return reacton.core.Element(comp, kwargs={"props": props, "events": events, "children": children})


def Col(props: ColProps = {}, events: ColPropsEvents = {}, children: ChildrenType = []):
    widget_cls = widgets.Col
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return reacton.core.Element(comp, kwargs={"props": props, "events": events, "children": children})


def Select(
    value: Optional[Union[Any, float]] = None,
    on_value: Optional[Callable[[Union[Any, float]], None]] = None,
    props: SelectProps = {},
    events: SelectPropsEvents = {},
    children: ChildrenType = [],
):
    widget_cls = widgets.Select
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return reacton.core.Element(
        comp,
        kwargs={
            "value": value,
            "on_value": on_value,
            "props": props,
            "events": events,
            "children": children,
        },
    )


def Switch(
    value: Optional[bool] = None,
    on_value: Optional[Callable[[bool], None]] = None,
    props: SwitchProps = {},
    events: SwitchPropsEvents = {},
    children: ChildrenType = [],
):
    widget_cls = widgets.Switch
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return reacton.core.Element(
        comp,
        kwargs={
            "value": value,
            "on_value": on_value,
            "props": props,
            "events": events,
            "children": children,
        },
    )


def Dropdown(
    value: bool = False,
    on_value: Optional[Callable[[bool], None]] = None,
    props: DropdownProps = {},
    events: DropdownPropsEvents = {},
    children: ChildrenType = [],
):
    widget_cls = widgets.Dropdown
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return reacton.core.Element(
        comp,
        kwargs={
            "value": value,
            "on_value": on_value,
            "props": props,
            "events": events,
            "children": children,
        },
    )


def Modal(
    value: bool = False,
    on_value: Optional[Callable[[bool], None]] = None,
    props: ModalProps = {},
    events: ModalPropsEvents = {},
    children: ChildrenType = [],
):
    widget_cls = widgets.Modal
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return reacton.core.Element(
        comp,
        kwargs={
            "value": value,
            "on_value": on_value,
            "props": props,
            "events": events,
            "children": children,
        },
    )


def DatePicker(
    value: Optional[str] = None,
    on_value: Optional[Callable[[str], None]] = None,
    props: DatePickerProps = {},
    events: DatePickerPropsEvents = {},
    children: ChildrenType = [],
):
    widget_cls = widgets.DatePicker
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return reacton.core.Element(
        comp,
        kwargs={
            "value": value,
            "on_value": on_value,
            "props": props,
            "events": events,
            "children": children,
        },
    )


def ColorPicker(
    value: Optional[Union[ColorModel, RGB1, RGBA1, HSB, HSBA, Union[str, float]]] = None,
    on_value: Optional[Callable[[Union[ColorModel, RGB1, RGBA1, HSB, HSBA, Union[str, float]]], None]] = None,
    props: ColorPickerProps = {},
    events: ColorPickerPropsEvents = {},
    children: ChildrenType = [],
):
    widget_cls = widgets.ColorPicker
    comp = reacton.core.ComponentWidget(widget=widget_cls)
    return reacton.core.Element(
        comp,
        kwargs={
            "value": value,
            "on_value": on_value,
            "props": props,
            "events": events,
            "children": children,
        },
    )


@reacton.component
def Page():
    count, set_count = reacton.use_state(0)
    color, set_color = reacton.use_state("red")
    date, set_date = reacton.use_state(None)
    print(count)

    def click(*event):
        print(event)
        set_count(lambda x: x + 1)

    def pick(*data):
        print(data)
        set_date(data[0])

    with Flex(gap="small") as f:
        if date:
            DatePicker(onChange=pick, value=date)
        else:
            DatePicker(onChange=pick)
        Button(children=["Hi1 " + str(count)], props=dict(type="primary"), onClick=click)
        Button(
            children=["Hi2 " + str(date)],
            type="primary",
            onClick=click,
            danger=count > 4,
            style=dict(minWidth="300px", backgroundColor="green"),
        )
    return f


Page()

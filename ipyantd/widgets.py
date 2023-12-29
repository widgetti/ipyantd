import ipyreact
import traitlets
from traitlets import List, Unicode, observe


class Button(ipyreact.Widget):
    _module = traitlets.Unicode("antd").tag(sync=True)
    _type = traitlets.Unicode("Button").tag(sync=True)


class Slider(ipyreact.ValueWidget):
    _module = traitlets.Unicode("antd-jupyter").tag(sync=True)
    _type = traitlets.Unicode("SliderStatefull").tag(sync=True)


class Flex(ipyreact.Widget):
    _module = traitlets.Unicode("antd").tag(sync=True)
    _type = traitlets.Unicode("Flex").tag(sync=True)


class DatePicker(ipyreact.ValueWidget):
    # _module = traitlets.Unicode("antd").tag(sync=True)
    # _type = traitlets.Unicode("DatePicker").tag(sync=True)
    _esm = """
    import {DatePicker} from "antd";
    import dayjs from "https://esm.sh/dayjs@1.11.10"

    export default ({value, setValue, children, ...rest}) => {
        const dayjsValue = Boolean(value) ? dayjs(value) : value
        console.log(value, dayjsValue)
        return <DatePicker value={dayjsValue} onChange={(dayjsValue) => setValue((dayjsValue))} {...rest}>{children}</DatePicker>
    }
    
    """
    _dependencies = List(Unicode(), ["antd", "dayjs-formatter"], allow_none=True).tag(
        sync=True
    )


class ColorPicker(ipyreact.ValueWidget):
    _esm = """
import {ColorPicker} from "antd";

export default ({value, setValue, children, ...rest}) => {
    //const dayjsValue = Boolean(value) ? dayjs(value) : value
    //console.log(value, dayjsValue)
    return <ColorPicker value={value} onChange={(color) => setValue((color.metaColor))} {...rest}>{children}</ColorPicker>
}
    
    """
    _dependencies = List(Unicode(), ["antd"], allow_none=True).tag(sync=True)


cp = ColorPicker()
cp

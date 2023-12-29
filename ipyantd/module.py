import ipyreact
from pathlib import Path

HERE = Path(__file__).parent

ant_module_path = HERE / "assets/antd.mjs"
ant_jupyter_module_path = HERE / "assets/antd-jupyter.js"

ipyreact.define_module("antd", ant_module_path)
ipyreact.define_module("antd-jupyter", ant_jupyter_module_path)
ipyreact.define_module(
    "dayjs-formatter",
    """
import dayjs from "https://esm.sh/dayjs@1.11.10"
import weekday from "https://esm.sh/dayjs@1.11.10/plugin/weekday"
import localeData from "https://esm.sh/dayjs@1.11.10/plugin/localeData"
import en from "https://esm.sh/dayjs@1.11.10/locale/en"
import quarterOfYear from "https://esm.sh/dayjs@1.11.10/plugin/quarterOfYear"

dayjs.locale('en') // use en?? locale globally

dayjs.extend(weekday)
dayjs.extend(localeData)
dayjs.extend(quarterOfYear)

export
const py2js = (pyValue) => Boolean(pyValue) ? dayjs(pyValue) : pyValue

export
const js2py = (jsValue) => JSON.stringify(jsValue)

""",
)

# def create_library():
#     dayjs = ipyreact.Widget(_esm="""
# import dayjs from "https://esm.sh/dayjs@1.11.10"
# import weekday from "https://esm.sh/dayjs@1.11.10/plugin/weekday"
# import localeData from "https://esm.sh/dayjs@1.11.10/plugin/localeData"
# import en from "https://esm.sh/dayjs@1.11.10/locale/en"
# import quarterOfYear from "https://esm.sh/dayjs@1.11.10/plugin/quarterOfYear"

# dayjs.locale('en') // use en?? locale globally

# dayjs.extend(weekday)
# dayjs.extend(localeData)
# dayjs.extend(quarterOfYear)

# export
# const py2js = (pyValue) => Boolean(pyValue) ? dayjs(pyValue) : pyValue

# export
# const js2py = (jsValue) => JSON.stringify(jsValue)

# """, _name="dayjs-formatter")

#     antd = ipyreact.Widget(_esm=ant_module_path.read_text(), _name="antd")
#     return None

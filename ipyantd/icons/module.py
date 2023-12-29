import ipyreact
from pathlib import Path

HERE = Path(__file__).parent

ant_design_icons_module_path = HERE.parent / "assets/@ant-design/icons.bundle.mjs"

ipyreact.define_module("@ant-design/icons", ant_design_icons_module_path)

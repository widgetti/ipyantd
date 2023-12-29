import * as React from "react";
import { Slider } from "antd";

export function SliderStatefull({ value, setValue, ...rest }) {
  return <Slider value={value} onChange={(v) => setValue(v)} {...rest} />;
}

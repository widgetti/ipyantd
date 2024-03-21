import * as React from "react";
import * as antd from "antd";

export function SliderStatefull({ value, setValue, ...rest }) {
  return <antd.Slider value={value} onChange={(v) => setValue(v)} {...rest} />;
}

export function SelectStatefull({ value, setValue, ...rest }) {
  return <antd.Select value={value} onChange={(v) => setValue(v)} {...rest} />;
}

export function SwitchStatefull({ value, setValue, ...rest }) {
  return <antd.Switch value={value} onChange={(v) => setValue(v)} {...rest} />;
}

export function DropdownStatefull({ value, setValue, ...rest }) {
  const onOpenChange = (open, info) => {
    setValue(open);
    if (rest.onOpenChange) {
      rest.onOpenChange({ open, info });
    }
  };
  return <antd.Dropdown open={value} onOpenChange={onOpenChange} {...rest} />;
}

export function ModalStatefull({ value, setValue, ...rest }) {
  const onOpenChange = (open) => {
    setValue(open);
    if (rest.onOpenChange) {
      rest.afterOpenChange(open);
    }
  };
  const handleOk = () => {
    // setValue(false);
    if (rest.onOk) {
      rest.onOk();
    }
  };
  const handleCancel = () => {
    // setValue(false);
    if (rest.onCancel) {
      rest.onCancel();
    }
  };
  return <antd.Modal open={value} afterOpenChange={onOpenChange} onOk={handleOk} onCancel={handleCancel} {...rest} />;
}

import json
from pathlib import Path
import collections


HERE = Path(__file__).parent

schema_file = HERE / "schema.json"

with open(schema_file, encoding="utf8") as f:
    schema = json.load(f)

mapping = {
    "React.ReactNode": "ReactNode",
    "React.CSSProperties": "CSSProperties",
    "React.FunctionComponent<P>": "FunctionComponent",
    "React.FunctionComponent<{}>": "FunctionComponent",
    "React.ComponentClass<P,any>": "ComponentClass",
    "React.MutableRefObject<PickerRefConfig>": "object",
    "React.WeakValidationMap<P>": "object",
    "Iterable<React.ReactNode>": "ReactNodeList",
    "Partial<Record<SemanticName,React.CSSProperties>>": "SpecificCssProperties",
    "React.Key": "StringOrNumber",
    "React.ReactInstance": "ElementOrComponent",
    "React.Component<any,{},any>": "Component",
    "React.ReactElement<any,string|React.JSXElementConstructor<any>>_1": "Element",
    "React.FunctionComponent<P>_1": "Component",
    "JSX.Element": "Element",
}

remove = [
    "React.Context<any>",
    "React.ReactPortal",
    "React.ReactElement<any,string|React.JSXElementConstructor<any>>",
    "React.Provider<any>",
    "React.WeakValidationMap<React.ProviderProps<any>>",
    "React.Validator<any>",
    "React.Validator<React.ReactNode>",
    "React.Consumer<any>",
    "React.ComponentClass<{},any>",
    "React.RefObject<HTMLDivElement>",
    "React.WeakValidationMap<{}>",
    "ValidationMap<any>",
    "React.WeakValidationMap<P>_1",
    "React.RefObject<any>",
    "Partial<Record<TabBarExtraPosition,React.ReactNode>>",
    "React.ComponentClass<P,any>_1",
]
remove_refs = ["#/definitions/" + k for k in remove]

events = collections.defaultdict(set)
schema["definitions"]["ReactNodeList"] = {
    "type": "array",
    "items": {"$ref": "#/definitions/ReactNode"},
}

ref_mapping = {"#/definitions/" + k: "#/definitions/" + v for k, v in mapping.items()}


def replace_refs(obj):
    if isinstance(obj, dict):
        if "$ref" in obj:
            if obj["$ref"] in ref_mapping:
                obj["$ref"] = ref_mapping[obj["$ref"]]
        for v in obj.values():
            replace_refs(v)
    elif isinstance(obj, list):
        for v in obj:
            replace_refs(v)


def remove_unsupported(obj):
    if isinstance(obj, dict):
        for key, value in obj.copy().items():
            if key == "$ref" and value in remove_refs:
                obj.pop(key)
            else:
                remove_unsupported(value)
    elif isinstance(obj, list):
        for v in obj.copy():
            if isinstance(v, dict) and "$ref" in v and v["$ref"] in remove_refs:
                obj.remove(v)
            else:
                remove_unsupported(v)


for name, definition in schema["definitions"].copy().items():
    if name in mapping:
        schema["definitions"][mapping[name]] = definition
        schema["definitions"].pop(name)
        name = mapping[name]
    if name in remove:
        schema["definitions"].pop(name)
        continue
    replace_refs(definition)
    remove_unsupported(definition)
    if "properties" in definition:
        for prop_name, prop in definition["properties"].copy().items():
            # lets drop all arias for now
            if prop_name.startswith("aria") or prop_name in ["role", "tabIndex"]:
                definition["properties"].pop(prop_name)
                continue
            # if "$ref" in prop:
            #     if prop["$ref"] in ref_mapping:
            #         prop["$ref"] = ref_mapping[prop["$ref"]]
            #     print(prop["$ref"])
            if prop_name.startswith("on"):
                # if "type" not in prop:
                #     raise ValueError("Missing type for", name, prop_name, definition)
                if "type" in prop and prop["type"] == "object":
                    prop["type"] = "function"
                events[name].add(prop_name)
                definition["properties"].pop(prop_name)
    if events[name]:
        definition["properties"]["events"] = {"$ref": "#/definitions/" + name + "Events"}

all_events = set()
for name, event_set in events.items():
    all_events.update(event_set)
for name, events in events.items():
    if events:
        schema["definitions"][name + "Events"] = {
            "type": "object",
            "properties": {event: {"type": "function"} for event in events},
            "additionalProperties": False,
        }

        # extra = events - all_events
        # if extra:
        #     print(name, "has extra events", extra)
        # missing = all_events - events
        # if missing:
        #     print(name, "is missing events", missing)

del schema["definitions"]["ReactNode"]
schema_file_polished = HERE / "schema-polished.json"
with open(schema_file_polished, "w") as f:
    json.dump(schema, f, indent=2)

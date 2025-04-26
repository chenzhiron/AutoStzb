def def_label_checkbox(component):
    for v in component.spec["input"]["options"]:
        v["label"] = ""
    return component

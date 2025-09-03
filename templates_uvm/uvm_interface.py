def clean_name(raw_name):
    keywords_to_strip = {"input", "output", "inout", "logic", "wire", "reg", "bit"}
    tokens = raw_name.split()
    clean_tokens = [t for t in tokens if t not in keywords_to_strip]
    return " ".join(clean_tokens)

def generate_interface(module_name, signals, parameters=None):
    interface_name = f"{module_name}_if"

    param_block = ""
    if parameters:
        param_lines = []
        for k, v in parameters.items():
            if v is None:
                param_lines.append(f"  parameter int {k}")
            else:
                param_lines.append(f"  parameter int {k} = {v}")
        param_block = "#(\n" + ",\n".join(param_lines) + "\n)"

    port_lines = []
    for sig in signals:
        direction = sig["dir"]
        width = sig["width"]
        raw_name = sig["name"]
        name = clean_name(raw_name)

        if width:
            port_lines.append(f"  {direction} {width} {name}")
        else:
            port_lines.append(f"  {direction} {name}")
    port_block = "(\n" + ",\n".join(port_lines) + "\n);"

    interface_code = f"""interface {interface_name} {param_block} {port_block}

endinterface
"""
    return interface_code

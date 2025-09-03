import re
from signal_parser.signal_extractor import extract_signals_from_text, extract_parameters_from_text
from templates_uvm.uvm_interface import generate_interface

def parse_interfaces_from_file(filepath: str):
    with open(filepath, 'r') as f:
        content = f.read()

    # Remove comments
    content = re.sub(r"//.*?$|/\*.*?\*/", "", content, flags=re.DOTALL | re.MULTILINE)

    # Match blocks like: alu_if #(...) ( ... );
    interface_re = re.compile(
        r"(?P<name>\w+)_if\s*(#\((?P<params>.*?)\))?\s*\((?P<ports>.*?)\);",
        re.DOTALL | re.MULTILINE
    )

    interfaces = []

    for match in interface_re.finditer(content):
        base_name   = match.group("name")
        raw_params  = match.group("params") or ""
        raw_ports   = match.group("ports") or ""

        # Extract from text blocks
        params  = extract_parameters_from_text(raw_params)
        signals = extract_signals_from_text(raw_ports)

        # Generate interface
        interface_code = generate_interface(base_name, signals, params)

        # Append full info for downstream use (like seq_item generation)
        interfaces.append({
            "name": f"{base_name}",
            "parameters": params,
            "signals": signals,
            "interface_code": interface_code,
            "raw_params": raw_params,
            "raw_ports": raw_ports
        })

    return interfaces

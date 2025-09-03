import re
from typing import List, Dict


def extract_signals_from_text(content: str) -> List[Dict]:
    signals = []

    # Remove comments
    content = re.sub(r"//.*?$|/\*.*?\*/", "", content, flags=re.DOTALL | re.MULTILINE)

    # Flatten and strip port block
    content = content.replace('\n', ' ').replace('\r', '')
    content = content.strip().lstrip('(').rstrip(')').rstrip(';')

    # Split by comma
    entries = [e.strip() for e in content.split(',') if e.strip()]

    for entry in entries:
        # Match: direction (ignored), optional logic, optional width, name
        match = re.match(r"(input|output|inout)?\s*(logic\s+)?(\[[^\]]+\]\s+)?(\w+)", entry)
        if match:
            width = match.group(3).strip() if match.group(3) else ""
            name = match.group(4).strip()

            # FORCE direction to 'input'
            signals.append({
                "dir": "input",
                "width": width,
                "name": name
            })

    return signals

def extract_parameters_from_text(param_block: str) -> Dict:
    params = {}
    param_block = re.sub(r"//.*?$|/\*.*?\*/", "", param_block, flags=re.DOTALL | re.MULTILINE)

    param_regex = re.compile(
        r'(localparam|parameter|param)\s+(?:\w+\s+)?(?P<name>\w+)\s*(?:=\s*(?P<value>[^,;]+))?\s*[;,]?'
    )

    for match in param_regex.finditer(param_block):
        name = match.group("name")
        value = match.group("value")
        if name:
            name = name.strip()
            if value is not None:
                params[name] = value.strip()
            else:
                params[name] = None

    return params

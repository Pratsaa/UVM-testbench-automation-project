import os
import re

def extract_design_file_name(filepath: str) -> str:
    with open(filepath, 'r') as f:
        content = f.read()

    match = re.search(r'//\s*Please insert the name of the design file:\s*(\S+)', content)
    if match:
        return match.group(1).replace(".sv", "")
    else:
        raise ValueError("Design file name comment not found.")


def generate_combined_harness_file(interfaces, module_name, design_template_path, output_path):
    dut_instance = extract_design_file_name(design_template_path)
    harness_name = f"{module_name}_harness"
    guard = harness_name.upper()

    harness_lines = [
        f"`ifndef {guard}_SV",
        f"`define {guard}_SV",
        "",
        f"interface {harness_name}();",
        "",
        "  import uvm_pkg::*;",
        "  `include \"uvm_macros.svh\"",
        ""
    ]

    # Interface instantiations with signal mappings
    for iface in interfaces:
        iface_name_raw = iface["name"]
        iface_name = iface_name_raw if iface_name_raw.endswith("_if") else iface_name_raw + "_if"
        inst_name = f"{iface_name}_inst"

        conn_lines = [
            f"    .{sig['name']} ({dut_instance}.{sig['name']})"
            for sig in iface["signals"]
        ]
        connection_block = ",\n".join(conn_lines)
        harness_lines.append(f"  {iface_name} {inst_name} (\n{connection_block}\n  );\n")

    # Individual set_vif functions per interface
    for iface in interfaces:
        iface_name = iface["name"]
        iface_name_mod = iface_name if iface_name.endswith("_if") else iface_name + "_if"
        inst_name = f"{iface_name}_if_inst"
        func_name = f"set_{iface_name}_vif"

        harness_lines.append(f"  function void {func_name}(string path);")
        harness_lines.append(
            f"    uvm_config_db#(virtual {iface_name_mod})::set(null, path, \"{iface_name_mod}\", {inst_name});"
        )
        harness_lines.append("  endfunction\n")

    harness_lines.append(f"endinterface: {harness_name}\n")

    # Single bind statement
    harness_lines.append(f"bind {dut_instance} {harness_name} {harness_name}_inst();")
    harness_lines.append("")
    harness_lines.append(f"`endif")

    # Write to file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write("\n".join(harness_lines))

    print(f"[Generated] {output_path}")

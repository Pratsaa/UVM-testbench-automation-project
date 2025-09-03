import argparse
import os
from templates_uvm.uvm_driver import generate_driver
from templates_uvm.uvm_monitor import generate_monitor
from templates_uvm.uvm_interface import generate_interface
from signal_parser.signal_extractor import extract_signals_from_text, extract_parameters_from_text
from multi_interface_parser import parse_interfaces_from_file
from templates_uvm.uvm_env import generate_env_file
from templates_uvm.uvm_harness import generate_combined_harness_file
from templates_uvm.uvm_tb_top import generate_tb_top_sv
from templates_uvm.uvm_tb_pkg import generate_tb_pkg_sv
from templates_uvm.uvm_scoreboard import generate_scoreboard_sv
from templates_uvm.uvm_test import generate_test_sv
from templates_uvm.uvm_basic_seq import generate_basic_seq_sv
from templates_uvm.verifF_template import generate_verif_f
from templates_uvm.Makefile_template import generate_makefile
from templates_uvm.designF_template import generate_design_f
from templates_uvm.uvm_harness import extract_design_file_name

def parse_args():
    parser = argparse.ArgumentParser(
        description="UVM Testbench Generator CLI"
    )

    parser.add_argument(
        "-m", "--module", required=True,
        help="Top-level design module name (e.g., async_fifo)"
    )

    parser.add_argument(
        "-o", "--outdir", default=".",
        help="Output directory for generated testbench (default: current directory)"
    )

    parser.add_argument(
        "--design", help="Path to RTL design file to extract interface signals from"
    )

    parser.add_argument(
        "--interface", action="store_true",
        help="Generate UVM interfaces from a multi-interface input file"
    )

    return parser.parse_args()

def write_agent_interface_files(interfaces, outdir):
    for iface in interfaces:
        iface_name = iface["name"]  # e.g. alu_if
        agent_dir = os.path.join(outdir, f"{iface_name}_agent")
        os.makedirs(agent_dir, exist_ok=True)

        sv_filename = f"{iface_name}.sv"
        sv_filepath = os.path.join(agent_dir, sv_filename)

        with open(sv_filepath, "w") as f:
            f.write(iface["interface_code"])

        print(f"[Generated] {sv_filepath}")

def write_sv_file(outdir, module_name, role, content, override_filename=None):
    """
    Writes SystemVerilog content to a file with naming convention: <module_name>_<role>.sv
    or override with custom file name if provided.
    """
    module_dir = os.path.join(outdir, module_name)
    os.makedirs(module_dir, exist_ok=True)

    filename = override_filename if override_filename else f"{module_name}_{role}.sv"
    filepath = os.path.join(module_dir, filename)

    with open(filepath, "w") as f:
        f.write(content)

    print(f"[Generated] {filepath}")

def generate_files(module_name, outdir, design_path=None, gen_interface=False):
    if not gen_interface:
        return

    if not design_path:
        print("[ERROR] --interface was requested but no --design file was provided.")
        return

    print(f"[INFO] Parsing all interfaces from: {design_path}")
    interfaces = parse_interfaces_from_file(design_path)

    if not interfaces:
        print("[WARN] No interfaces found in design file.")
        return

    # Setup directory structure
    tb_root = os.path.join(outdir, module_name)
    module_folder = os.path.join(tb_root, "tb")
    tests_dir = os.path.join(tb_root, "tests")
    sim_dir = os.path.join(tb_root, "sim")

    os.makedirs(module_folder, exist_ok=True)
    os.makedirs(tests_dir, exist_ok=True)
    os.makedirs(sim_dir, exist_ok=True)

    interface_names = []

    for iface in interfaces:
        iface_name = iface["name"]
        agent_folder = os.path.join(module_folder, f"{iface_name}_agent")
        os.makedirs(agent_folder, exist_ok=True)

        # Write interface file
        filename = f"{iface_name}_if.sv"
        filepath = os.path.join(agent_folder, filename)
        with open(filepath, "w") as f:
            f.write(iface["interface_code"])
        print(f"[Generated] {filepath}")

        # Agent components
        generate_agent_file(iface_name, agent_folder)
        generate_driver_file(iface_name, agent_folder)
        generate_monitor_file(iface_name, agent_folder)
        generate_agent_pkg_files(iface_name, agent_folder)

        # Sequence item
        template_path = "templates_uvm/uvm_seq_item.sv"
        seq_item_path = os.path.join(agent_folder, f"{iface_name}_seq_item.sv")
        generate_seq_item_from_template_using_extractor(
            raw_params=iface["raw_params"],
            raw_ports=iface["raw_ports"],
            name=iface_name,
            template_path=template_path,
            output_path=seq_item_path
        )

        interface_names.append(iface_name)

    # Harness
    combined_harness_path = os.path.join(module_folder, f"{module_name}_harness.sv")
    generate_combined_harness_file(
        interfaces=interfaces,
        module_name=module_name,
        design_template_path=design_path,
        output_path=combined_harness_path
    )

    # Environment
    env_code = generate_env_file(module_name, interface_names)
    env_path = os.path.join(module_folder, f"{module_name}_env.sv")
    with open(env_path, "w") as f:
        f.write(env_code)
    print(f"[Generated] {env_path}")

    # tb_top
    try:
        design_file_name = extract_design_file_name(design_path)
    except ValueError as e:
            print(f"[ERROR] {e}")
            design_file_name = os.path.splitext(os.path.basename(design_path))[0]  # fallback

    tb_top_code = generate_tb_top_sv(
        module_name=module_name,
        design_file_name=design_file_name,
        agent_list=interface_names
    )

    tb_top_path = os.path.join(module_folder, "tb_top.sv")
    with open(tb_top_path, "w") as f:
        f.write(tb_top_code)
    print(f"[Generated] {tb_top_path}")

    # tb_pkg
    tb_pkg_code = generate_tb_pkg_sv(module_name, interface_names)
    tb_pkg_path = os.path.join(module_folder, "tb_pkg.sv")
    with open(tb_pkg_path, "w") as f:
        f.write(tb_pkg_code)
    print(f"[Generated] {tb_pkg_path}")

    # Scoreboard
    scoreboard_code = generate_scoreboard_sv(module_name, interface_names)
    scoreboard_path = os.path.join(module_folder, f"{module_name}_scoreboard.sv")
    with open(scoreboard_path, "w") as f:
        f.write(scoreboard_code)
    print(f"[Generated] {scoreboard_path}")

    # Test file
    generate_test_file(module_name, interfaces, tests_dir)

    # Basic sequence file
    first_iface = interface_names[0] if interface_names else module_name
    generate_basic_seq_file(module_name, first_iface, tests_dir)

    print(f"[Created] Simulation folder: {sim_dir}")

     # Write verif.F to <outdir>/<module_name>/tb/
    generate_verif_f(module_name, interface_names, os.path.join(outdir, module_name))

    # Generate Makefile in sim directory
    generate_makefile_file(outdir, module_name)

    # Write design.F to <outdir>/<module_name>/tb/\
    write_design_f_file(outdir, module_name)



def generate_agent_file(interface_name, output_dir):
    template_path = "templates_uvm/uvm_agent.sv"
    with open(template_path, "r") as f:
        template = f.read()

    code = template.format(name=interface_name, name_upper=interface_name.upper())

    agent_path = os.path.join(output_dir, f"{interface_name}_agent.sv")
    with open(agent_path, "w") as f:
        f.write(code)

    print(f"[Generated] {agent_path}")

def generate_driver_file(interface_name, output_dir):
    template_path = "templates_uvm/uvm_driver.sv"
    with open(template_path, "r") as f:
        template = f.read()

    code = template.format(name=interface_name, name_upper=interface_name.upper())

    driver_path = os.path.join(output_dir, f"{interface_name}_driver.sv")
    with open(driver_path, "w") as f:
        f.write(code)

    print(f"[Generated] {driver_path}")

def generate_monitor_file(interface_name, output_dir):
    template_path = "templates_uvm/uvm_monitor.sv"
    with open(template_path, "r") as f:
        template = f.read()

    code = template.format(name=interface_name, name_upper=interface_name.upper())

    monitor_path = os.path.join(output_dir, f"{interface_name}_monitor.sv")
    with open(monitor_path, "w") as f:
        f.write(code)

    print(f"[Generated] {monitor_path}")

def generate_seq_item_from_template_using_extractor(raw_params, raw_ports, name, template_path, output_path):
    # Step 1: Extract using your own utilities
    param_dict = extract_parameters_from_text(raw_params)
    signals = extract_signals_from_text(raw_ports)

    # Step 2: Load template
    with open(template_path, "r") as f:
        template = f.read()

    # Step 3: Format parameters
    param_lines = []
    for pname, pval in param_dict.items():
        if pval:
            param_lines.append(f"  localparam int {pname} = {pval};")
        else:
            param_lines.append(f"  localparam int {pname};")
    param_block = "\n".join(param_lines) if param_lines else "  // No parameters"

    # Step 4: Format signals + uvm fields
    signal_lines = []
    uvm_fields = []
    for sig in signals:
        width = f"{sig['width']} " if sig['width'] else ""
        sig_name = sig['name']
        signal_lines.append(f"  logic {width}{sig_name};")
        uvm_fields.append(f"  `uvm_field_int({sig_name}, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)")

    # Step 5: Fill template
    content = template.format(
        name=name,
        name_upper=name.upper(),
        param_lines=param_block,
        signal_lines="\n".join(signal_lines),
        uvm_fields="\n".join(uvm_fields)
    )

    with open(output_path, "w") as f:
        f.write(content)

    print(f"[Generated] {output_path}")

def generate_agent_pkg_files(interface_name, output_dir):
    template_path = "templates_uvm/uvm_agent_pkg.sv"
    with open(template_path, "r") as f:
        template = f.read()

    code = template.format(name=interface_name, name_upper=interface_name.upper())

    pkg_path = os.path.join(output_dir, f"{interface_name}_agent_pkg.sv")
    with open(pkg_path, "w") as f:
        f.write(code)

    print(f"[Generated] {pkg_path}")

def generate_test_file(module_name, interfaces, outdir):
    """
    Generate a UVM test file for the given module name.
    """
    test_code = generate_test_sv(module_name, interfaces)
    test_path = os.path.join(outdir, f"{module_name}_test.sv")
    
    with open(test_path, "w") as f:
        f.write(test_code)

    print(f"[Generated] {test_path}")

def generate_makefile_file(outdir, module_name):
    """
    Generate a Makefile in tb/sim/ folder under <outdir>/<module_name>/sim/
    """
    sim_dir = os.path.join(outdir, module_name, "sim")
    os.makedirs(sim_dir, exist_ok=True)
    
    makefile_content = generate_makefile(module_name)

    makefile_path = os.path.join(sim_dir, "Makefile")
    with open(makefile_path, "w") as f:
        f.write(makefile_content)

    print(f"[Generated] {makefile_path}")

def write_design_f_file(outdir, module_name):
    """
    Generate design.F in the <outdir>/<module_name>/tb/ directory.
    """
    tb_dir = os.path.join(outdir, module_name, "tb")
    os.makedirs(tb_dir, exist_ok=True)

    design_f_content = generate_design_f()
    design_f_path = os.path.join(tb_dir, "design.F")

    with open(design_f_path, "w") as f:
        f.write(design_f_content)

    print(f"[Generated] {design_f_path}")


def generate_basic_seq_file(module_name, first_interface, outdir):
    """
    Generate a basic sequence file using the first interface's sequence item.
    """
    basic_seq_code = generate_basic_seq_sv(module_name, first_interface)
    basic_seq_path = os.path.join(outdir, f"{module_name}_basic_seq.sv")

    with open(basic_seq_path, "w") as f:
        f.write(basic_seq_code)

    print(f"[Generated] {basic_seq_path}")

def main():
    args = parse_args()

    module_name = args.module
    outdir = os.path.abspath(args.outdir)
    design_path = args.design
    gen_interface = args.interface

    print(f"\nModule name      : {module_name}")
    print(f"Output directory : {outdir}")
    if gen_interface:
        print(f"Generating UVM interface(s) from: {design_path}")

    generate_files(module_name, outdir, design_path, gen_interface)

if __name__ == "__main__":
    main()

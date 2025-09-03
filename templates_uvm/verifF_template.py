import os

def generate_verif_f(module_name: str, agent_list: list, module_root: str):
    """
    Generate verif.F inside <module_root>/tb/, dynamically adding agent paths.
    
    Args:
        module_name: Name of top module (e.g., async_fifo)
        agent_list: List of agents like ["alu_if", "dma_if", "uart_if"]
        module_root: Path to <outdir>/<module_name>
    """
    tb_dir = os.path.join(module_root, "tb")
    os.makedirs(tb_dir, exist_ok=True)

    verif_f_path = os.path.join(tb_dir, "verif.F")
    lines = []

    # Fixed include dirs
    lines.extend([
        "+incdir+../../../../../common/vip/clock_controller",
        "+incdir+../../../../../common/vip/misc",
        "+incdir+../../tb",
    ])

    # Add +incdir for each agent
    for agent in agent_list:
        lines.append(f"+incdir+../../tb/{agent}_agent")

    # Static includes
    lines.extend([
        "+incdir+../../tests",
        "+define++UVM_PACKER_MAX_BYTES=10000",
        "+define+UVM_DISABLE_AUTO_ITEM_RECORDING",
        "+incdir+${VCS_HOME}/etc/uvm-ieee-2020/vcs",
        "+incdir+../../../../common/ip/dl_misc/rtl",
        "+incdir+../../../../common/ip/dl_fifo/rtl",
        "//Add directories to the relevant files over here",
        "",
        "-y ../../../../common/ip/dl_misc/rtl",
        "-y ../../../../common/ip/dl_fifo/rtl",
        "//Add directories to the relevant files over here",
        "",
        "+incdir+../../../../common/vip/src/",
        "-y ../../../../common/vip/src/",
        "+incdir+../../tests/dl_async_fifo_ft_test",
        "+incdir+${VCS_HOME}/etc/uvm-ieee-2020/vcs",
        "+incdir+${VCS_HOME}/etc/uvm-ieee-2020/verdi",
        "-y ../../tests",
        "-y ../../../../common/vip/",
        "",
        "${VCS_HOME}/etc/uvm-ieee-2020/uvm_pkg.sv",
        "${VCS_HOME}/etc/uvm-ieee-2020/vcs/uvm_custom_install_vcs_recorder.sv",
        "${VCS_HOME}/etc/uvm-ieee-2020/verdi/uvm_custom_install_verdi_recorder.sv",
        ""
    ])

    # Add all agent interface files and pkg files
    for agent in agent_list:
        lines.append(f"../../tb/{agent}_agent/{agent}_if.sv")
    lines.append("//../../../../../common/vip/misc/clk_if.sv")
    for agent in agent_list:
        lines.append(f"../../tb/{agent}_agent/{agent}_agent_pkg.sv")

    # Final main files
    lines.extend([
        "../../tb/tb_pkg.sv",
        "../../tb/tb_top.sv",
        f"../../tb/{module_name}_harness.sv"
    ])

    with open(verif_f_path, "w") as f:
        f.write("\n".join(lines))

    print(f"[Generated] {verif_f_path}")

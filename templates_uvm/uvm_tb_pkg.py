def generate_tb_pkg_sv(module_name: str, agent_list: list) -> str:
    """
    Generate tb_pkg.sv dynamically based on module name and agents.

    Args:
        module_name (str): e.g., "async_fifo"
        agent_list (list): e.g., ["uart_if", "dma_if"]
    """
    # Generate agent import lines
    agent_imports = "\n    ".join(
        f"import {agent}_agent_pkg::*;" for agent in agent_list
    )

    return f'''\
`ifndef TB_PKG_SV
`define TB_PKG_SV

package tb_pkg;

    import uvm_pkg::*;
    {agent_imports}

    `include "uvm_macros.svh"
    //`include "clock_controller.sv"

    // Checkers
    `include "{module_name}_scoreboard.sv"

    // ENV
    `include "{module_name}_env.sv"

    // Sequences
    `include "{module_name}_basic_seq.sv"

    // Tests
    `include "{module_name}_test.sv"

endpackage: tb_pkg
`endif
'''

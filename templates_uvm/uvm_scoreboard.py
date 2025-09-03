def generate_scoreboard_sv(module_name: str, agent_list: list) -> str:
    """
    Generates a compile-clean UVM scoreboard with write() methods for each agent's seq_item.

    Args:
        module_name (str): Testbench name (e.g., pratyush2test)
        agent_list (list): List of agent base names (e.g., ["alu_if", "dma_if", "uart_if"])
    """
    # Header with guard and class definition
    header = f"""\
`ifndef {module_name.upper()}_SCOREBOARD_SV
`define {module_name.upper()}_SCOREBOARD_SV

class {module_name}_scoreboard extends uvm_scoreboard;
  `uvm_component_utils({module_name}_scoreboard)

"""

    # Declare uvm_analysis_imp for each agent
    export_decls = ""
    for agent in agent_list:
        export_decls += f"  uvm_analysis_imp #({agent}_seq_item, {module_name}_scoreboard) {agent}_export;\n"

    # Constructor
    constructor = f"""
  function new(string name = "{module_name}_scoreboard", uvm_component parent = null);
    super.new(name, parent);
  endfunction
"""

    # Build phase with export creation
    build_phase = """
  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
"""
    for agent in agent_list:
        build_phase += f'    {agent}_export = new("{agent}_export", this);\n'
    build_phase += "  endfunction\n"

    # Write functions
    write_funcs = ""
    for agent in agent_list:
        write_funcs += f"""
  virtual function void write_{agent}({agent}_seq_item t);
    `uvm_info("SCOREBOARD", $sformatf("Received {agent} transaction: %s", t.convert2string()), UVM_LOW)
    // TODO: Add checking logic here
  endfunction
"""

    # Footer
    footer = f"""
endclass

`endif
"""

    return "/*\n" + header + export_decls + constructor + build_phase + write_funcs + footer + "*/\n"

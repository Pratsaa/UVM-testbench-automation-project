def generate_monitor(module_name):
    upper_name = module_name.upper()
    return f"""\
`ifndef {upper_name}_DRIVER_SV
`define {upper_name}_DRIVER_SV

class {module_name}_monitor extends uvm_monitor
  `uvm_component_utils({module_name}_monitor)

  function new(string name, uvm_component parent);
    super.new(name, parent);
  endfunction

  task run_phase(uvm_phase  phase);
  forever begin
    // TODO: Implement {module_name} monitor behavior
  end
  endtask

endclass

`endif
"""
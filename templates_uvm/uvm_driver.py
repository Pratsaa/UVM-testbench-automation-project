def generate_driver(module_name):
    upper_name = module_name.upper()
    return f"""\
`ifndef {upper_name}_DRIVER_SV
`define {upper_name}_DRIVER_SV

class {module_name}_driver extends uvm_driver
  `uvm_component_utils({module_name}_driver)

  function new(string name, uvm_component parent);
    super.new(name, parent);
  endfunction

  task run_phase(uvm_phase phase);
    // TODO: Implement {module_name} driver behavior
  endtask

endclass

`endif
"""
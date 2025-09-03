def generate_basic_seq_sv(module_name: str, interface_base: str) -> str:
    upper = module_name.upper()
    return f'''\
`ifndef {upper}_BASIC_SEQ
`define {upper}_BASIC_SEQ

class {module_name}_basic_seq extends uvm_sequence;
  `uvm_object_utils({module_name}_basic_seq)

  {interface_base}_seq_item req;

  function new(string name = "{module_name}_basic_seq");
    super.new(name);
  endfunction

  task body();
    `uvm_info(get_type_name(), "starting basic sequence ...", UVM_LOW)
    req = {interface_base}_seq_item::type_id::create("req");
    start_item(req);
    assert(req.randomize());
    finish_item(req);
  endtask

endclass

`endif
'''

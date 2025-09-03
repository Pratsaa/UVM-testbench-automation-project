`ifndef {name_upper}_SEQ_ITEM_SV
`define {name_upper}_SEQ_ITEM_SV

class {name}_seq_item extends uvm_sequence_item;

  // Parameters
{param_lines}

  // Signals
{signal_lines}

  // UVM Macros
  `uvm_object_utils_begin({name}_seq_item)
{uvm_fields}
  `uvm_object_utils_end

  function new(string name = "{name}_seq_item");
    super.new(name);
  endfunction : new

endclass : {name}_seq_item

`endif

`ifndef FINALTEST1_BASIC_SEQ
`define FINALTEST1_BASIC_SEQ

class finaltest1_basic_seq extends uvm_sequence;
  `uvm_object_utils(finaltest1_basic_seq)

  alu_seq_item req;

  function new(string name = "finaltest1_basic_seq");
    super.new(name);
  endfunction

  task body();
    `uvm_info(get_type_name(), "starting basic sequence ...", UVM_LOW)
    req = alu_seq_item::type_id::create("req");
    start_item(req);
    assert(req.randomize());
    finish_item(req);
  endtask

endclass

`endif

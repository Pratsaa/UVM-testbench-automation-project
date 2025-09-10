`ifndef ALU_SEQ_ITEM_SV
`define ALU_SEQ_ITEM_SV

class alu_seq_item extends uvm_sequence_item;

  // Parameters
  localparam int WIDTH = 32;
  localparam int SIGNED_OP = 1;

  // Signals
  logic clk;
  logic rst_n;
  logic [WIDTH-1:0] a;
  logic [WIDTH-1:0] b;
  logic [2:0] op;
  logic [WIDTH-1:0] result;
  logic valid;

  // UVM Macros
  `uvm_object_utils_begin(alu_seq_item)
  `uvm_field_int(clk, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(rst_n, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(a, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(b, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(op, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(result, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(valid, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_object_utils_end

  function new(string name = "alu_seq_item");
    super.new(name);
  endfunction : new

endclass : alu_seq_item

`endif

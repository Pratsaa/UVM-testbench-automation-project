`ifndef UART_SEQ_ITEM_SV
`define UART_SEQ_ITEM_SV

class uart_seq_item extends uvm_sequence_item;

  // Parameters
  // No parameters

  // Signals
  logic clk;
  logic reset;
  logic tx_start;
  logic tx_ready;
  logic [7:0] tx_data;
  logic tx_line;

  // UVM Macros
  `uvm_object_utils_begin(uart_seq_item)
  `uvm_field_int(clk, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(reset, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(tx_start, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(tx_ready, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(tx_data, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(tx_line, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_object_utils_end

  function new(string name = "uart_seq_item");
    super.new(name);
  endfunction : new

endclass : uart_seq_item

`endif

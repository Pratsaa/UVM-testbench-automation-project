`ifndef DMA_SEQ_ITEM_SV
`define DMA_SEQ_ITEM_SV

class dma_seq_item extends uvm_sequence_item;

  // Parameters
  localparam int ADDR_WIDTH = 16;

  // Signals
  logic start;
  logic done;
  logic [ADDR_WIDTH-1:0] src_addr;
  logic [ADDR_WIDTH-1:0] dest_addr;
  logic busy;

  // UVM Macros
  `uvm_object_utils_begin(dma_seq_item)
  `uvm_field_int(start, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(done, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(src_addr, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(dest_addr, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_field_int(busy, UVM_ALL_ON | UVM_NOCOMPARE | UVM_NOPACK)
  `uvm_object_utils_end

  function new(string name = "dma_seq_item");
    super.new(name);
  endfunction : new

endclass : dma_seq_item

`endif

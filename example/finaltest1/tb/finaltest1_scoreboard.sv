/*
`ifndef FINALTEST1_SCOREBOARD_SV
`define FINALTEST1_SCOREBOARD_SV

class finaltest1_scoreboard extends uvm_scoreboard;
  `uvm_component_utils(finaltest1_scoreboard)

  uvm_analysis_imp #(alu_seq_item, finaltest1_scoreboard) alu_export;
  uvm_analysis_imp #(dma_seq_item, finaltest1_scoreboard) dma_export;
  uvm_analysis_imp #(uart_seq_item, finaltest1_scoreboard) uart_export;

  function new(string name = "finaltest1_scoreboard", uvm_component parent = null);
    super.new(name, parent);
  endfunction

  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    alu_export = new("alu_export", this);
    dma_export = new("dma_export", this);
    uart_export = new("uart_export", this);
  endfunction

  virtual function void write_alu(alu_seq_item t);
    `uvm_info("SCOREBOARD", $sformatf("Received alu transaction: %s", t.convert2string()), UVM_LOW)
    // TODO: Add checking logic here
  endfunction

  virtual function void write_dma(dma_seq_item t);
    `uvm_info("SCOREBOARD", $sformatf("Received dma transaction: %s", t.convert2string()), UVM_LOW)
    // TODO: Add checking logic here
  endfunction

  virtual function void write_uart(uart_seq_item t);
    `uvm_info("SCOREBOARD", $sformatf("Received uart transaction: %s", t.convert2string()), UVM_LOW)
    // TODO: Add checking logic here
  endfunction

endclass

`endif
*/

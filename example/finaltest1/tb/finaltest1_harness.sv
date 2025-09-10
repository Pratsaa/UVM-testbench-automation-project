`ifndef FINALTEST1_HARNESS_SV
`define FINALTEST1_HARNESS_SV

interface finaltest1_harness();

  import uvm_pkg::*;
  `include "uvm_macros.svh"

  alu_if alu_if_inst (
    .clk (stub_dut.clk),
    .rst_n (stub_dut.rst_n),
    .a (stub_dut.a),
    .b (stub_dut.b),
    .op (stub_dut.op),
    .result (stub_dut.result),
    .valid (stub_dut.valid)
  );

  dma_if dma_if_inst (
    .start (stub_dut.start),
    .done (stub_dut.done),
    .src_addr (stub_dut.src_addr),
    .dest_addr (stub_dut.dest_addr),
    .busy (stub_dut.busy)
  );

  uart_if uart_if_inst (
    .clk (stub_dut.clk),
    .reset (stub_dut.reset),
    .tx_start (stub_dut.tx_start),
    .tx_ready (stub_dut.tx_ready),
    .tx_data (stub_dut.tx_data),
    .tx_line (stub_dut.tx_line)
  );

  function void set_alu_vif(string path);
    uvm_config_db#(virtual alu_if)::set(null, path, "alu_if", alu_if_inst);
  endfunction

  function void set_dma_vif(string path);
    uvm_config_db#(virtual dma_if)::set(null, path, "dma_if", dma_if_inst);
  endfunction

  function void set_uart_vif(string path);
    uvm_config_db#(virtual uart_if)::set(null, path, "uart_if", uart_if_inst);
  endfunction

endinterface: finaltest1_harness

bind stub_dut finaltest1_harness finaltest1_harness_inst();

`endif
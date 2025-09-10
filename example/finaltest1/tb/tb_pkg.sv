`ifndef TB_PKG_SV
`define TB_PKG_SV

package tb_pkg;

    import uvm_pkg::*;
    import alu_agent_pkg::*;
    import dma_agent_pkg::*;
    import uart_agent_pkg::*;

    `include "uvm_macros.svh"
    //`include "clock_controller.sv"

    // Checkers
    `include "finaltest1_scoreboard.sv"

    // ENV
    `include "finaltest1_env.sv"

    // Sequences
    `include "finaltest1_basic_seq.sv"

    // Tests
    `include "finaltest1_test.sv"

endpackage: tb_pkg
`endif

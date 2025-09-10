module tb_top ();

  // Set timescale
  timeunit 1ns;
  timeprecision 100ps;

  // Import UVM and your testbench package
  import uvm_pkg::*;
  `include "uvm_macros.svh"
  import tb_pkg::*;

  // Add the Top-level signals


  // Add any internal signals over here 

  // Enable waveform dump if "vpd" is passed as an argument
  initial begin
    if ($test$plusargs("vpd")) begin
      $vcdplusfile("vcdplus.vpd");
      $vcdpluson(0, tb_top);
    end
  end

  // Set time format
  initial begin
    $timeformat(-9, 1, " ns", 9);
  end

  // Run test
  initial begin
    $timeformat(-9, 3, " ns");
    uvm_root::get().set_finish_on_completion(1);
    uvm_root::get().set_timeout(1s);
    run_test("finaltest1_test");
  end

  //---------------------------------------------------------------------------
  // Instantiate DUT (Design Under Test)
  //---------------------------------------------------------------------------
  stub_dut dut (
    // Add any signals if necessary here
  );

  //---------------------------------------------------------------------------
  // Set virtual interface using the function in the bound harness
  //---------------------------------------------------------------------------
  initial begin
    // #1; // Optional delay for elaboration
    //dut.async_fifo_harness_inst.set_clk1_if("uvm_test_top.env_m");
    //dut.async_fifo_harness_inst.set_clk2_if("uvm_test_top.env_m");

    `uvm_info("TB_TOP", "Setting virtual interface for alu_agent.", UVM_LOW)
    dut.finaltest1_harness_inst.set_alu_vif("uvm_test_top.m_env.m_alu_agent*");
    `uvm_info("TB_TOP", "Setting virtual interface for dma_agent.", UVM_LOW)
    dut.finaltest1_harness_inst.set_dma_vif("uvm_test_top.m_env.m_dma_agent*");
    `uvm_info("TB_TOP", "Setting virtual interface for uart_agent.", UVM_LOW)
    dut.finaltest1_harness_inst.set_uart_vif("uvm_test_top.m_env.m_uart_agent*");
  end

endmodule

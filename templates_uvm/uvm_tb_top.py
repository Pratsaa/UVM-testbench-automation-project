def generate_tb_top_sv(module_name: str, design_file_name: str, agent_list: list) -> str:
    """
    Generate tb_top.sv with dynamic virtual interface assignments for multiple agents.

    Args:
        module_name (str): Name prefix for testbench module (e.g., "async_fifo")
        design_file_name (str): DUT module name (e.g., "dl_async_fifo_ft_wrapper")
        agent_list (list): List of agent base names (e.g., ["uart", "dma", "alu"])
    """
    
    # Generate per-agent set_vif calls
    vif_assignments = "\n".join(
        f'''    `uvm_info("TB_TOP", "Setting virtual interface for {agent}_agent.", UVM_LOW)
    dut.{module_name}_harness_inst.set_{agent}_vif("uvm_test_top.m_env.m_{agent}_agent*");'''
        for agent in agent_list
    )

    return f'''\
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
    run_test("{module_name}_test");
  end

  //---------------------------------------------------------------------------
  // Instantiate DUT (Design Under Test)
  //---------------------------------------------------------------------------
  {design_file_name} dut (
    // Add any signals if necessary here
  );

  //---------------------------------------------------------------------------
  // Set virtual interface using the function in the bound harness
  //---------------------------------------------------------------------------
  initial begin
    // #1; // Optional delay for elaboration
    //dut.async_fifo_harness_inst.set_clk1_if("uvm_test_top.env_m");
    //dut.async_fifo_harness_inst.set_clk2_if("uvm_test_top.env_m");

{vif_assignments}
  end

endmodule
'''

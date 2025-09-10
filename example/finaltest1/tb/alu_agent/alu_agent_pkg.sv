`ifndef ALU_AGENT_PKG_SV
`define ALU_AGENT_PKG_SV
//`include "alu_if.sv"
package alu_agent_pkg;
import uvm_pkg::*;
`include "uvm_macros.svh" 

`include "alu_seq_item.sv"
//add test sequences here 
`include "alu_driver.sv"
`include "alu_monitor.sv"
`include "alu_agent.sv"

endpackage
`endif
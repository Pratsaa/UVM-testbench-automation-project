`ifndef {name_upper}_AGENT_PKG_SV
`define {name_upper}_AGENT_PKG_SV
//`include "{name}_if.sv"
package {name}_agent_pkg;
import uvm_pkg::*;
`include "uvm_macros.svh" 

`include "{name}_seq_item.sv"
//add test sequences here 
`include "{name}_driver.sv"
`include "{name}_monitor.sv"
`include "{name}_agent.sv"

endpackage
`endif
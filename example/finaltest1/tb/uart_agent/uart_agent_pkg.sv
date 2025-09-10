`ifndef UART_AGENT_PKG_SV
`define UART_AGENT_PKG_SV
//`include "uart_if.sv"
package uart_agent_pkg;
import uvm_pkg::*;
`include "uvm_macros.svh" 

`include "uart_seq_item.sv"
//add test sequences here 
`include "uart_driver.sv"
`include "uart_monitor.sv"
`include "uart_agent.sv"

endpackage
`endif
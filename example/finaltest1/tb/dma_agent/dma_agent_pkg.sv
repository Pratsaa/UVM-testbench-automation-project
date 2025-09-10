`ifndef DMA_AGENT_PKG_SV
`define DMA_AGENT_PKG_SV
//`include "dma_if.sv"
package dma_agent_pkg;
import uvm_pkg::*;
`include "uvm_macros.svh" 

`include "dma_seq_item.sv"
//add test sequences here 
`include "dma_driver.sv"
`include "dma_monitor.sv"
`include "dma_agent.sv"

endpackage
`endif
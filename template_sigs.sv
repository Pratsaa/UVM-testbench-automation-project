alu_if #(
  parameter WIDTH = 32,
  parameter SIGNED_OP = 1
)
(
  input logic clk,
  input logic rst_n,
  input logic [WIDTH-1:0] a,
  input logic [WIDTH-1:0] b,
  input logic [2:0] op,
  output logic [WIDTH-1:0] result,
  output logic valid
);

dma_if #(
  param ADDR_WIDTH = 16
)
(
  input logic start,
  output logic done,
  input logic [ADDR_WIDTH-1:0] src_addr,
  input logic [ADDR_WIDTH-1:0] dest_addr,
  output logic busy
);

uart_if (
  input logic clk,
  input logic reset,
  input logic tx_start,
  output logic tx_ready,
  input logic [7:0] tx_data,
  output logic tx_line
);

// dl_sync_fifo_ft_if (
//   // Clock and reset
//   input logic rst_n,
//   input logic clk,

//   // FIFO Write interface
//   input  logic                  wr_en,      
//   input  logic [32-1:0] wr_data,      
//   output logic                  ready,    // Inidcates the FIFO can hold more data; basicall !full
//   output logic                  full,
//   output logic                  early_full,
//   output logic                  overflow,

//   // FIFO Read interface
//   input  logic                  rd_en,
//   output logic [32-1:0] rd_data,      
//   output logic                  valid,     // Indicates read data is available
//   output logic                  empty,        // Indicates the FIFO is empty
//   output logic                  early_empty,
//   output logic                  underflow,
//   // FIFO Status
//   input  logic                    hi_mark_reset,
//   output logic [5-1:0] hi_mark_cnt,   // higest FIFO level since last reset
//   output logic [5-1:0] data_cnt   // Number of data words in the FIFO
//  );

// dl_freelistMngr_if #(
//     parameter ListSize = 2048, // This is same as MemDepth in ListListMngr
//     localparam ListSizeBits = $clog2(ListSize),
//     localparam FreeSizeBits = $clog2(ListSize + 1)
// )(
//     input  logic clk,
//     input  logic rst_n,

//     // Freelist Manager Interface
//     // ptrOut - will be used to push a new linkedList manager entry
//     //       freelist entry will be cleared on getPtr
//     // ptrIn - ptr from a linkedList manager pop request
//     //       freelist entry will be set on ptrInValid
//     output logic [ListSizeBits-1:0] ptrOut,    // This value preemptively available, and is updated on getPtr with the next free pointer
//     output logic                    ptrOutValid,
//     input  logic                    getPtr,     // Request to get a free pointer
//     input  logic                    ptrInValid, // Valid signal for pointer being returned to freelist
//     input  logic [ListSizeBits-1:0] ptrIn,     // Pointer being returned to freelist, valid one cycle after ptrInValid is high

//     output logic [FreeSizeBits-1:0] freeSize,  // Number of free pointers available
//     output logic [FreeSizeBits-1:0] usedSize,  // Number of used pointers

//     output logic                    intr        // Interrupt signal
// );

//Please insert the name of the design file: stub_dut.sv
interface uart_if  (
  input clk,
  input reset,
  input tx_start,
  input tx_ready,
  input [7:0] tx_data,
  input tx_line
);

endinterface

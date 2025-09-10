interface dma_if #(
  parameter int ADDR_WIDTH = 16
) (
  input start,
  input done,
  input [ADDR_WIDTH-1:0] src_addr,
  input [ADDR_WIDTH-1:0] dest_addr,
  input busy
);

endinterface

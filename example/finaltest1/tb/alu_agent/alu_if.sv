interface alu_if #(
  parameter int WIDTH = 32,
  parameter int SIGNED_OP = 1
) (
  input clk,
  input rst_n,
  input [WIDTH-1:0] a,
  input [WIDTH-1:0] b,
  input [2:0] op,
  input [WIDTH-1:0] result,
  input valid
);

endinterface

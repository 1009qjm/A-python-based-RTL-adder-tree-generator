module adder
#(parameter DATA_WIDTH=32)
(
input logic clk,
input logic [DATA_WIDTH-1:0] a,
input logic [DATA_WIDTH-1:0] b,
output logic [DATA_WIDTH-1:0] sum
);
always_ff@(posedge clk)
    sum<=a+b;
endmodule
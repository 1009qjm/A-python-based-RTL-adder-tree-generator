module adder_tree
(
input logic [32-1:0] din [0:64-1],
input logic clk,
output logic [32-1:0] sum
);
genvar i;
logic [32-1:0] stage1 [0:64-1];
logic [32-1:0] stage2 [0:32-1];
logic [32-1:0] stage3 [0:16-1];
logic [32-1:0] stage4 [0:8-1];
logic [32-1:0] stage5 [0:4-1];
logic [32-1:0] stage6 [0:2-1];
logic [32-1:0] stage7 [0:1-1];
assign sum=stage7[0];
always_comb
begin
    for(int i=0;i<64;i++)
        stage1[i]=din[i];
end
//level1
generate
for(i=0;i<32;i++)
    adder U1
    (
     .clk(clk),
     .a(stage1[2*i]),
     .b(stage1[2*i+1]),
     .sum(stage2[i])
    );
endgenerate
//level2
generate
for(i=0;i<16;i++)
    adder U2
    (
     .clk(clk),
     .a(stage2[2*i]),
     .b(stage2[2*i+1]),
     .sum(stage3[i])
    );
endgenerate
//level3
generate
for(i=0;i<8;i++)
    adder U3
    (
     .clk(clk),
     .a(stage3[2*i]),
     .b(stage3[2*i+1]),
     .sum(stage4[i])
    );
endgenerate
//level4
generate
for(i=0;i<4;i++)
    adder U4
    (
     .clk(clk),
     .a(stage4[2*i]),
     .b(stage4[2*i+1]),
     .sum(stage5[i])
    );
endgenerate
//level5
generate
for(i=0;i<2;i++)
    adder U5
    (
     .clk(clk),
     .a(stage5[2*i]),
     .b(stage5[2*i+1]),
     .sum(stage6[i])
    );
endgenerate
//level6
generate
for(i=0;i<1;i++)
    adder U6
    (
     .clk(clk),
     .a(stage6[2*i]),
     .b(stage6[2*i+1]),
     .sum(stage7[i])
    );
endgenerate
endmodule
module test_tb;
logic clk;
logic [32-1:0] din [0:64-1];
logic [32-1:0] sum;
logic [32-1:0] ref_sum;
initial
begin
    clk=0;
    forever begin
        #5 clk=~clk;
    end
end
//din
initial
begin
    for(int i=0;i<64;i++)
        din[i]=$urandom%256;
end
always_comb
begin
    ref_sum=0;
    for(int i=0;i<64;i++)
        ref_sum=ref_sum+din[i];
end
//inst
adder_tree U
(.*);
endmodule
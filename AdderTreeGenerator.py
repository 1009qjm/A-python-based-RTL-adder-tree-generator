import numpy as np

def adder(DATA_WIDTH):
    adder="module adder\n" \
           "#(parameter DATA_WIDTH={})\n" \
           "(\ninput logic clk,\n" \
           "input logic [DATA_WIDTH-1:0] a,\n" \
           "input logic [DATA_WIDTH-1:0] b,\n" \
           "output logic [DATA_WIDTH-1:0] sum\n);\n" \
           "always_ff@(posedge clk)\n" \
           "    sum<=a+b;\n" \
           "endmodule".format(DATA_WIDTH)
    return adder

#N输入加法树，N=2^d,即加法树深度为d
def genOneLevel(N,d):                                     #N输入，第d级,N/2^(d-1)输入,N/2^d输出
       generate_for_module="//level{}\n" \
                           "generate\n" \
                    "for(i=0;i<{};i++)\n" \
                    "    adder U{}\n" \
                    "    (\n" \
                    "     .clk(clk),\n" \
                    "     .a(stage{}[2*i]),\n" \
                    "     .b(stage{}[2*i+1]),\n" \
                    "     .sum(stage{}[i])\n" \
                    "    );\n" \
                    "endgenerate\n".format(d,int(N/(2**d)),d,d,d,d+1)

       #print(generate_for_module)
       return generate_for_module

def adderTree(N,DATA_WIDTH):             #N输入加法树
       adder_tree_head="module adder_tree\n" \
           "(\ninput logic [{}-1:0] din [0:{}-1],\n" \
           "input logic clk,\n" \
           "output logic [{}-1:0] sum\n" \
           ");\n".format(DATA_WIDTH,N,DATA_WIDTH)
       depth=int(np.log(N)/np.log(2))
       variables="genvar i;\n"
       for i in range(1,depth+2):
           v="logic [{}-1:0] stage{} [0:{}-1];\n".format(DATA_WIDTH,i,int(N/2**(i-1)))
           variables+=v
       assign_inputs="always_comb\n" \
                     "begin\n" \
                     "    for(int i=0;i<{};i++)\n" \
                     "        stage1[i]=din[i];\n" \
                     "end\n".format(N)
       assign_output="assign sum=stage{}[0];\n".format(depth+1)
       adderTreeInst=""
       for i in range(1,depth+1):
              adderTreeInst+=genOneLevel(N,i);
       return adder_tree_head+variables+assign_output+assign_inputs+adderTreeInst+"endmodule"

def test_tb(DATA_WIDTH,N):
    module="module test_tb;\n" \
                "logic clk;\n" \
                "logic [{}-1:0] din [0:{}-1];\n" \
                "logic [{}-1:0] sum;\n" \
                "logic [{}-1:0] ref_sum;\n" \
                "initial\n" \
                "begin\n" \
                "    clk=0;\n" \
                "    forever begin\n" \
                "        #5 clk=~clk;\n" \
                "    end\n" \
                "end\n" \
                "//din\n" \
                "initial\n" \
                "begin\n" \
                "    for(int i=0;i<{};i++)\n" \
                "        din[i]=$urandom%256;\n" \
                "end\n" \
                "always_comb\n" \
                "begin\n" \
                "    ref_sum=0;\n" \
                "    for(int i=0;i<{};i++)\n" \
                "        ref_sum=ref_sum+din[i];\n" \
                "end\n" \
                "//inst\n" \
                "adder_tree U\n" \
                "(.*);\n" \
                "endmodule".format(DATA_WIDTH,N,DATA_WIDTH,DATA_WIDTH,N,N)
    return module
if __name__=='__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Generator of Verilog Adder Tree")
    parser.add_argument('-W',help="DATA WIDTH", default=32)
    parser.add_argument('-N',help="INPUT DATA NUMBER OF ADDER TREE", default=32)
    args = parser.parse_args()

    adder_module=adder(int(args.W))
    f=open("adder.sv","w")
    f.write(adder_module)
    f.close()
    adderTree_module=adderTree(DATA_WIDTH=int(args.W),N=int(args.N))
    f=open("adderTree.sv","w")
    f.write(adderTree_module)
    f.close()
    test_module=test_tb(DATA_WIDTH=int(args.W),N=int(args.N))
    f=open("test_tb.sv","w")
    f.write(test_module)
    f.close()
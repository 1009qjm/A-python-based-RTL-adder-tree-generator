# A-python-based-RTL-adder-tree-generator
## Introduction
This is a python based script that can generate system verilog codes of pipelined adder tree.There are two configurable parameters in this script:DATA_WIDTH and N.
DATA_WIDTH means the data width of input and output;
N means the input data number of the adder tree,currently only support N to be power of two.
## Usage
To use this script,just input  
**python -W your_data_width -N your_input_data_num**  
Then you can find three system verilog source files in current path.There are adder.sv,adderTree.sv and test_tb.sv.The first two are source file,and the last one is testbench.
## RTL View
Take N=32,W=64 as example,the RTL View is as below:
![2 DOZVM@R3ML}T4M)ATMDC4](https://user-images.githubusercontent.com/44521731/155707182-3c972c43-195f-4189-acd0-01043a017281.png)
## Simulation Result
![NMT9_2}0PMQ3${BH)~MUI}4](https://user-images.githubusercontent.com/44521731/155707287-24c4f175-fa55-4cfd-9979-a112e7910481.png)



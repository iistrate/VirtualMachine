//push const to stack
@15
D=A
@SP
A=M
M=D
//increment stack
@SP
M=M+1
//
// get local + offset
// 
@2 //offset
D=A //offset
@LCL
D=M+D
@R13 //load address of local + stuff
M=D
//pop to D
@SP
M=M-1
@SP
A=M
D=M
//put into R13
@R13
A=M
M=D



@256
D=A
@SP
M=D
@RETURN1
D=A
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R1
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R2
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R3
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R4
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@5
D=A
@SP
AD=A-D
@R2
A=D
@SP
D=M
@R1
M=D
@Sys.init
0;JMP
(RETURN1)
(Main.fibonacci)
@0
D=A
@R2
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@2
D=A
@SP
A=M
M=D
@SP
AM=M+1
@SP
AM=M-1
@SP
A=M
D=M
@SP
AM=M-1
@SP
A=M
A=M
D=A-D
@SP
A=M
M=D
@SP
AM=M+1
@SP
AM=M-1
@SP
A=M
D=M
@CMPTRUE2
D;JLT
@SP
A=M
M=0
@SP
AM=M+1
@END2
0;JMP
(CMPTRUE2)
@SP
A=M
M=-1
@SP
AM=M+1
(END2)
@SP
AM=M-1
@SP
A=M
D=M
@IF_TRUE
D;JNE
@IF_FALSE
0;JMP
(IF_TRUE)
@0
D=A
@R2
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@R1
D=M
@R15
M=D
@5
A=D-A
D=A
@R14
M=D
@0
D=A
@R2
D=D+M
@R13
M=D
@SP
AM=M-1
@SP
A=M
D=M
@R13
A=M
M=D
@R2
M=M+1
D=M
@SP
A=M
M=D
@SP
M=D
@R15
AM=M-1
D=M
@R4
M=D
@R15
AM=M-1
D=M
@R3
M=D
@R15
AM=M-1
D=M
@R2
M=D
@R15
AM=M-1
D=M
@R1
M=D
@R14
A=M
0;JMP
(IF_FALSE)
@0
D=A
@R2
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@2
D=A
@SP
A=M
M=D
@SP
AM=M+1
@SP
AM=M-1
@SP
A=M
D=M
@SP
AM=M-1
@SP
A=M
A=M
D=A-D
@SP
A=M
M=D
@SP
AM=M+1
@RETURN3
D=A
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R1
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R2
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R3
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R4
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@6
D=A
@SP
AD=A-D
@R2
A=D
@SP
D=M
@R1
M=D
@Main.fibonacci
0;JMP
(RETURN3)
@0
D=A
@R2
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@SP
A=M
M=1
@SP
AM=M+1
@SP
AM=M-1
@SP
A=M
D=M
@SP
AM=M-1
@SP
A=M
A=M
D=A-D
@SP
A=M
M=D
@SP
AM=M+1
@RETURN4
D=A
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R1
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R2
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R3
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R4
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@6
D=A
@SP
AD=A-D
@R2
A=D
@SP
D=M
@R1
M=D
@Main.fibonacci
0;JMP
(RETURN4)
@SP
AM=M-1
@SP
A=M
D=M
@SP
AM=M-1
@SP
A=M
A=M
D=D+A
@SP
A=M
M=D
@SP
AM=M+1
@R1
D=M
@R15
M=D
@5
A=D-A
D=A
@R14
M=D
@0
D=A
@R2
D=D+M
@R13
M=D
@SP
AM=M-1
@SP
A=M
D=M
@R13
A=M
M=D
@R2
M=M+1
D=M
@SP
A=M
M=D
@SP
M=D
@R15
AM=M-1
D=M
@R4
M=D
@R15
AM=M-1
D=M
@R3
M=D
@R15
AM=M-1
D=M
@R2
M=D
@R15
AM=M-1
D=M
@R1
M=D
@R14
A=M
0;JMP
(Sys.init)
@4
D=A
@SP
A=M
M=D
@SP
AM=M+1
@RETURN5
D=A
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R1
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R2
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R3
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@0
D=A
@R4
D=D+M
A=D
D=M
@SP
A=M
M=D
@SP
AM=M+1
@6
D=A
@SP
AD=A-D
@R2
A=D
@SP
D=M
@R1
M=D
@Main.fibonacci
0;JMP
(RETURN5)
(WHILE)
@WHILE
0;JMP

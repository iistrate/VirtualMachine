@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=D-A
@EQUAL1
D;JEQ
@NOT_EQUAL1
0;JMP
(EQUAL1)
@SP
A=M
M=-1
(NOT_EQUAL1)
@SP
A=M
M=0
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=D-A
@EQUAL2
D;JEQ
@NOT_EQUAL2
0;JMP
(EQUAL2)
@SP
A=M
M=-1
(NOT_EQUAL2)
@SP
A=M
M=0
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=D-A
@EQUAL3
D;JEQ
@NOT_EQUAL3
0;JMP
(EQUAL3)
@SP
A=M
M=-1
(NOT_EQUAL3)
@SP
A=M
M=0
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=D-A
@LESS_THAN4
D;JLT
@GREATER_THAN4
0;JMP
(LESS_THAN4)
@SP
A=M
M=-1
(GREATER_THAN4)
@SP
A=M
M=0
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=D-A
@LESS_THAN5
D;JLT
@GREATER_THAN5
0;JMP
(LESS_THAN5)
@SP
A=M
M=-1
(GREATER_THAN5)
@SP
A=M
M=0
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=D-A
@LESS_THAN6
D;JLT
@GREATER_THAN6
0;JMP
(LESS_THAN6)
@SP
A=M
M=-1
(GREATER_THAN6)
@SP
A=M
M=0
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=D-A
@LESS_THAN7
D;JLT
@GREATER_THAN7
0;JMP
(LESS_THAN7)
@SP
A=M
M=0
(GREATER_THAN7)
@SP
A=M
M=-1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=D-A
@LESS_THAN8
D;JLT
@GREATER_THAN8
0;JMP
(LESS_THAN8)
@SP
A=M
M=0
(GREATER_THAN8)
@SP
A=M
M=-1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=D-A
@LESS_THAN9
D;JLT
@GREATER_THAN9
0;JMP
(LESS_THAN9)
@SP
A=M
M=0
(GREATER_THAN9)
@SP
A=M
M=-1
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=D+A
@SP
A=M
M=D
@SP
M=M+1
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=D-A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
D=-D
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=D&A
@SP
A=M
M=D
@SP
M=M+1
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=D|A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
@SP
A=M
D=M
D=!D
@SP
A=M
M=D
@SP
M=M+1

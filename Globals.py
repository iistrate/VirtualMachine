#
#   Holds our constants, and globals
#

from Assoc import *
from Stack import *

#globally accessible stack
g_Stack = Stack()  


#registers
SP = 0 #RAM[0]
LCL = 1 #RAM[1]
ARG = 2 #RAM[2]
THIS = 3 #RAM[3] POINTER1
THAT = 4 #RAM[4] POINTER2
#RAM[5..12]
TEMP = 5 #starts at 5 ends at 12  
#RAM[13..15]
GEN_PURPOSE = 13 #starts at 13 ends at 15 

#command types
C_ARITHMETIC = 0
C_PUSH = 1
C_POP = 2
C_LABEL = 3
C_GOTO = 4
C_IF_GOTO = 5
C_FUNCTION = 6
C_RETURN = 7
C_CALL = 8

#command table
commandTable = []
commandTable.append(Assoc("add", C_ARITHMETIC))
commandTable.append(Assoc("sub", C_ARITHMETIC))
commandTable.append(Assoc("neg", C_ARITHMETIC))
commandTable.append(Assoc("eq", C_ARITHMETIC))
commandTable.append(Assoc("gt", C_ARITHMETIC))
commandTable.append(Assoc("lt", C_ARITHMETIC))
commandTable.append(Assoc("and", C_ARITHMETIC))
commandTable.append(Assoc("or", C_ARITHMETIC))
commandTable.append(Assoc("not", C_ARITHMETIC))
commandTable.append(Assoc("push", C_PUSH))
commandTable.append(Assoc("pop", C_POP))
commandTable.append(Assoc("label", C_LABEL))
commandTable.append(Assoc("goto", C_GOTO))
commandTable.append(Assoc("if-goto", C_IF_GOTO))
commandTable.append(Assoc("function", C_FUNCTION))
commandTable.append(Assoc("call", C_CALL))
commandTable.append(Assoc("return", C_RETURN))
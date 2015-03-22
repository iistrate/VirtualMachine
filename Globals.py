#
#   Holds our constants, and globals
#

from Assoc import *  

#command types

C_ARITHMETIC = 0
C_PUSH = 1
C_POP = 2
C_LABEL = 3
C_GOTO = 4
C_IF = 5
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
commandTable.append(Assoc("if-goto", C_IF))
commandTable.append(Assoc("function", C_FUNCTION))
commandTable.append(Assoc("call", C_CALL))
commandTable.append(Assoc("return", C_RETURN))
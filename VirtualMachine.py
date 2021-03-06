#
#   Virtual Machine
#   has: Parser, CodeWriter
#

from Parser import *
from CodeWriter import *

class VirtualMachine(object):
    def __init__(self, userInput):
        self.__m_Parser = Parser(userInput)
        filename = self.__m_Parser.getFileName()
        self.__m_CodeWriter = CodeWriter(filename)

    def run(self):
        while self.__m_Parser.hasMoreCommands:
            #advance through commands
            self.__m_Parser.advance()
            #get command and args and write assembly code for it
            cmdType = self.__m_Parser.commandType
            if cmdType == C_ARITHMETIC:
                self.__m_CodeWriter.writeArithmetic(self.__m_Parser.arg1())
            elif cmdType in (C_PUSH, C_POP):
                self.__m_CodeWriter.writePushPop(cmdType, self.__m_Parser.arg1(), self.__m_Parser.arg2()) 
            elif cmdType == C_LABEL:
                self.__m_CodeWriter.writeLabel(self.__m_Parser.arg1(), False)
            elif cmdType == C_IF_GOTO:
                self.__m_CodeWriter.writeIf(self.__m_Parser.arg1())
            elif cmdType == C_GOTO:
                self.__m_CodeWriter.writeGoto(self.__m_Parser.arg1(), False)
            elif cmdType == C_FUNCTION:
                self.__m_CodeWriter.writeFunction(self.__m_Parser.arg1(), self.__m_Parser.arg2())
            elif cmdType == C_CALL:
                self.__m_CodeWriter.writeCall(self.__m_Parser.arg1(), self.__m_Parser.arg2())
            elif cmdType == C_RETURN:
                self.__m_CodeWriter.writeReturn()


            #test case
            print(self.__m_Parser.getRawCommand())
            #print("Arg1 is {}, Arg2 is {}".format(self.__m_Parser.arg1(), self.__m_Parser.arg2()))        
            #end test

        #close and free resources
        self.__m_CodeWriter.close()
        #print contents of out file
        print(self.__m_CodeWriter)

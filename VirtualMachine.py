#
#   Virtual Machine
#   has: Parser, CodeWriter
#

from Parser import *
from CodeWriter import *

class VirtualMachine(object):
    def __init__(self, filename):
        self.__m_Parser = Parser(filename)
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

            #test case
            print(self.__m_Parser.getRawCommand())
            #print("Arg1 is {}, Arg2 is {}".format(self.__m_Parser.arg1(), self.__m_Parser.arg2()))        
            #end test

        #close and free resources
        self.__m_CodeWriter.close()
        #print contents of out file
        print(self.__m_CodeWriter)

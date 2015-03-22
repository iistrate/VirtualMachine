#
#   Virtual Machine
#   has: Stack, Instruction
#

from Stack import *
from Parser import *

class VirtualMachine(object):
    def __init__(self, filename):
        self.__m_Stack = Stack()
        self.__m_Parser = Parser(filename)

    def run(self):
        #test case
        while self.__m_Parser.hasMoreCommands:
            self.__m_Parser.advance()
            print(self.__m_Parser.getRawCommand())
            print("Arg1 is {}".format(self.__m_Parser.arg1()))        
            print("Arg2 is {}".format(self.__m_Parser.arg2()))        

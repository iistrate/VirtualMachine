#
#   Virtual Machine
#   has: Stack, Instruction
#

from Stack import *

class VirtualMachine(object):
    def __init__(self, filename):
        self.__m_Stack = Stack()
        self.__m_Parser = Parser(filename)

    def run(self):
        self.__m_Stack.push(3)
        print(self.__m_Stack.getPointer)
        print(self.__m_Stack.pop())
        print(self.__m_Stack.getPointer)

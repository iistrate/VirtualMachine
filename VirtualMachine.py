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
        print(self.__m_Parser)

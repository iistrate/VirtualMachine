from Stack import *

class VirtualMachine(object):
    def __init__(self):
        self.m_Stack = Stack()

    def run(self):
        self.m_Stack.push(3)
        print(self.m_Stack.getPointer)
        print(self.m_Stack.pop())
        print(self.m_Stack.getPointer)

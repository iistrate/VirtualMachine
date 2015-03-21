class Stack(object):
    """I am a stack"""
    def __init__(self):
        self.__m_contents = list()
        self.__m_pointer = 0
    #push
    def push(self, value):
        self.__m_contents.append(value)
        self.__m_pointer += 1
    #pop
    def pop(self):
        if not (self.__m_pointer - 1 < 0): self.__m_pointer -= 1
        return self.__m_contents.pop()
    @property
    def getPointer(self):
        return self.__m_pointer


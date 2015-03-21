class Instruction(object):
    """Holds Instruction Key and Value"""
    def __init__(self):
        self.__m_key = 0
        self.__m_value = 0
    
    #print override
    def __str__(self):
        rep = "Key is {0} | Value is {1}".format(self.__m_key, self.__m_value)
        return rep      

    #key value sets and gets
    def setValue(self, value):
        self.__m_value = value
    def getValue(self):
        return self.__m_value;

    def setKey(self, key):
        self.__m_key = key
    def getKey(self):
        return self.__m_key
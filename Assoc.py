class Assoc(object):
    """Holds Assoc Key and Value"""
    def __init__(self, key, value):
        self.__m_key = key
        self.__m_value = value
    
    #print override
    def __str__(self):
        rep = "Key is {0} | Value is {1}".format(self.__m_key, self.__m_value)
        return rep      

    #key value sets and gets
    def setValue(self, value):
        self.__m_value = value
    @property
    def getValue(self):
        return self.__m_value;

    def setKey(self, key):
        self.__m_key = key
    @property
    def getKey(self):
        return self.__m_key
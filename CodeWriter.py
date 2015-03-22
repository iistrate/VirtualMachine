class CodeWriter(object):
    """Translates VM commands into Hack assembly code"""

    def __init__(self, filename):
        self.__m_outFile = open(filename, 'w')
        self.__m_started = False
    
    #translation of a VM file started     
    def setFileName(self):
        self.__m_started = True

    #write assembly for arithmetic commands
    def writeArithmetic(self, command):
        pass

    #write assembly for push or pop
    def writePushPop(self, command, segment, index):
        pass

    #close resources
    def close(self):
        self.__m_outFile.close()

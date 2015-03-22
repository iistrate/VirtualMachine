from Globals import *

class CodeWriter(object):
    """Translates VM commands into Hack assembly code"""

    def __init__(self, filename):
        #change .vm to .asm
        filename = filename[:-2] 
        filename = filename + "asm"

        self.__m_outFile = open(filename, 'w')
        self.__m_started = False
    
    #translation of a VM file started     
    def setFileName(self):
        self.__m_started = True

    #write assembly for arithmetic commands
    def writeArithmetic(self, command):
        if command == "add":
            #test stack
            print(g_Stack)
            #end test
            x = g_Stack.pop()
            y = g_Stack.pop()
            add = int(x) + int(y)
            g_Stack.push(add)
            #test stack
            print(g_Stack)
            #end test

    #write assembly for push or pop
    def writePushPop(self, command, segment, index):
        #see if segment is a constant
        if segment == "constant":
            #if constant then add the actual value
            g_Stack.push(index)
    
    #writing to file
    def writeACommand(self, address):
        self.__m_outFile.writelines('@' + address + '\n')

    def writeLCommand(self, label):
        self.__m_outFile.writelines('(' + label + ')')

    def writeCCommand(self, dest, comp, jump):
        if dest:
            self.__m_outFile.writelines(dest + "=")
        if comp:
            self.__m_outFile.writelines(comp)
        if jump:
            self.__m_outFile.writelines(";" + jump)
        self.__m_outFile.writelines("\n")


    #close resources
    def close(self):
        self.__m_outFile.close()

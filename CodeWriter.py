from Globals import *

class CodeWriter(object):
    """Translates VM commands into Hack assembly code"""

    def __init__(self, filename):
        #change .vm to .asm
        filename = filename[:-2] 
        filename = filename + "asm"

        self.__m_filename = filename
        self.__m_outFile = open(filename, 'w')
        self.__m_started = False
    
    #translation of a VM file started     
    def setFileName(self):
        self.__m_started = True

    def __str__(self):
        rep = ""
        for line in open(self.__m_filename, 'r'):
            rep += line
        return rep

    #write assembly for arithmetic commands
    def writeArithmetic(self, command):
        if command == "add":
            x = g_Stack.pop()
            self.writeACommand(x) #@value
            self.writeCCommand('D', 'A', None) #@D=A
            y = g_Stack.pop()
            self.writeACommand(y)  #@value
            self.writeCCommand('A', 'A+D', None) #@A=A+D
            add = int(x) + int(y)
            g_Stack.push(add)
        elif command == "sub":
            x = g_Stack.pop()
            self.writeACommand(x) #@value
            self.writeCCommand('D', 'A', None) #@D=A
            y = g_Stack.pop()
            self.writeACommand(y)  #@value
            self.writeCCommand('A', 'A-D', None) #@A=A-D
            add = int(x) - int(y)
            g_Stack.push(add)
        elif command == "neg":
            x = g_Stack.pop()
            self.writeACommand(x) #@value
            self.writeCCommand('A', '-A', None) #@A=-A
            neg = (-1) * int(x)
            g_Stack.push(neg)

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

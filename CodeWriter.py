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
            #pop x to D
            self.pop("D")
            #pop y to A
            self.pop("A")
            #add x and y
            self.writeCCommand("D", "D+A", None) #A=A+D
            #push add
            self.push()
        elif command == "eq":
            pass

    #write assembly for push or pop
    def writePushPop(self, command, segment, index):
        #if constant then push the actual value
        if command == C_PUSH:
            if segment == "constant": 
                #load into A
                self.writeACommand(str(index)) #@value
                #copy A to D
                self.writeCCommand("D", "A", None) #D=A
                #load stack pointer
                self.writeACommand("SP") #@SP
                self.writeCCommand("A", "M", None) #A=M
                self.writeCCommand("M", "D", None) #M=D
            #increment stack pointer
            self.incStackP()
        elif command == C_POP:
            pass
            #decrement stack pointer
            #self.decStackP()

    #push to stack
    def push(self):
        self.writeACommand("SP") #@SP
        self.writeCCommand("A", "M", None) #A=M
        self.writeCCommand("M", "D", None) #M=D
        self.incStackP()

    #pop
    def pop(self, dest):
        self.decStackP()
        self.writeACommand("SP") #@SP
        self.writeCCommand("A", "M", None) #A=M
        self.writeCCommand(dest, "M", None) #D=M

    #inc stack pointer
    def incStackP(self):
        self.writeACommand("SP")
        self.writeCCommand("M", "M+1", None)
    #dec stack pointer
    def decStackP(self):
        self.writeACommand("SP")
        self.writeCCommand("M", "M-1", None)

    #writing to file
    def writeACommand(self, address):
        self.__m_outFile.writelines('@' + str(address) + '\n')

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

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
        self.__m_labelCounter = 1
    
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
            self.writeCCommand("D", "D+A", None) #D=D+A
            #push add
            self.push()
        elif command == "sub":
            #pop x to D
            self.pop("D")
            #pop y to A
            self.pop("A")
            #add x and y
            self.writeCCommand("D", "D-A", None) #D=D-A
            #push add
            self.push()
        elif command == "eq":
            #pop x to D
            self.pop("D")
            #pop y to A
            self.pop("A")
            #sub x and y
            self.writeCCommand("D", "D-A", None) #D=D-A
            #labels
            self.writeACommand("EQUAL" + str(self.__m_labelCounter)) #@EQUAL$i
            self.writeCCommand("D", None, "JEQ") #D;JEQ
            self.writeACommand("NOT_EQUAL" + str(self.__m_labelCounter)) #@NOT_EQUAL$i
            self.writeCCommand("0", None, "JMP") #0;JNE
            self.writeLCommand("EQUAL" + str(self.__m_labelCounter)) #(EQUAL$i)
            #put -1
            self.valToStack("-1")
            self.writeLCommand("NOT_EQUAL" + str(self.__m_labelCounter)) #(NOT_EQUAL$i)
            #put 0
            self.valToStack("0")
            self.__m_labelCounter += 1
        elif command == "gt":            
            #pop x to D
            self.pop("D")
            #pop y to A
            self.pop("A")
            #sub x and y
            self.writeCCommand("D", "D-A", None) #D=D-A
            #labels
            self.writeACommand("LESS_THAN" + str(self.__m_labelCounter)) #@LESS$i
            self.writeCCommand("D", None, "JLT") #D;JLT
            self.writeACommand("GREATER_THAN" + str(self.__m_labelCounter)) #@GREATER_THAN$i
            self.writeCCommand("0", None, "JMP") #0;JMP
            self.writeLCommand("LESS_THAN" + str(self.__m_labelCounter)) #(LESS_THAN$i)
            #put -1
            self.valToStack("0")
            self.writeLCommand("GREATER_THAN" + str(self.__m_labelCounter)) #(GREATER_THAN$i)
            #put 0
            self.valToStack("-1")
            self.__m_labelCounter += 1
        elif command == "lt":
            #pop x to D
            self.pop("D")
            #pop y to A
            self.pop("A")
            #sub x and y
            self.writeCCommand("D", "D-A", None) #D=D-A
            #labels
            self.writeACommand("LESS_THAN" + str(self.__m_labelCounter)) #@LESS$i
            self.writeCCommand("D", None, "JLT") #D;JLT
            self.writeACommand("GREATER_THAN" + str(self.__m_labelCounter)) #@GREATER_THAN$i
            self.writeCCommand("0", None, "JMP") #0;JMP
            self.writeLCommand("LESS_THAN" + str(self.__m_labelCounter)) #(LESS_THAN$i)
            #put -1
            self.valToStack("-1")
            self.writeLCommand("GREATER_THAN" + str(self.__m_labelCounter)) #(GREATER_THAN$i)
            #put 0
            self.valToStack("0")
            self.__m_labelCounter += 1
        elif command == "and":
            #pop x to D
            self.pop("D")
            #pop y to A
            self.pop("A")
            self.writeCCommand("D", "D&A", None) #D=D&A
            self.push()
        elif command == "or":
            #pop x to D
            self.pop("D")
            #pop y to A
            self.pop("A")
            self.writeCCommand("D", "D|A", None) #D=D&A
            self.push()
        elif command == "not":
            #pop x to D
            self.pop("D")
            self.writeCCommand("D", "-D", None) #D=-D
            self.push()

    #write assembly for push or pop
    def writePushPop(self, command, segment, index):
        #if constant then push the actual value
        if command == C_PUSH:
            if segment == "constant": 
                #load into A
                self.writeACommand(str(index)) #@value
                #copy A to D
                self.writeCCommand("D", "A", None) #D=A
                self.push()
            #increment stack pointer
            self.incStackP()
        elif command == C_POP:
            pass
            #decrement stack pointer
            #self.decStackP()
    
    def valToStack(self, val):
        self.writeACommand("SP") #@SP
        self.writeCCommand("A", "M", None) #A=M
        self.writeCCommand("M", val, None) #M=val
        
    #push to stack
    def push(self):
        self.writeACommand("SP") #@SP
        self.writeCCommand("A", "M", None) #A=M
        self.writeCCommand("M", "D", None) #M=D
        self.incStackP()

    #pop to dest
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

    ##
    # Writing to file
    ##

    #Address
    def writeACommand(self, address):
        self.__m_outFile.writelines('@' + str(address) + '\n')
    
    #Label
    def writeLCommand(self, label):
        self.__m_outFile.writelines('(' + label + ')' + "\n")
    
    #Dest=Comp;Jump
    def writeCCommand(self, dest, comp, jump):
        if dest:
            dORj = "=" if not jump else ";"
            self.__m_outFile.writelines(dest + dORj)
        if comp:
            self.__m_outFile.writelines(comp)
        if jump:
            self.__m_outFile.writelines(jump)
        self.__m_outFile.writelines("\n")


    #close resources
    def close(self):
        self.__m_outFile.close()

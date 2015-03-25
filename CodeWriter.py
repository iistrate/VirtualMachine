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

    def writeInit(self):
        #make stack pointer start at 256
        self.valToStack(256)
        #cals Sys.init

    
    
    #write assembly for arithmetic commands
    def writeArithmetic(self, command):
        if command == "add":
            self.doBinary("D+A") #D=D+A
            self.push()
        elif command == "sub":
            self.doBinary("D-A") #D=D-A
            self.push()
        elif command == "eq":
            #dest jump with label
            self.doDestJump("D", "JEQ")
        elif command == "gt":            
            #dest jump with label
            self.doDestJump("D", "JGT")
        elif command == "lt":
            #dest jump with label
            self.doDestJump("D", "JLT")
        elif command == "and":
            self.doBinary("D&A") #D=D&A
            self.push()
        elif command == "or":
            self.doBinary("D|A") #D=D&A
            self.push()
        elif command == "neg":
            self.doUnary("-D") #D=-D
            self.push()
        elif command == "not":
            self.doUnary("!D") #D=!D
            self.push()
    
    #add labels and symbols for dest jumps
    def doDestJump(self, dest, jump):
        #do sub first
        self.doBinary("D-A") #D=D-A
        #condition @
        self.writeACommand("CMPTRUE" + str(self.__m_labelCounter)) #@GENERATED$i
        self.writeCCommand(dest, None, jump) #D;JEQ
        #if not condition @
        self.writeACommand("CMPFALSE" + str(self.__m_labelCounter)) #@GENERATED$i
        self.writeCCommand("0", None, "JMP") #0;JMP
        #labels ()
        self.writeLabel("CMPFALSE" + str(self.__m_labelCounter)) #(LESS_THAN$i)
        self.valToStack("0")
        #end @symbol
        self.writeACommand("END" + str(self.__m_labelCounter)) #@GENERATED$i
        self.writeCCommand("0", None, "JMP") #0;JMP
        #labels ()
        self.writeLabel("CMPTRUE" + str(self.__m_labelCounter)) #(LESS_THAN$i)
        self.valToStack("-1")
        #label end ()
        self.writeLabel("END" + str(self.__m_labelCounter)) #(LESS_THAN$i) 
        self.__m_labelCounter += 1

    def doUnary(self, comp):
        #pop x to D
        self.pop("D")
        self.writeCCommand("D", comp, None)

    def doBinary(self, comp):
        #pop x to D
        self.pop("D")
        #pop y to A
        self.pop("A")            
        #add/sub.. x and y
        self.writeCCommand("D", comp, None)

    def writeLabelSymbol(self):
        self.writeACommand("Label" + str(self.__m_labelCounter)) #@Label($i)

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
        #only good for -1, 1, and 0
        if val in (-1, 1, 0):
            self.writeACommand("SP") #@SP
            self.writeCCommand("A", "M", None) #A=M
            self.writeCCommand("M", val, None) #M=val
        #else we have to use registers
        else:
            self.writeACommand("@256")
            self.writeCCommand("D", "A", None) #D=A
            self.writeACommand("@SP")
            self.writeCCommand("A", "D", None) #A=D
        
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
    def writeLabel(self, label):
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

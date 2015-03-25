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

        #init stack to 256 and call main
        #self.writeInit()
    
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
        self.pushConstToStack(256)
        #cals Sys.init
    
    #write assembly for arithmetic commands
    def writeArithmetic(self, command):
        if command == "add":
            self.doBinary("D+A") #D=D+A
        elif command == "sub":
            self.doBinary("D-A") #D=D-A
        elif command == "eq":
            self.doDestJump("D", "JEQ")
        elif command == "gt":            
            self.doDestJump("D", "JGT")
        elif command == "lt":
            self.doDestJump("D", "JLT")
        elif command == "and":
            self.doBinary("D&A") #D=D&A
        elif command == "or":
            self.doBinary("D|A") #D=D&A
        elif command == "neg":
            self.doUnary("-D") #D=-D
        elif command == "not":
            self.doUnary("!D") #D=!D

    #write assembly for push or pop
    def writePushPop(self, command, segment, index):
        #if constant then push the actual value
        if command == C_PUSH:
            if segment == "constant": 
                self.pushConstToStack(index)
        elif command == C_POP:
            #decrement stack pointer
            #self.decStackP()
            pass
    
    #add labels and symbols for dest jumps
    def doDestJump(self, dest, jump):
        #do sub first
        self.doBinary("D-A") #D=D-A
        #load to D
        self.pop("D")
        #condition @
        self.writeLabelSymbol("CMPTRUE")
        self.writeCCommand(dest, None, jump) #D;JEQ
        #if here means no jump
        self.pushConstToStack("0")
        #unconditional jump to label
        self.writeGoto("END")
        #labels ()
        self.writeLabel("CMPTRUE")
        self.pushConstToStack("-1")
        #label end ()
        self.writeLabel("END")
        self.__m_labelCounter += 1

    def doUnary(self, comp):
        #pop x to D
        self.pop("D")
        self.writeCCommand("D", comp, None)
        self.pushDtoStack()

    def doBinary(self, comp):
        #pop x to D
        self.pop("D")
        #pop y to A
        self.pop("A")            
        #add/sub.. x and y
        self.writeCCommand("D", comp, None)
        self.pushDtoStack()

    def writeLabelSymbol(self, label):
        self.writeACommand(label + str(self.__m_labelCounter)) #@Label($i)

    #unconditional jump to label
    def writeGoto(self, label):
        self.writeLabelSymbol(label)
        self.writeCCommand("0", None, "JMP")
    
    def writeIf(self, label):
        #load stack pointer with 0 or -1
        self.pop()
        self.writeLabelSymbol(label)        
        self.writeCCommand("D", None, "JNE") #if D is < 0 or D is > 0
       
    #push a value to stack; increments stack pointer
    def pushConstToStack(self, val):
        #only good for -1, 1, and 0
        if val in ("-1", "1", "0"):
            self.writeACommand("SP") #@SP
            self.writeCCommand("A", "M", None) #A=M
            #load value straight to stack
            self.writeCCommand("M", val, None) #M=val
        #else we have to use registers
        else:
            #load value into A
            self.writeACommand(val)
            #load value into D
            self.writeCCommand("D", "A", None) #D=A
            self.pushDtoStack()
        self.incStackP()
    
    #push D to stack
    def pushDtoStack(self):
        self.writeACommand("SP")
        self.writeCCommand("A", "M", None) #A=M
        self.writeCCommand("M", "D", None) #M=D



    #pop to dest
    def pop(self, dest):
        self.decStackP()
        self.writeACommand("SP") #@SP
        self.writeCCommand("A", "M", None) #A=M
        self.writeCCommand(dest, "M", None) #D||A=M

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
        self.__m_outFile.writelines('(' + label + str(self.__m_labelCounter) +  ')' + "\n")           
    
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

from Globals import *
import os
class CodeWriter(object):
    """Translates VM commands into Hack assembly code"""

    def __init__(self, filename):
        isDir = False
        #cut out .vm 
        if ".vm" in filename:
            filename = filename[:-3] 
        else:
            #read until the first /
            index = filename.find("/")
            #filepath/filename
            filename += filename[index+1:-1]
            isDir = True

        #add .asm
        filename = filename + ".asm"

        self.__m_filename = filename
        self.__m_outFile = open(filename, 'w')
        self.__m_labelCounter = 1
        
        if isDir:
            #init stack to 256 and call main
            self.writeInit()

    
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
        self.writeCall("Sys.init", 0)
    
    #write assembly for arithmetic commands
    def writeArithmetic(self, command):
        if command == "add":
            self.doBinary("D+A") #D=D+A
        elif command == "sub":
            self.doBinary("A-D") #D=A-D
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
            else:
                self.pushFromRAM(segment, index)
        elif command == C_POP:
            if segment != "constant" :
                self.popToRam(segment, index)
               
    def writeFunction(self, name, param):
         self.writeLabelSymbol(name, False)
         for var in range(0, int(param)):
             #push enough 0 constants on the stack
             self.pushConstToStack(0)

    def writeCall(self, name, param):
        label = self.writeLabelSymbol("RETURN")#@label{i}
        #push label
        self.writeCCommand("D", "M") #address to D
        self.putDintoRAM("SP")
        self.incStackP()  
        #end push label
        self.pushFromRAM("local", 0)
        self.pushFromRAM("argument", 0)
        self.pushFromRAM("this", 0)
        self.pushFromRAM("that", 0)
        #1
        self.writeACommand(str(int(param)+5))
        self.writeCCommand("D", "A")
        self.writeACommand("SP")
        self.writeCCommand("AD", "A-D")
        #e1
        #2
        self.writeACommand("R2")
        self.writeCCommand("A", "D")
        #e2
        #3 LCL=SP
        self.writeACommand("SP")
        self.writeCCommand("D", "M")
        self.writeACommand("R1")
        self.writeCCommand("M", "D")
        #e3
        self.writeCCommand('0', None, 'JMP')
        self.writeLabel(label[:-1])#(label{i})
        self.__m_labelCounter += 1

    def writeFrame(self, register):
        self.writeACommand("R15")
        self.writeCCommand("AM", "M-1") #get content
        self.writeCCommand("D", "M") #de ref
        self.writeACommand(register)
        self.writeCCommand("M", "D") #bam

    def writeReturn(self):
        #1 Frame = LCL
        self.writeACommand("R1")
        self.writeCCommand("D", "M") 
        self.writeACommand("R15") #frame
        self.writeCCommand("M", "D") #address of R1 in R13 (frame)
        #end1
        #2 RET = *(Frame - 5)
        self.writeACommand("5")
        self.writeCCommand("A", "D-A")
        self.writeCCommand("D", "A") #de ref 312 here
        self.writeACommand("R14") #return is R14 1000 here????
        self.writeCCommand("M", "D")
        #end2
        #3 *ARG = pop()
        self.popToRam("argument", 0)
        #end3
        #4 SP = ARG+1
        self.writeACommand("SP")
        self.writeCCommand("A", "M")
        self.writeCCommand("M", "D")
        self.writeACommand("SP")
        self.writeCCommand("M", "D")
        #end4
        self.writeFrame("R4") #that
        self.writeFrame("R3") #this
        self.writeFrame("R2") #argument       
        self.writeFrame("R1") #local
        #jump to return
        self.writeACommand("R14")
        self.writeCCommand("A", "M") #bam
        self.writeCCommand("0", None, "JMP")

    #add labels and symbols for dest jumps
    def doDestJump(self, dest, jump):
        #do sub first
        self.doBinary("A-D") #D=D-A
        #load to D
        self.popToRegister("D")
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
        self.popToRegister("D")
        self.writeCCommand("D", comp, None)
        self.putDintoRAM("SP")
        self.incStackP()

    def doBinary(self, comp):
        #pop x to D
        self.popToRegister("D")
        #pop y to A
        self.popToRegister("A")            
        #add/sub.. x and y
        self.writeCCommand("D", comp, None)
        self.putDintoRAM("SP")
        self.incStackP()

    def writeLabelSymbol(self, label, autoGen = True):
        label = label if autoGen == False else label + str(self.__m_labelCounter)
        self.writeACommand(label) #@Label($i)
        return label

    #unconditional jump to label
    def writeGoto(self, label, autoGen = True):
        self.writeLabelSymbol(label, autoGen)
        self.writeCCommand("0", None, "JMP")
    
    def writeIf(self, label):
        #load stack pointer with 0 or -1
        self.popToRegister("D")
        self.writeLabelSymbol(label, False)        
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
            self.putDintoRAM("SP")
        self.incStackP()
    
    #push D to RAM
    def putDintoRAM(self, ram):
        self.writeACommand(ram)
        self.writeCCommand("A", "M", None) #A=M
        self.writeCCommand("M", "D", None) #M=D

    #put stack value into D
    def StackVToD(self):
        self.writeACommand("SP")
        self.writeCCommand("A", "M")
        self.writeCCommand("D", "M")

    #pop stack content to A
    def pop(self):
        self.decStackP()
        #load stack address into A
        self.writeACommand("SP") #@SP
        #load stack content into A
        self.writeCCommand("A", "M", None) #A=M

    #pop to registers A or D
    def popToRegister(self, dest):
        self.pop()
        self.writeCCommand(dest, "M", None) #D|A=M
    
    #pop to RAM
    def popToRam(self, segment, index):
        memory = self.memoryType(segment) if segment != "static" else self.memoryType(segment) + str(index)
        if segment != "static":
            #load offset
            self.writeACommand(index)
            self.writeCCommand("D", "A", None) #load offset to D
        #access R+segment
        self.writeACommand(memory)
        if segment == "temp" or segment == "pointer":
           self.writeCCommand("D", "D+A", None) #add offset to local/temp/arg address 300+offset
        elif segment == "static":
           self.writeCCommand("D", "A", None) #add offset to local/temp/arg address 300+offset
        else:
             self.writeCCommand("D", "D+M", None) #add offset to local/temp/arg address 300+offset
        #load R13
        self.writeACommand("R13")
        self.writeCCommand("M", "D", None) #save address to R13
        #pop value to register
        self.popToRegister("D")
        #put D value into local/temp/arg address 300+offset
        self.putDintoRAM("R13")


    #take what is in segment + index and push it to SP
    def pushFromRAM(self, segment, index):
        memory = self.memoryType(segment) if segment != "static" else self.memoryType(segment) + str(index)
        if segment != "static":
            #load offset
            self.writeACommand(index)
            self.writeCCommand("D", "A", None) #load offset to D
        #access R+segment
        self.writeACommand(memory)
        if segment == "temp" or segment == "pointer":
           self.writeCCommand("D", "D+A", None) #add offset to local/temp/arg address 300+offset
        elif segment == "static":
           self.writeCCommand("D", "A", None) #add offset to local/temp/arg address 300+offset
        else:
             self.writeCCommand("D", "D+M", None) #add offset to local/temp/arg address 300+offset

        self.writeCCommand("A", "D", None) #add offset to local/temp/arg address 300+offset
        self.writeCCommand("D", "M", None) #add offset to local/temp/arg address 300+offset

        self.putDintoRAM("SP")
        self.incStackP()      
    
    def memoryType(self, segment):
        memory = "R"
        if segment == "local":
            memory += str(LCL)
        elif segment == "temp":
            memory += str(TEMP)
        elif segment == "this" or segment == "pointer":
            memory += str(THIS)
        elif segment == "that":
            memory += str(THAT)
        elif segment == "argument":
            memory += str(ARG)
        elif segment == "static":
            memory = self.__m_filename[:-3]
        return memory
    ##
    # Stack Ops
    ##

    #inc stack pointer
    def incStackP(self):
        self.writeACommand("SP")
        self.writeCCommand("AM", "M+1", None)

    #dec stack pointer
    def decStackP(self):
        self.writeACommand("SP")
        self.writeCCommand("AM", "M-1", None)

    ##
    # Writing to file
    ##

    #Address
    def writeACommand(self, address):
        self.__m_outFile.writelines('@' + str(address) + '\n')
 
    #Label
    def writeLabel(self, label, autoGen = True):
        label = label if autoGen == False else label + str(self.__m_labelCounter)
        self.__m_outFile.writelines('(' + label +  ')' + "\n")           
    
    #Dest=Comp;Jump
    def writeCCommand(self, dest, comp, jump=None):
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

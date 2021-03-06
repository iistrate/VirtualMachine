from Globals import *
import os

class CodeWriter(object):
    """Translates VM commands into Hack assembly code"""

    def __init__(self, filename):
        hasSys = False
        self.__m_path = ""

        #cut out .vm 
        if ".vm" in filename:
            #read until the last /
            index = filename.rfind("/")
            #filepath/filename
            self.__m_path += filename[:index+1]
            filename = filename[index+1:]
            #filename - .vm
            filename = filename[:-3] 
        else:
            #read until the first /
            # directory/
            index = filename[:-1].find("/")
            #filepath/filename
            self.__m_path = filename
            filename = filename[index+1:-1]
            if "Sys.vm" in os.listdir(self.__m_path):
                hasSys = True
                
        #add .asm
        filename = filename + ".asm"

        self.__m_filename = filename
        self.__m_outFile = open(self.__m_path +  self.__m_filename, 'w')
        self.__m_labelCounter = 1
        
        if hasSys:
        #init stack to 256 and call Sys
            self.writeInit()
            

    
    #translation of a VM file started     
    def setFileName(self):
        self.__m_started = True

    def __str__(self):
        rep = ""
        for line in open(self.__m_path + self.__m_filename, 'r'):
            rep += line
        return rep

    def writeInit(self):
        #make stack pointer start at 256
        self.writeACommand("256")
        self.writeCCommand("D", "A", None) #D=A
        self.writeACommand("SP")
        self.writeCCommand("M", "D", None) #M=D
        #cals Sys.init
        self.writeComment("stack to 256, now call Sys.init");
        self.writeCall("Sys.init", 0)
    
    #write assembly for arithmetic commands
    def writeArithmetic(self, command):
        if command == "add":
            self.writeComment("add");
            self.doBinary("D+A") #D=D+A
        elif command == "sub":
            self.writeComment("sub");
            self.doBinary("A-D") #D=A-D
        elif command == "eq":
            self.writeComment("eq");
            self.doDestJump("D", "JEQ")
        elif command == "gt":            
            self.writeComment("gt");
            self.doDestJump("D", "JGT")
        elif command == "lt":
            self.writeComment("lt");
            self.doDestJump("D", "JLT")
        elif command == "and":
            self.writeComment("and");
            self.doBinary("D&A") #D=D&A
        elif command == "or":
            self.writeComment("or");
            self.doBinary("D|A") #D=D&A
        elif command == "neg":
            self.writeComment("neg");
            self.doUnary("-D") #D=-D
        elif command == "not":
            self.writeComment("not");
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
         self.writeLabel(name, False)
         for var in range(0, int(param)):
             #push enough 0 constants on the stack
             self.pushConstToStack(0)

    def writeCallPush(self, register):
        self.writeCCommand("D", "M")
        self.writeCCommand("A", "M")
        self.writeACommand("SP")
        self.writeCCommand("A", "M")
        self.writeCCommand("M","D")
        self.incStackP()

    def writeCall(self, name, param):
        #push label
        self.writeComment("push label");
        label = self.writeLabelSymbol("RETURN")#@label{i}
        self.writeCCommand("D", "A") #address to D
        self.putDintoRAM("SP")
        self.incStackP()  
        #end push label
        #push in 262 261
        self.writeCallPush("R1");
        #
        #push in 262 261
        self.writeCallPush("R2");
        #
        #push in 263 3000
        self.writeCallPush("R3");
        #
        #push in 262 4000
        self.writeCallPush("R4");
        #ARG = (SP-n-5)
        self.writeComment("ARG = (SP-n-5)")
        self.writeACommand(str(int(param)+5))
        self.writeCCommand("D", "A") #5+n in D
        self.writeACommand("SP") #load SP
        self.writeCCommand("A", "M", None)
        self.writeCCommand("D", "A-D") #in D = SP-n-5
        self.writeACommand("R2") #ARG
        self.writeCCommand("M", "D") #ARG = ^^
        #LCL=SP
        self.writeComment("LCL=SP");
        self.writeACommand("SP")
        self.writeCCommand("A", "M")
        self.writeCCommand("D", "A")
        self.writeACommand("R1")
        self.writeCCommand("M", "D")
        #goto fname
        self.writeComment("goto fname")
        self.writeACommand(name)
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
        self.writeComment("Frame = LCL")
        self.writeACommand("R1")
        self.writeCCommand("D", "M") 
        self.writeACommand("R15") #frame
        self.writeCCommand("M", "D") #address of R1 in R13 (frame)
        #end1
        #2 RET = *(Frame - 5)
        self.writeComment("RET = *(Frame - 5)")
        self.writeACommand("5")
        self.writeCCommand("A", "D-A") #frame still loaded in D
        self.writeCCommand("D", "M") #de ref 312 here ??error could be here!!
        self.writeACommand("R14") #return is R14 1000 here????
        self.writeCCommand("M", "D")
        #end2
        #3 *ARG = pop()
        self.writeComment("*ARG = pop()")
        self.decStackP()
        self.writeACommand("SP")
        self.writeCCommand("A", "M") #stack to D
        self.writeCCommand("D", "M") #stack to D
        self.writeACommand("R2")
        self.writeCCommand("A", "M")
        self.writeCCommand("M", "D")   
        #end3
        #4 SP = ARG+1
        self.writeComment("SP = ARG+1");
        self.writeACommand("R2")
        self.writeCCommand("M", "M+1")
        self.writeCCommand("D", "M")
        self.writeACommand("SP")
        self.writeCCommand("M", "D")
        #end4
        self.writeComment("that");
        self.writeFrame("R4") #that
        self.writeComment("this");
        self.writeFrame("R3") #this
        self.writeComment("argument");
        self.writeFrame("R2") #argument       
        self.writeComment("local");
        self.writeFrame("R1") #local
        #jump to return
        self.writeComment("jump to return");
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

    def writeComment(self, comment):
        self.__m_outFile.writelines("// {} \n".format(comment))

    #close resources
    def close(self):
        self.__m_outFile.close()

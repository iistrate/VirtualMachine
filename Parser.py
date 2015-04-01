
from Globals import *
import os

class Parser(object):
    """Parses a single .vm file or a whole directory of .vm files"""
    def __init__(self, userInput):
        self.__m_rawCommands = []
        self.__m_rawCommand = []
        self.__m_cursor = 0
        self.__m_finalFileName = userInput

        #populate rawCommands
        if os.path.isfile(userInput):
            self.fileToList(userInput)
        else:
            self.translateFiles(userInput)

    def __str__(self):
        rep = ""
        for command in self.__m_rawCommands:
            rep += "Raw command is: {}\n".format(command) 
        return rep

    def translateFiles(self, dirname):
        for fn in os.listdir(dirname):
            if ".vm" in fn:
                self.fileToList(dirname + fn)

    def fileToList(self, filename):
        #get all VM files
        file = open(filename, 'r')
        for line in file:
            #remove out comments
            indexOfComment = line.find('/')
            line = line[:indexOfComment]
            #remove newlines
            line = line.strip()
            #remove empty lines
            if (line):
                self.__m_rawCommands.append(line)
    
    #name of the final .asm file    
    def getFileName(self):
        return self.__m_finalFileName
     
    #check if we have more untranslated commands
    @property
    def hasMoreCommands(self):
        if self.__m_cursor != len(self.__m_rawCommands): return True
        else: return False
    
    #read the next raw command line
    def advance(self):
        if self.hasMoreCommands:
            #grab the first line
            self.__m_rawCommand = self.__m_rawCommands[self.__m_cursor].split()
            #advance cursor
            self.__m_cursor += 1

    #get command type; set command
    @property
    def commandType(self):
        for command in commandTable:
            if self.__m_rawCommand[0] == command.getKey:
                #return it
                return command.getValue

    #returns first argument of command
    def arg1(self):
        ctype = self.commandType
        #if return don't return anything
        if ctype == C_RETURN:
            return
        #if arithmetic return the actual command
        if ctype == C_ARITHMETIC:
            return self.__m_rawCommand[0]
        else:
            #return argument
            return self.__m_rawCommand[1]

    #returns second argument of command
    def arg2(self):
        ctype = self.commandType 
        if ctype in (C_POP, C_PUSH, C_FUNCTION, C_CALL):
            return self.__m_rawCommand[2] 

    #get raw command
    def getRawCommand(self):
        return self.__m_rawCommand

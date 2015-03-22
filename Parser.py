
from Globals import *
from os import path
from Assoc import *

class Parser(object):
    """Parses a single .vm file"""
    def __init__(self, filename):
        self.__m_file = open(filename, 'r')
        self.__m_rawCommands = []
        self.__m_rawCommand = 0
        self.__m_cursor = 0
        self.__m_commandTable = []

        #get command table
        self.populateCmdTable()
        #populate rawCommands
        self.fileToList()

    def __str__(self):
        rep = ""
        for command in self.__m_rawCommands:
            rep += "Raw command is: {}\n".format(command) 
        return rep

    def fileToList(self):
        for line in self.__m_file:
            #remove out comments
            indexOfComment = line.find('/')
            line = line[:indexOfComment]
            #remove newlines
            line = line.strip()
            #remove empty lines
            if (line):
                self.__m_rawCommands.append(line)

    #check if we have more untranslated commands
    def hasMoreCommands(self):
        if self.__m_cursor != len(self.__m_rawCommands): return True
        else: return False
    
    #read the next raw command
    def advance(self):
        if self.hasMoreCommands():
            self.__m_rawCommands[self.__m_cursor]
            #advance cursor
            self.__m_cursor += 1

    def populateCmdTable(self):
        self.__m_commandTable.append(Assoc("add", C_ARITHMETIC))
        self.__m_commandTable.append(Assoc("sub", C_ARITHMETIC))
        self.__m_commandTable.append(Assoc("neg", C_ARITHMETIC))
        self.__m_commandTable.append(Assoc("eq", C_ARITHMETIC))
        self.__m_commandTable.append(Assoc("gt", C_ARITHMETIC))
        self.__m_commandTable.append(Assoc("lt", C_ARITHMETIC))
        self.__m_commandTable.append(Assoc("and", C_ARITHMETIC))
        self.__m_commandTable.append(Assoc("or", C_ARITHMETIC))
        self.__m_commandTable.append(Assoc("not", C_ARITHMETIC))
        self.__m_commandTable.append(Assoc("push", C_PUSH))
        self.__m_commandTable.append(Assoc("pop", C_POP))
        self.__m_commandTable.append(Assoc("label", C_LABEL))
        self.__m_commandTable.append(Assoc("goto", C_GOTO))
        self.__m_commandTable.append(Assoc("if-goto", C_IF))
        self.__m_commandTable.append(Assoc("function", C_FUNCTION))
        self.__m_commandTable.append(Assoc("call", C_CALL))
        self.__m_commandTable.append(Assoc("return", C_RETURN))



from Globals import *
from os import path

class Parser(object):
    """Parses a single .vm file"""
    def __init__(self, filename):
        self.__m_file = open(filename, 'r')
        self.__m_rawCommands = []
        self.__m_rawCommand = 0
        self.__m_cursor = 0

        #populate rawCommands
        self.fileToList()

    def __str__(self):
        rep = ""
        for command in self.__m_rawCommands:
            rep += "Command is: {}\n".format(command) 
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


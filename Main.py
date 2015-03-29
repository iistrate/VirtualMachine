#
# Virtual Machine for nand2tetris
#

from VirtualMachine import *

from sys import argv
from os import path

def main():
    #open file
    argv = list(range(2)) #comment line when done
    argv[1] = "PointerTest" #comment line when done
    #force .vm extension
    userInput = argv[1] + ".vm" if not (argv[1][-3:] == ".vm") else argv[1]

    if not (path.isfile(userInput)): 
        print("Please enter correct filename")
    else:
        VM = VirtualMachine(userInput)
        VM.run()


if __name__ == '__main__': main()
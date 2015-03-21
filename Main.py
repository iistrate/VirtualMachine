#
# Virtual Machine for nand2tetris
#

from VirtualMachine import *

from sys import argv
from os import path

def main():
    #open file
    try:
        argv[1] = "SimpleAdd"
        #force .vm extension
        userInput = argv[1] + ".vm" if not (argv[1][-3:] is ".vm") else argv[1]
        #check if file exists
        path.isfile(userInput)
    except:
        raise FileNotFoundError("Please enter correct filename")
    finally:
        VM = VirtualMachine(userInput)
        VM.run()


if __name__ == '__main__': main()
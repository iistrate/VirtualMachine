#
# Virtual Machine for nand2tetris
#

from VirtualMachine import *
import os
from sys import argv

def main():
    #get argument 1
    userInput = argv[1]
    if os.path.isfile(userInput) or os.path.isdir(userInput):
        VM = VirtualMachine(userInput)
        VM.run()
    else:
        print("File/dir {} not found".format(userInput))


if __name__ == '__main__': main()
#
# Virtual Machine for nand2tetris
#

from VirtualMachine import *
import os
from sys import argv

def main():
    try:
        #get argument 1
        userInput = argv[1]
    except:
        print("Error. Usage: from cmd python Main.py file.vm OR dir/subdir/")
    else:
        if os.path.isfile(userInput) or os.path.isdir(userInput):
            VM = VirtualMachine(userInput)
            VM.run()
        else:
            print("File/dir {} not found".format(userInput))


if __name__ == '__main__': main()
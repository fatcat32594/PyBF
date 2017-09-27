#!/bin/python
"""Python3 BrainFuck Interpreter"""
import sys

def sanatize(program):
    """Removes excess characters from program"""
    accepted = "<>+-.,[]"
    sanatized = ""
    for char in program:
        if char in accepted:
            sanatized += char
    return sanatized

def read(mode):
    """Get code to be interpreted"""
    if mode == 'i':
        print("Input mode not yet implemented")
        exit()
    elif mode == 'f':
        filename = sys.argv[1]
        try:
            data = open(filename, 'r')
        except IOError:
            print("Error opening file")
            exit()
        program = data.read()
        sanatized_program = sanatize(program)
        return sanatized_program

def main():
    """Main function"""
    arglen = len(sys.argv)
    if arglen == 1:
        mode = 'i'
    elif arglen == 2:
        mode = 'f'
    else:
        print("Number of arguments not understood")
        exit()
    program = read(mode)
    print(program)

if __name__ == "__main__":
    main()

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

def jump(inst_ptr, program, direction):
    """Jump the instruction pointer in the program until matching bracket"""
    count = direction
    while count != 0:
        inst_ptr += direction
        char = program[inst_ptr]
        if char == '[':
            count += 1
        elif char == ']':
            count -= 1
        else:
            pass
    return inst_ptr

def interpret(program):
    """Interpret the program"""
    inst_ptr = 0
    data_ptr = 0
    data = [0]

    while inst_ptr < len(program):
        command = program[inst_ptr]
        if command == '<':
            #Decrement the data pointer
            data_ptr -= 1
            if data_ptr < 0:
                print("Error: attempting to go before data start")
                quit()
        elif command == '>':
            #Increment the data pointer
            data_ptr += 1
            if data_ptr == len(data):
                data += [0]
        elif command == '+':
            #Increment the data at the data pointer
            data[data_ptr] += 1
        elif command == '-':
            #Decrement the data at the data pointer
            data[data_ptr] -= 1
        elif command == '.':
            #Print the data at the data pointer as a character
            print(chr(data[data_ptr]), end='')
        elif command == ',':
            #Read in one character from stdin to the data pointer location
            char = sys.stdin.read(1)
            data[data_ptr] = ord(char)
        elif command == '[':
            #Start of while loop
            if data[data_ptr] == 0:
                inst_ptr = jump(inst_ptr, program, 1)
        elif command == ']':
            #End of while loop
            if data[data_ptr] != 0:
                inst_ptr = jump(inst_ptr, program, -1)
        else:
            print("Error while interpreting program.")
            exit()
        inst_ptr += 1

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
    interpret(program)

if __name__ == "__main__":
    main()

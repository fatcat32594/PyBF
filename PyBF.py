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


def error(err):
    """Print error message and exit"""
    print(err)
    exit()


def move_ptr(command, data_ptr):
    """move the data pointer based on the command"""
    if command == '<':
        data_ptr -= 1
        if data_ptr < 0:
            print("Error: attempting to go before data start")
            quit()
    elif command == '>':
        data_ptr += 1
    else:
        error("Error while interpreting program")
    return data_ptr


def mod_data(command, data):
    """Modify the data based on the command"""
    if command == '+':
        data += 1
    elif command == '-':
        data -= 1
    else:
        error("Error while modifying data")
    return data


def in_out(command, data):
    """Perform I/O operation based on command"""
    if command == '.':
        print(chr(data), end='')
    elif command == ',':
        char = sys.stdin.read(1)
        data = ord(char)
    else:
        error('Error during I/O operation')
    return data


def interpret(program):
    """Interpret the program"""
    inst_ptr = 0
    data_ptr = 0
    data = [0]

    while inst_ptr < len(program):
        command = program[inst_ptr]
        if command in '<>':
            # move data pointer
            data_ptr = move_ptr(command, data_ptr)
            if data_ptr == len(data):
                data += [0]
        elif command in '+-':
            # change data at data pointer
            data[data_ptr] = mod_data(command, data[data_ptr])
        elif command in '.,':
            # Do some I/O
            in_out(command, data[data_ptr])
        elif command == '[':
            # Start of while loop
            if data[data_ptr] == 0:
                inst_ptr = jump(inst_ptr, program, 1)
        elif command == ']':
            # End of while loop
            if data[data_ptr] != 0:
                inst_ptr = jump(inst_ptr, program, -1)
        else:
            error("Error while interpreting program.")
        inst_ptr += 1


def main():
    """Main function"""
    arglen = len(sys.argv)
    if arglen == 1:  # Start interactive mode
        mode = 'i'
    elif arglen == 2:  # Start file mode
        mode = 'f'
    else:
        print("Number of arguments not understood")
        exit()
    program = read(mode)
    interpret(program)


if __name__ == "__main__":
    main()

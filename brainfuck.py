# Name:Brainfuck Interpreter Python
# Date: 2022/09/17
# Repository: https://github.com/BaseMax/BrainfuckInterpreterPython
# Author: Max Base

import sys

def brainfuck(input):
    # >	Move the pointer to the right
    # <	Move the pointer to the left
    # +	Increment the memory cell at the pointer
    # -	Decrement the memory cell at the pointer
    # .	Output the character signified by the cell at the pointer
    # ,	Input a character and store it in the cell at the pointer
    # [	Jump past the matching ] if the cell at the pointer is 0
    # ]	Jump back to the matching [ if the cell at the pointer is nonzero

    # initialize memory
    memory = [0] * 30*1000
    # initialize pointer
    pointer = 0
    # initialize output
    output = ""

    # All characters other than ><+-.,[] should be considered comments and ignored. But, see extensions below.

    # loop through input
    i = 0
    while i < len(input):
        # print("i: {}, input[i]: {}, memory: {}, pointer: {}".format(i, input[i], memory, pointer))
        # >	Move the pointer to the right
        if input[i] == ">":
            pointer += 1
        # <	Move the pointer to the left
        elif input[i] == "<":
            pointer -= 1
        # +	Increment the memory cell at the pointer
        elif input[i] == "+":
            memory[pointer] += 1
        # -	Decrement the memory cell at the pointer
        elif input[i] == "-":
            memory[pointer] -= 1
        # .	Output the character signified by the cell at the pointer
        elif input[i] == ".":
            output += chr(memory[pointer])
        # ,	Input a character and store it in the cell at the pointer
        elif input[i] == ",":
            memory[pointer] = ord(input())
        # [	Jump past the matching ] if the cell at the pointer is 0
        elif input[i] == "[":
            if memory[pointer] == 0:
                # find matching ]
                count = 1
                while count > 0:
                    i += 1
                    if input[i] == "[":
                        count += 1
                    elif input[i] == "]":
                        count -= 1
        # ]	Jump back to the matching [ if the cell at the pointer is nonzero
        elif input[i] == "]":
            if memory[pointer] != 0:
                # find matching [
                count = 1
                while count > 0:
                    i -= 1
                    if input[i] == "]":
                        count += 1
                    elif input[i] == "[":
                        count -= 1
        else:
            pass
        i += 1

    # print(memory)
    return output

# init
### dcode
# input1 = "++++++++ [>++++++++++++>+++++++++++++<<-] >++++. -. >+++++++. <+. +."
### fibunacci
# input2 = "+++++++++++>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]"
### test
# input3 = "+++[>+++++<-]"
### hello world (with deep comments)
# input4 = """
# +++++ +++++             initialize counter (cell #0) to 10
# [                       use loop to set the next four cells to 70/100/30/10
#     > +++++ ++              add  7 to cell #1
#     > +++++ +++++           add 10 to cell #2 
#     > +++                   add  3 to cell #3
#     > +                     add  1 to cell #4
#     <<<< -                  decrement counter (cell #0)
# ]                   
# > ++ .                  print 'H'
# > + .                   print 'e'
# +++++ ++ .              print 'l'
# .                       print 'l'
# +++ .                   print 'o'
# > ++ .                  print ' '
# << +++++ +++++ +++++ .  print 'W'
# > .                     print 'o'
# +++ .                   print 'r'
# ----- - .               print 'l'
# ----- --- .             print 'd'
# > + .                   print '!'
# > .                     print '\n'
# """
### hello world
# input5 = """
# >++++++++[<+++++++++>-]<.
# >++++[<+++++++>-]<+.
# +++++++..
# +++.
# >>++++++[<+++++++>-]<++.
# ------------.
# >++++++[<+++++++++>-]<+.
# <.
# +++.
# ------.
# --------.
# >>>++++[<++++++++>-]<+.
# """

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            print(brainfuck(file.read()))
    else:
        print("Usage: python3 brainfuck.py [file]")

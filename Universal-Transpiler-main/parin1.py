from lex1 import *
from emit1 import *
from parse1 import *
import sys

def main():
    print("PARIN TRANSPILER")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()

    
    lexer = Lexer(input)
    emitter = Emitter("out.cpp")
    parser = Parser(lexer, emitter)

    parser.program() 
    emitter.writeFile() 
    print("YOUR CPP CODE IS READY...")

main()

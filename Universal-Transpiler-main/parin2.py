from lex2 import *
from emit2 import *
from parse2 import *
import sys

def main():
    print("PARIN TRANSPILER")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()

    
    lexer = Lexer(input)
    emitter = Emitter("out.java")
    parser = Parser(lexer, emitter)

    parser.program() 
    emitter.writeFile() 
    print(" YOUR JAVA CODE IS READY...")

main()

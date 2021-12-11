
fin = open("cout.py", "rt")
#output file to write the result to
fout = open("cfout.py", "wt")
#for each line in the input file
data = fin.read()
# print(data)

# Before the first line of the file is read, a single zero is pushed on the stack
import re
def get_indent(s) -> int:
    m = re.match(r' *', s)
    return len(m.group(0))
def add_token(token):
    while token == DEDENT:
#        fout.write("\n")
        fout.write("}")
        break
   
INDENT="indent"
DEDENT="dedent"
indent_stack = [0]
# Before the first line of the file is read, a single zero is pushed on the stack
for line in data.splitlines():
    fout.write("\n")
    fout.write(line)
    indent = get_indent(line)
    # At the beginning of each logical line, the line’s 
    # indentation level is compared to the top of the stack. 
    if indent > indent_stack[-1]:
        # If it is larger, it is pushed on the stack, 
        # and one INDENT token is generated.
        add_token(INDENT)
        indent_stack.append(indent)
    elif indent < indent_stack[-1]:
        while indent < indent_stack[-1]:
            #  If it is smaller, ...
            # all numbers on the stack that are larger are popped off,
            # and for each number popped off a DEDENT token is generated.
            add_token(DEDENT)
            indent_stack.pop()
        if indent != indent_stack[-1]:
            # it must be one of the numbers occurring on the stack; 
            raise IndentationError
while indent_stack[-1]>0:
     # At the end of the file, a DEDENT token is generated for each number 
     # remaining on the stack that is larger than zero.
     add_token(DEDENT)
     indent_stack.pop()





# for line in fin:
# 	#read replace the string and write to output file
# 	fout.write(line.replace('print', 'PRINT'))
    
#close input and output files
fin.close()
fout.close()
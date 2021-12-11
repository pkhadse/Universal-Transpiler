
fin = open("input.py", "rt")
#output file to write the result to
fout = open("cpout.py", "wt")

#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('print', 'PRINT').replace('input', 'INPUT').replace('elif', 'ELIF').replace('if', 'IF').replace('while', 'WHILE').replace('else', 'ELSE').replace('int', 'INT').replace('float', 'FLOAT').replace('char', 'CHAR'))



    
#close input and output files
fin.close()
fout.close()
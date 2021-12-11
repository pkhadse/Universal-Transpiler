
pattern='}'
f = open('jfout.py', 'r')
g = open('tempo2.py', 'w')
l=f.readlines()
f.close()
for ind in range(len(l)):
    if pattern in l[ind]:
        l[ind] = l[ind].replace('}','')
        l[ind]=  "}" + "\n" + l[ind] 
        
        g.write("\n")
for field in l:
    g.write(field)
g.close()



import re
file=open('actual.txt')
intlist=list()
for line in file:
    x=re.findall('[0-9]+',line)
    if x != []:
        for s in x:
            intlist.append(int(s))
print(sum(intlist))

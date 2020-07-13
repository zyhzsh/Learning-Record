fname=input("Enter file name: ")
fh=open(fname)
text=fh.read()
lst=list()
lst=text.split()
lst.sort()
temp=list()
for x in lst:
    if x not in temp:
        temp.append(x)
print(temp)

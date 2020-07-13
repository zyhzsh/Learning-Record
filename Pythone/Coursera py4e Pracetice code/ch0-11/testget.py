counts=dict()
names=['zhu','jane','zhu','lin','lin','jane','zhu']
for name in names:
    counts[name]=counts.get(name,0)+1
x=counts.get('xx',0)
print(counts)

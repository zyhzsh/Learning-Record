name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()
for line in handle:
    if line.startswith("From "):
        words=line.split()
        count[words[1]]=count.get(words[1],0)+1

mostcount=None
mostemail=None
for email,count in count.items():
    if mostcount is None or count>mostcount:
        mostemail=email
        mostcount=count
print(mostemail,mostcount)

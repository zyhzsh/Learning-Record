# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
temp=0.0
count=0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        index=0
        while index < len(line):
            if line[index]==":":
                temp=temp+float(line[index+1:].rstrip())
                count=count+1
            index=index+1
print('Average spam confidence:'+temp/count)

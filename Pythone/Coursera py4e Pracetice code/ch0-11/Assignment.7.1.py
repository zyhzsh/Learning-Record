
while True:
    fname = input("Enter file name: ")
    try:
        fh = open(fname)
    except:
        continue
    for line in fh:
        line=line.upper().rstrip()
        print(line)
    break

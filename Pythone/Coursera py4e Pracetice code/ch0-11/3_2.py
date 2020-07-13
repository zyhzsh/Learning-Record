score = input("Enter Score: ")
try:
    grade=float(score)
except:
    message="Please enter a vaild Score:"
    print(message)
    exit()
if grade>1.0 or grade<0.0:
    message="Please enter a vaild Score:"
    print(message)
    exit()
else:
    if grade>=0.9:
    	result="A"
    elif grade>=0.8:
        result="B"
    elif grade>=0.7:
        result="C"
    elif grade>=0.6:
        result="D"
    elif grade<0.6:
        result="F"
print(result)

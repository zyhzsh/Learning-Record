
again=True
while again==True:
    hrs = input("Enter Hours:")
    try:
        h = float(hrs)
    except:
        message="Please input vaild hours~!"
        print(message)
        continue
    rate=input("Enter Rate:")
    try:
        r=float(rate)
    except:
        message="Please input vaild rate~!"
        print(message)
        continue
    if h>40:
	    result=(h-40)*1.5*r+40*r
    else:
        result=h*r
    print(result)
    again=False

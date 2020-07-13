largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        temp=int(num)
    except:
        print('Invalid input')
        continue
    if largest is None and smallest is None:
        largest=temp
        smallest=temp
    elif temp>largest:
        largest=temp
    elif temp<smallest:
        smallest=temp
print("Maximum is", largest)
print("Minimum is", smallest)

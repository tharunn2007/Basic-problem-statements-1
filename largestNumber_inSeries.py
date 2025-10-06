list=[]
while True:
    number=float(input("Enter number:"))
    if number!=0:
        list.append(number)
    else:
        print("The largest number is:",max(list))

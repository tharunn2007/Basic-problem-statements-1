fibonacci_sequence=int(input("Enter the number of Fibonacci numbers to print (0 to exit): "))
first,second=0,1

if fibonacci_sequence==1:
    print(first)
elif fibonacci_sequence>1:
    print(first)
    print(second)
    for i in range(fibonacci_sequence-2):
        third=first+second
        print(third)
        first,second=second,third
else:
    print("Not possible!")

    

#problem:check for the given input number to be even or odd
#if even then give the half of the number
#if odd then give 3 times the number
X=int(input("ENTER NUMBER:"))
if X%2==0:
    print("Input number is an even number")
    print(X*0.5)
else:
    print("Input number is an odd number")
    print(X*3)
#Stop
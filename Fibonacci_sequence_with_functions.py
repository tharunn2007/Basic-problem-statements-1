
def fibonacci_Sequence(loop_count):
    if loop_count <= 0:
        print("Please enter a positive integer.")
        return
    first, second = 0, 1
    print(first)
    if loop_count > 1:
        print(second)
    for n in range(loop_count - 2):
        third = first + second
        print(third)
        first, second = second, third

while True:
    try:
        loop_count = int(input("Enter the number of Fibonacci numbers to print (0 to exit): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue
    if loop_count == 0:
        print("Exiting.")
        break
    fibonacci_Sequence(loop_count)

print("Standard conversion from centimeters to inches:1 cm = 0.3937 in")
smallest_Centimetervalue=int(input("Enter the smallest centimeter value:"))
largest_Centimetervalue=int(input("Enter the largest centimeter value:"))
step_Centimetervalue=10
for i in range(smallest_Centimetervalue,largest_Centimetervalue+step_Centimetervalue,step_Centimetervalue):
    smallest_inch= smallest_Centimetervalue*0.3937
    largest_inch= largest_Centimetervalue*0.3937
    step_inch=step_Centimetervalue*0.3937
    print(f"Centimeters:{smallest_Centimetervalue:.2f}|Inches:{smallest_inch:.4f}")
    smallest_Centimetervalue+=step_Centimetervalue
    smallest_inch+=step_inch


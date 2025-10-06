init_degree=int(input("Enter the starting degree:"))
final_degree=int(input("Enter the final degree value:"))
step_degree=int(input("Enter the step degree value:"))
#Mistake I made previously:CANT USE range() for float values.
for i in range(init_degree,final_degree,step_degree):
    init_radian=init_degree*0.0174533
    final_radian=final_degree*0.0174533
    step_radian=step_degree*0.0174533
    sin_x= init_radian-(init_radian**3/6)+(init_radian**5/120)-(init_radian**7/5040)
    cos_x=1-(init_radian**2/2)+(init_radian**4/24)-(init_radian**6/720)
#Second mistake I made instead of iterating the value and forming a dictionary key value pair for each radian and its respective value I just ut print value and just spammed uneccessarily
    print(f"Degree: {init_degree:.2f}° | Radian: {init_radian:.4f} | Sin: {sin_x:.6f} | Cos: {cos_x:.6f}")
    init_degree += step_degree
    init_radian += step_radian
if init_degree>=90 and final_degree<=180:
    init_radian=init_degree*0.0174533
    final_radian=final_degree*0.0174533
    step_radian=step_degree*0.0174533
    sin_x= (3.1415-init_radian)-((3.1415-init_radian)**3/6)+((3.1415-init_radian)**5/120)-((3.1415-init_radian)**7/5040)
    cos_x=1-((3.1415-init_radian)**2/2)+((3.1415-init_radian)**4/24)-((3.1415-init_radian)**6/720)
    print(f"Degree: {init_degree:.2f}° | Radian: {init_radian:.4f} | Sin: {sin_x:.6f} | Cos: {cos_x:.6f}")
    #NOTE:HERE THE VALUE FOR INIT_DEGREE SHOULD BE"EQUAL" OR "GREATER."
    #THIS MODEL IS JUST AN APPROXIMATED VERSION SINCE IT WAS A CHALLENGE GIVEN BY MY PROFESSOR TO NOT USE MATH MODULE.



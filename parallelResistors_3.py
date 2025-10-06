while True:
    r1=float(input("Enter resistor1 value:"))
    r2=float(input("Enter resistor2 value:"))
    r3=float(input("Enter resistor3 value:"))
    battery_Voltage=float(input("Enter batter volateg value:"))
    equivalent_Resitance=(r1*r2*r3)/(r1*r2+r2*r3+r3*r1)
    circuit_Current= (battery_Voltage/equivalent_Resitance)
    print("Equivalent resistors of 3 parallel resistors is:",equivalent_Resitance)
    print("Total current flowing through the circuit:",circuit_Current)



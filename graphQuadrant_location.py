while True:
    Abscissa=float(input("Enter the abscissa value:"))
    Ordinate=float(input("Enter the oradinate value:"))
    if Abscissa>0 and Ordinate>0:
        print("QUADRANT ONE")
    elif Abscissa<0 and Ordinate<0:
        print("QUADRANT THREE")
    elif Abscissa<0 and Ordinate>0:
        print("QUADRANT TWO")
    elif Abscissa>0 and Ordinate<0:
        print("QUADRANT FOUR")

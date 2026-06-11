height=float(input("Enter your height in centimeters"))
weight=float(input("Enter your weight in kilograms"))
bmi=weight/(height/100)**2
print("Your BMI is",bmi)
if bmi<=18.4:
    print("You are under-weight")
elif bmi<=24.9:
    print("You are healthy")
elif bmi<=29.9:
    print("You are over-weight")
elif bmi<=34.9:
    print("You are severely over-weight")
elif bmi<=39.9:
    print("You are obeese")
else:
    print("You are severely obeese")
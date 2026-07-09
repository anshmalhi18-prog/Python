cause=input("Did you have a medical cause? Y/N").strip().upper()
if cause=="Y":
    print("You are allowed")
else:
    atten=int(input("What is your attendance"))
    if atten>=75:
        print("You are allowed")
    else:
        print("You are not allowed")
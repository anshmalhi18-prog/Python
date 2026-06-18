print("Please enter marks obtained in five subjects")
sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
total=sub1+sub2+sub3+sub4+sub5
avg=int(total/5)
validRange=range(0,101)

if avg not in validRange:
    print("Invalid Input")

elif avg in range(91,101):
    print("Your grade is A1")

elif avg in range(81,91):
    print("Your grade is A2")

elif avg in range(71,81):
    print("Your grade is B1")

elif avg in range(61,71):
    print("Your grade is B2")

elif avg in range(51,61):
    print("Your grade is C1")

elif avg in range(41,51):
    print("Your grade is C2")

elif avg in range(31,41):
    print("Your grade is D1")

elif avg in range(21,31):
    print("Your grade is D2")

elif avg in range(0,21):
    print("Your grade is E")
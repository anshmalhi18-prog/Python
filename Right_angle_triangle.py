print("Half pattern diamond of a star")
n=int(input("Please enter the number of rows"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
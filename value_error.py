try:
    num=int(input("Please enter a number: "))
except ValueError as ex:
    print("This is an invalid input")
    print(ex)
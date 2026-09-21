def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def add(a,b):
    return a+b

def minus(a,b):
    return a-b

try:
    num1=float(input("Enter your first number: "))
    num2=float(input("Enter your second number: "))

    result=multiply(num1,num2)
    print("The product is: ",result)

    result1=divide(num1,num2)
    print("The quotient is: ",result1)

    result2=add(num1,num2)
    print("The sum is: ",result2)

    result3=minus(num1,num2)
    print("The subtracted value is: ",result3)

except ZeroDivisionError:
    print("Don't enter 0 as one of your numbers")

except ValueError:
    print("You need to enter a number")
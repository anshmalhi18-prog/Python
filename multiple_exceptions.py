try:
    num1,num2=eval(input("Please enter two numbers seperated by a comma: "))
    result=num1/num2
    print("The result is",result)

except ZeroDivisionError:
    print("Division by zero is an error")

except SyntaxError:
    print("Seperate both numbers by using a comma")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("Thank You!!!")
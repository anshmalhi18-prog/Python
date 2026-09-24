def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

print("=" * 36)
print("FUNCTION CALCULATOR")
print("=" * 36)
print("Operations: add / subtract / multiply / divide")
print()

operation = input("Choose operation: ").strip().lower()

result = None
is_valid = True
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        try:
            result = divide(num1, num2)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
            is_valid = False
    else:
        print("Error: Unknown operation.")
        is_valid = False

    if is_valid and result is not None:
        print("Result:", result)

except ValueError:
    print("Error: Please enter numbers. Typing letters is not allowed.")
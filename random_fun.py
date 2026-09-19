import math
import random

lucky_num=random.randint(1,10)
print("Your lucky number is",lucky_num)

fun_choices=["Play a game","Solve a puzzle","Read a story","Draw Something"]
random_activity=random.choice(fun_choices)
print("Random activity for today:", random_activity)

print("\nGuess the secret number from 1 to 5")
secret_number = random.randint(1,5)

while True:
    guess=int(input("\nEnter your guess: "))
    if guess==secret_number:
        print("Correct! You win")
        break
    else:
        print("Wrong! Guess again")

decimal_number=float(input("Enter a decimal number: "))
print("Ceiling Value: ",math.ceil(decimal_number))
print("Floor Value",math.floor(decimal_number))

x=10
y=-5
print("Copy sign result: ",math.copysign(x,y))

negative_number=int(input("Enter anegative number: "))
print("Absolute value: ",math.fabs(negative_number))

num1=int(input("Enter your first number for GCD: "))
num2=int(input("Enter your second number for GCD: "))

print("GCD is", math.gcd(num1,num2))

print("\n===== FUN CALCULATOR SUMMARY =====")
print("Lucky Number:", lucky_num)
print("Random Activity:", random_activity)
print("Secret Number:", secret_number)
print("==================================")
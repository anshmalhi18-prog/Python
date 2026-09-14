import random 
play=True
num=random.randint(0,9)
total_chance=5
print("I will generate a number from 0 to 9 and you have to guess the number. You have a total of 5 chances")
for i in range(1,total_chance+1):
    guess=int(input("Enter your guess: "))
    if guess==num:
        print("Congratulations you guessed the secret number!!")
        break
    elif guess<num:
        print("Your number is too low. Try a higher number")
    else:
        print("Your number is too high. Try a lower number")
    if i==total_chance:
        print("Game Over")
        print("You ran out of chances")
        print("The secret number was: ",num)
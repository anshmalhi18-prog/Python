secret=31
i=1
while i<6:
    hearts=5
    guess=int(input("Enter your guess: "))
    if guess==secret:
        print("Correct")
        break
    elif guess<=31:
        print("Higher")
        hearts=hearts-1
    elif guess>=31:
        print("Lower")
        hearts=hearts-1
    i=i+1
    if i==5:
        print("You lose, the correct answer was",secret)
import random
while True:
    user_action=input("Enter a choice(rock, paper or scissors): ")
    possible_ations=["rock", "paper", "scissors"]
    computer_action=random.choice(possible_ations)
    print(f"\nYou chose {user_action}, and the computer chose {computer_action}")

    if user_action==computer_action:
        print("It's a tie")

    elif user_action=="rock":
        if computer_action=="scissor":
            print("You win")
        else:
            print("You lost")

    elif user_action=="scissor":
        if computer_action=="paper":
            print("You win")
        else:
            print("You lost")

    elif user_action=="paper":
        if computer_action=="scissors":
            print("You win")
        else:
            print("You lost")
    play_again=input("Do you want to play again(y/n)")
    if play_again!="y":
        break

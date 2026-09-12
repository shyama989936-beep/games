
import random

print("===================================")
print("      ROCK PAPER SCISSORS")
print("===================================")

options = ["rock", "paper", "scissors"]

user = input("Enter rock, paper or scissors: ").lower()

if user not in options:
    print("Invalid choice! Please enter rock, paper or scissors.")

else:
    computer = random.choice(options)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie! 🤝")

    elif user == "rock" and computer == "scissors":
        print("You Win! 🎉")

    elif user == "paper" and computer == "rock":
        print("You Win! 🎉")

    elif user == "scissors" and computer == "paper":
        print("You Win! 🎉")

    else:
        print("Computer Wins! 😢")

print("===================================")
print("          GAME OVER")
print("===================================")


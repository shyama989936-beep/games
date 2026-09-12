
import random

print("===================================")
print("       NUMBER GUESSING GAME")
print("===================================")

# Computer 1 se 100 ke beech random number choose karega
number = random.randint(1, 100)

attempts = 0

print("Maine 1 se 100 ke beech ek number socha hai.")
print("Ab tumhe number guess karna hai.")
print()

while True:

    guess = int(input("Enter your guess: "))

    attempts = attempts + 1

    if guess == number:
        print()
        print("Congratulations! 🎉")
        print("Tumne correct number guess kar liya.")
        print("Correct number:", number)
        print("Total attempts:", attempts)
        break

    elif guess < number:
        print("Too Low! ⬆️")
        print("Thoda bada number try karo.")
        print()

    else:
        print("Too High! ⬇️")
        print("Thoda chhota number try karo.")
        print()

print()
print("Thank you for playing!")
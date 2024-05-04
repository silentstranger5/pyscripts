import random

options = ["rock", "paper", "scissors"]
computer_choice = random.randrange(3)

while (user_choice := input("Pick an option: ").lower()) not in options:
    print("Pick a valid option.")

user_choice = options.index(user_choice)
difference = computer_choice - user_choice

if difference == 0:
    print("Tie")
elif difference in [-1, 2]:
    print("You win.")
else:
    print("You lose.")

print(f"Computer chose was {options[computer_choice]}.")

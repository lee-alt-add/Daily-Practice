import random

game_rules = {
    "rock":["scissors","lizard"],
    "scissors":["paper","lizard"],
    "paper":["rock","spock"],
    "lizard":["spock","paper"],
     "spock":["scissors","rock"],
}        


cpu_choice = random.choice(list(game_rules.keys()))

user_choice = input("Enter a choice: ")

if user_choice in  game_rules[cpu_choice]:
    print("You lose!")
elif user_choice == cpu_choice:
    print("Draw")
else:
    print("You win!")
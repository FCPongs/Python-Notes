print("Library, Lists and Methods")

import random #! Library that randomizes

food = ["pizza", "carrots","eggs"] #! This is a list
dinner = random.choice(food) #! Assign dinner to randomize the food list
print(dinner) #! Prints the dinner (randomized)

def get_choices():
    player_choice = input("Enter a choice (rock, paper scissors: ") 
    options = ["rock", "paper", "scissors"] #! List for the computer choice (to be randomized)
    computer_choice = random.choice(options) #! Assign computer_choice to random options
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

choices=get_choices() #! Choices will be assigned to be printed
print(choices) #! Choices will be printed

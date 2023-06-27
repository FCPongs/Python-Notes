import random

print("Function Arguments and IF statements")
#! Functions can receive data when they are called
#! The data are called arguments- funcName(arguments)


def get_choices():
    player_choice = input("Enter a choice (rock, paper scissors:) ") 
    options = ["rock", "paper", "scissors"] #! List for the computer choice (to be randomized)
    computer_choice = random.choice(options) #! Assign computer_choice to random options
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer): #! Here, we have the arguments
    print("You chose "+player+", computer chose "+computer) #* CONCATENATE- Combining strings
    print(f"You chose {player}, computer chose {computer}")  #* FSTRINGS- Simplier way of combining variables
    if player == computer:
        return "Its a tie!"
    elif player == 'rock': #! We use nested-if statements, player==rock and nests if statements under it
        if computer == 'scissors':
            return "Rock smashes scissors! You win."
        else:
            return "Paper covers rock! You lose."
        
    elif player == "paper": #! We use nested-if statements, player==paper and nests if statements under it
        if computer=="rock":
            return "Paper covers rock! You win."
        else:
            return "Scissors cuts paper! You lose."
        
    elif player == "scissors": #! We use nested-if statements, player==paper and nests if statements under it
        if computer=="paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

choices = get_choices()     #! This allows you to access dictionary
result = check_win(choices["player"],choices["computer"])   #! Call check_win and pass choices as arguments

print(result)

#! Example
sampDCTNRY = {"player": "rock", "computer": "paper"} #! Dictionary
p_choice = sampDCTNRY["player"]                      #! We access sampDCTNRY[YourChoice]


        
    


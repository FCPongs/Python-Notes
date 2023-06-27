print("This is all about asking for a user input")
# print('Enter your name:') #! Asking for a user input
# x = input()
# print('Hello, ' + x)

def get_choices(): #! Function that assigns to choices
    player_choice = input("Enter a choice (rock, paper scissors: ")
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

choices=get_choices() #! Choices will be assigned to be printed
print(choices) #! Choices will be printed
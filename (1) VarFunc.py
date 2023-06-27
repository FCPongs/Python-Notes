print('Variables and Functions')

def get_choices(): #! Function that assigns to choices
    player_choice = "rock" #! Variable player_choice
    computer_choice = "paper"

    return player_choice

choice = get_choices()
print(choice)


def greeting():
    return "HI"

greeting() #! Calling the function but it doesnt print with this code
response = greeting() #! So we assign it to a variable
print(response) #! And print it



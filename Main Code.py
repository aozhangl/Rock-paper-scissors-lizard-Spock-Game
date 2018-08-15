#By: Liliana Ao
#An Introduction to Interactive Programming in Python (Part 1) - Week 1
#Mini-project #1: Rock-paper-scissors-lizard-Spock Game

def name_to_number(name):
    if (name == "rock"):
        return 0
    elif (name == "Spock"):
        return 1
    elif (name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    elif (name == "scissors"):
        return 4
    else:
        return "Please enter a valid choice."

def number_to_name(number):
    if (number == 0):
        return "rock"
    elif (number == 1):
        return "Spock"
    elif (number == 2):
        return "paper"
    elif (number == 3):
        return "lizard"
    elif (number == 4):
        return "scissors"
    else:
        return "Please enter an integer from 0 to 4."

def rpsls(player_choice): 
    import random
    print 
    if name_to_number (player_choice) == "Please enter a valid choice.":
        print name_to_number (player_choice)
    else: 
        print "Player chooses " + player_choice + "."
        player_number = name_to_number (player_choice)
        comp_number = random.randrange (0, 5)
        comp_choice = number_to_name (comp_number)
        print "Computer chooses " + comp_choice + "."
        remainder = (comp_number - player_number) % 5
        if ((remainder == 1) or (remainder == 2)):
            print "Computer wins!"
        elif ((remainder == 3) or (remainder == 4)):
            print "Player wins!"
        else:
            print "Player and computer tie!"
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("dynamite")

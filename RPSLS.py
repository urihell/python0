# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    if number == 0 :
        name = 'rock'
    elif number == 1 :
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print ("Invalid option! Do you even know how to play?! Try again!")
        
    return name
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print ("Invalid option! Do you even know how to play?! Try again!")
        
    # convert name to number using if/elif/else
    # don't forget to return the result!
    return number

def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number)%5
    
    
    # use if/elif/else to determine winner
    if difference <= 2 and difference > 0:
        winner = 'Player wins!' 
        
    elif difference >2 and difference <= 4:
        winner = 'Computer wins!' 
        
    elif difference == 0:
        winner = "It's a tie!" 
              
    else:
        print ("Something is wrong")
            
        
    # convert comp_number to name using number_to_name

    comp_name = number_to_name(comp_number)
    # print results
    print ('Player chose ', name)
    print ('Computer chose', comp_name)
    print (winner)
    print ("====")
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



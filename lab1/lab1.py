# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: 
# Student Number:
#

def wins_rock_scissors_paper(player, opponent):
    player = player.lower()
    opponent = opponent.lower()

    winning_rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    if winning_rules.get(player) == opponent:
        return True
    else:
        return False

def factorial():
	return 0


def fibonacci():
	return 0


def sum_to_goal():
	return 0
    

class UpCounter:


class DownCounter:




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
    
#Name: factorial
#Parameters: a number (int)
#Return: a number (int)
#Description: this function is passed a non-negative integer, 
# that we will call n in this description. function returns n! (pronounced n factorial). 
# n! = n * (n-1) * (n-2)... * 1 Thus, 3! = 3 * 2 * 1. Note that 0! is 1 by definition.
def factorial(n):
    if int(n) and n >= 0:
        fact = 1
        for i in range(1 , n+1):
            fact = fact * i
        
    return fact

#Description: this function is passed a non-negative integer, that we will call n in this description. 
# function returns the nth fibonacci number in the fibonacci sequence.
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)           
    

#Parameters: list of numbers, and a goal (number)
#Return: a number
#Description: This function finds the two numbers in the list that sum up to the goal value. 
# Function returns the product of the two numbers
# (the product is the result of multiplying the two numbers together). 
# If there are no two numbers that when summed results in the goal state, function returns 0
def sum_to_goal(numbers, goal):
    
    l = len(numbers)
    
    for i in range(l):
        possibleSecond = goal - numbers[i]
        #check if second number exists within array
        if possibleSecond in numbers:
           return numbers[i] * possibleSecond
    return 0
    

class UpCounter:
    def __init__(self, stepsize=1):
        self.countValue = 0
        self.stepsize = stepsize
        
        def count(self):
            return self.countValue
        
        def update(self):
            self.countValue += self.stepsize

class DownCounter(UpCounter):
    def update(self):
        self.countValue -= self.stepsize
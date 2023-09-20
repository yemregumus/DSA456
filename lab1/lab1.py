"""# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command : python test_lab1.py
#
# Author: Yunus Gumus
# Student Number:150331197
#"""


def wins_rock_scissors_paper(player, opponent):
    player = player.lower()
    opponent = opponent.lower()

    winning_rules = {'rock': 'scissors', 'paper': 'rock','scissors': 'paper'}

    if winning_rules.get(player) == opponent:
        return True
    else:
        return False


def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact


def fibonacci(n):
    if n < 0:
        print('Incorrect input')
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_to_goal(numbers, goal):
    l = len(numbers)
    for i in range(l):
        possibleSecond = goal - numbers[i]

        # Check if second number exists within array

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

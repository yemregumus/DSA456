# copy over your code from lab 1 to this file

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

    
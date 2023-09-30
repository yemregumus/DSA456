#
# Author: YUNUS EMRE GUMUS
# Student Number:150331197
#
# Place the code for your lab 3 here.  Read the specs carefully.
# Function name must be exactly as provided.
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab3.py
#


def factorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return number
    else:
        return number * factorial(number - 1)


def linear_search(values, key):
    if len(values) == 0:
        return -1
    else:
        if values[0] == key:
            return 0
        else:
            result = linear_search(values[1:], key)
            if result == -1:
                return -1
            else:
                return result + 1


def binary_search(list, key, tail=0, head=None):
    if head is None:
        head = len(list) - 1

    if tail > head:
        return -1

    middle = (head + tail) // 2

    if list[middle] == key:
        return middle
    elif list[middle] < key:
        return binary_search(list, key, middle + 1, head)
    else:
        return binary_search(list, key, tail, middle - 1)

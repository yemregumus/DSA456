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
            return 1 + linear_search(values[1:], key)


def binary_search(list, key, low=0, high=None):
	if not isinstance(high, int):
		high = len(list)-1

	if low > high:
		return -1

	mid = (low + high) // 2

	if list[mid] == key:
		return mid
	elif list[mid] < key:
		return binary_search(list,key,mid+1,high)
	else:
		return binary_search(list,key, mid-1, high)
# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def function1(number):
	total=0 				  #total initialized to 0  - #+1

	for i in range(0,number): #n + 2 (initializing i and loop iteration)
		x = (i+1)   		  #+1 (arithmetic operation)
		total+=(x*x)		  #+2 ( multiplication and addition)

	return total			  #+1 
#function one operations = n+2+1+2+1
#T(n) = 4 + n
#This functions time complexity is O(n) since as 'number' increases the number of iterations in the loops also increases linearly.
```


### function 2:

Analyze the following function with respect to number

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6 
	#                1       +1 +1 +1       +1  +1 = 6 constant arithmetic operations
	#T(n) = 1+1+1+1+1+1 = 6
	#Since the number of operations performed does not depend on the size or value of the input, this functions time complexity is O(1) also known as constant time complexity.

```

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list):
	for i in range (0,len(list)-1): 	 #n+2 (initializing i and loop iteration)
		for j in range(0,len(list)-1-i): #n+2 (initializing i and loop iteration)
			if(list[j]>list[j+1]): 		 #+1 constant operation (comparison)
				tmp=list[j] 			 #+1 constant operation
				list[j]=list[j+1]		 #+1 constant operation
				list[j+1]=tmp			 #+1 constant operation

#T(n) = (n * n) + (1+1+1+3) = 6n^2
#Time complexity of fucntion3 is O(n^2) which is quadratic time complexity. 

```
### function 4:

Analyze the following function with respect to number

```python
def function4(number):
	total=1							#total initialized to 1  - #+1
	for i in range(1 to number):	#n + 2 (initializing i and loop iteration)
		total=total*(i+1)			#+1 constant multiplication operation
	return total					#+1 constant operation

#T(n)=((n+1)*...*(n))+(1)+1=O(n!)
#Time complexity for this function is exponential because it has a factorial (total=total*(i+1)) term inside its equation.
```


## In class portion


### Group members
List the members of your group member below:

	* Dev Jigishkumar Shah 
	* Lorenzo Ramos
	* Revon Villava-Rayen
	* Sunchit Singh
	* Yunus Gumus


### Timing Data
Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

--------------------------------------------------------------------------
| Team member 		   | Timing for fibonacci | Timing for sum_to_number | 
|----------------------|----------------------|--------------------------|
| Dev Jigishkumar Shah | 1.58 			      | 0.67                     |
| Yunus Gumus          | 1.99                 | 0.09                     |
| Sunchit Singh        | 3.70                 | 0.23                     |
| Lorenzo Ramos  	   | 3.06 			      | 1.18                     |
| Revon Villava-Rayen  | 4.33                 | 0.109                    |
|----------------------|----------------------|--------------------------|



### Summary 
-----------------------------------------------------
| function          | fastest | slowest | difference|
|-------------------|---------|---------|-----------|
|sum_to_number      | 0.67    | 1.18    | -0.51     |
|fibonacci          | 1.58    | 4.33    | -2.75     |
-----------------------------------------------------


### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.

#difference in syntax

They are both almost the same but slow one is more concise on handling negative input but it might lead to more function calls and it makes the algorithm runs slower in my opinion. 



## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?

The fast version is more efficient because it keeps things simple. It follows the usual rules for the fibonacci sequence without extra complications. It doesn`t have as many special cases for different inputs or conditions to check. This simplicity makes it faster for most situations because it doesn`t get bogged down in extra steps. It`s like taking the direct route instead of going through a maze.

2. Was there a difference in terms of usage of space resource?  Did one algorithm use more/less space (memory)?  

I used memory-profiler in python to measure how much memory both algorithms using. They both gave the result of 55MB, so there is no difference.


3. What sort of conclusions can you draw based on your observations?

I think we analyze solutions for to measure how much time they use more than how much memory. Because time is the most precious resource we have. We can get more powerfull computer if needed (not all the time of course we cant build a super computer at home), but if we need a billion years to run a algorithm thats not going to work. So if we give bigger inputs to these functions, because they have exponential time complexity O(n^2)they might take years to complete running.







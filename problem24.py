'''A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?'''

from itertools import permutations

if __name__ == "__main__":
	# This is a naive solution using existing permutations library of python3
	
	x = list(permutations([i for i in range(10)]))
	x = ["".join([str(i) for i in j]) for j in x]
	x.sort()
	
	print(x[1000000 - 1])
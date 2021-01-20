"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included."""

import operator

def get_factorial(n: int, tot: int = 1) -> int:
	if n == 1 or n == 0:
		return tot
	else:
		return get_factorial(n - 1, n * tot)

if __name__ == "__main__":
	# Dictionary to store factorial of all digits from 0 to 9
	facts = {k: get_factorial(k) for k in range(10)}
	
	total_sum = 0
	# Brute force till 99,99,999 because factorial of 7*9! can't be greater than 99,99,999
	for i in range(3, 9999999):
		num_list = list(map(int, list(str(i))))
		
		sum_list = sum([facts[i] for i in num_list])
			
		if i == sum_list:
			print(i)
			total_sum += i
	print("Total sum: {}".format(total_sum))


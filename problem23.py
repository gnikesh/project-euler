# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 
# is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and 
# it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as 
# the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis 
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant 
# numbers is less than this limit.
#
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def is_abundant(n):
	if sum(find_factors(n)) > n:
		return True
	return False

def find_factors(n):
	factors = []

	# Checking only first n / 2 numbers suffices to find proper divisors
	for i in range(1, n//2 + 1):
		if n % i == 0:
			factors.append(i)
	return factors


if __name__ == "__main__":
	
	total = 0
	m = 1

	# Dictionary to save numbers that are evaluated to be either abundant or not abundant
	# For each number, it stores True or False
	abundant_yes_no = {}

	for i in range(1, 28123 + 1):
		# Flag to denote if i is our required number
		choice = 1
		for j in range(1, i):
			if not (i - j) in abundant_yes_no:
				abundant_yes_no[i - j] = is_abundant(i - j)
			
			if not j in abundant_yes_no:
				abundant_yes_no[j] = is_abundant(j)

			if abundant_yes_no[i - j] and abundant_yes_no[j]:
				choice = 0
				break
			
		if choice == 1:
			total += i
		
	print(total)
	# 4179871
	# [Finished in 21.6s]






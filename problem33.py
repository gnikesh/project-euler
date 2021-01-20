"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to 
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.
"""
from math import gcd
	

if __name__ == "__main__":
	numr_mul = 1
	deno_mul = 1
	for numr in range(10,100):
		for denom in range(10, 100):
			if numr % 10 == 0:
				break
			elif denom % 10 == 0:
				continue

			deno_list = list(str(denom))
			commons = []
			
			for letter in list(str(numr)):
				if letter in deno_list:
					commons.append(letter)

			for letter in commons:
				new_numr = str(numr).replace(letter, "")
				new_deno = str(denom).replace(letter, "")
				
				if new_numr and new_deno:
					new_numr = int(new_numr)
					new_deno = int(new_deno)

					if (new_numr / new_deno == numr / denom) and (numr / denom < 1):
						numr_mul *= numr
						deno_mul *= denom

	com_div = gcd(numr_mul, deno_mul)
	print(deno_mul/com_div)

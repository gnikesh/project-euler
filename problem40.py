"""An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

if __name__ == "__main__":
	decimal_string = "0."
	increment = 1
	product = 1
	
	for i in range(1, 1000000):
		decimal_string += str(i)
		if i % increment == 0:
			product *= int(decimal_string[i + 1])
			increment *= 10
	print(product)
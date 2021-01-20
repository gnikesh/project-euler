"""The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""

def is_palindrome(x):
	if len(x) == 1:
		return True
	string_length = len(x)
	start = 0
	end = string_length - 1
	while start <= end:
		if not x[start] == x[end]:
			return False
		start += 1
		end -= 1
	return True


def convert_to_binary(num):
	return bin(num)[2:]
	

if __name__ == "__main__":
	total_sum = 0
	for i in range(1, 1000000):
		if is_palindrome(str(i)) and is_palindrome(convert_to_binary(i)):
			total_sum += i

	print(total_sum)

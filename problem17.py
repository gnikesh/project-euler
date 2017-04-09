ONES = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
DOUBLE = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
HUNDREDS = ['hundred', 'thousand']

sum = 0
for i in range(1, 1001):
	number = i
	word = ""
	length = len(str(number));
	if length == 1:
		word = ONES[number - 1]
	elif number == 10:
		word = TENS[0]
	elif number == 20:
		word = TENS[1]
	elif length == 4:
		word = ONES[number // 1000 - 1] + HUNDREDS[1]
	elif (length == 2) and (number > 10 and number < 20):
		word = DOUBLE[number - 10 - 1]
	elif length == 2 and number > 20:
		if number % 10 == 0:
			word = TENS[number // 10 - 1]
		else:
			word = TENS[(number // 10) - 1] + ONES[(number % 10) - 1]
	elif (length == 3):
		if number % 100 == 0:
			word = ONES[number // 100 - 1] + HUNDREDS[0]
		else:
			hundredth_pos = ONES[number // 100 - 1] + HUNDREDS[0]
			number = number % 100
			if number % 10 == 0:
				tenth_pos = TENS[number // 10 - 1]
			elif number < 10:
				tenth_pos = ONES[number % 10 - 1]
			elif number > 10 and number < 20:
				tenth_pos = DOUBLE[number % 10 - 1]
			else:
				tenth_pos = TENS[number // 10 - 1] + ONES[number % 10 - 1]
			word =  hundredth_pos + 'and' + tenth_pos

	sum += len(word)

print("SUM: ", sum)
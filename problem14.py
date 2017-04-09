LIMIT = 1000000
DONE = [0] * LIMIT
LENGTH = [0] * LIMIT
MAX_LENGTH = 1
NUMBER = 1

def collatzFunction(n):
	global DONE, LENGTH, MAX_LENGTH, NUMBER
	temp = n
	count = 1

	while n != 1:
		if n % 2 == 0:
			n = int(n / 2)
		else:
			n = int(3 * n + 1)

		if n < LIMIT and DONE[n - 1] == 1:
			count += LENGTH[n - 1]
			break
		count += 1

	DONE[temp - 1] = 1
	LENGTH[temp - 1] = count

	if count > MAX_LENGTH:
		MAX_LENGTH = count
		NUMBER = temp
	
for i in range(1, LIMIT):
	collatzFunction(i)
	print(i)

print("NO: ", NUMBER, " STEPS: ", MAX_LENGTH)

amicable_array = []
total_sum = 0
def d(a):
	n = a
	sum = 0
	for i in range(1, n // 2 + 1):
		if n % i == 0:
			sum += i
	return sum

for i in range(1, 10000):
	if i == d(d(i)) and i != d(i):
		amicable_array.append(i)
		print(i)


print ("SUM:: ", sum(amicable_array))
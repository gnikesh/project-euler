sum = 0
for i in range(1, 1001):
	print(i)
	sum += i ** i
print(str(sum)[-10:])
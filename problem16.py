NUMBER = 2 ** 1000
sum = 0
r = 0
while NUMBER != 0:
	r = NUMBER % 10
	sum += r
	NUMBER = NUMBER // 10

print(sum)
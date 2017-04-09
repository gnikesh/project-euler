total_sum = 0
for i in range(2, 300000):
	s = sum([int(x) ** 5 for x in str(i)])
	if i == s:
		total_sum += i
		print (i)


print ("SUM: ", total_sum) 
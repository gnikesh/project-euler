NUMBER = 100
product = 1
sum = 0
for i in range(1, NUMBER + 1):
	product = product * i

for i in str(product):
	sum += int(i)

print(sum)
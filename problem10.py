''' Very Primite and Slow Solution. Takes more than an hour to compute the sum'''
sum = 0
prime = 2
nextPrimeCheck = 3
while prime < 2000000:
	sum += prime
	nextPrimeFound = False
	print(prime)
	while nextPrimeFound != True:
		for i in range(2, nextPrimeCheck//2 + 1):
			if nextPrimeCheck % i == 0:
				nextPrimeCheck += 1	
				break
		else:
			prime = nextPrimeCheck
			nextPrimeFound = True
	nextPrimeCheck += 1

print("SUM: ", sum)

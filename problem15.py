def fact(m, n):
	if m == 1:
		return n
	else:
		return fact(m-1, n*m)

if __name__ == "__main__":
	m, n = 20, 20
	
	# Number of lattice paths from (0, 0) to (x, y) is C(x+y, x) which is given by (x+y)! / (y! * (x + y - y)!)
	print(fact(m+n, 1) / (fact(m, 1) * fact(n, 1)))
"""If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

"""

if __name__ == "__main__":
	
	highest_solutions = 0
	corresponding_p = 0
	for p in range(2, 1001):
		total_solutions = 0
		for a in range(2, 1001):
			if p == a:
				continue

			if not (p * (p - 2* a)) % (2 * (p - a)) == 0:
				continue

			total_solutions += 1
		
		if total_solutions > highest_solutions:
			highest_solutions = total_solutions
			corresponding_p = p


	print(corresponding_p)


					
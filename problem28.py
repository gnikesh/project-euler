'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

# 1) brute-force approach
def get_sum(m, n):
	m_n_matrix = [[0 for i in range(m)] for i in range(n)]
	
	y, x = [int(m//2), int(n//2)]

	move_right, move_down, move_left, move_up = 1, 1, 2, 2
	
	fill = 1
	m_n_matrix[y][x] = fill
	
	# Generate the spiral matrix
	for _ in range(1, m * n + 1):
		for i in range(move_right):
			if fill >= m * n:
				break
			x += 1
			fill += 1
			m_n_matrix[y][x] = fill
			

		for i in range(move_down):
			if fill >= m * n:
				break
			y += 1
			fill += 1
			m_n_matrix[y][x] = fill
			

		for i in range(move_left):
			if fill >= m * n:
				break
			x -= 1
			fill += 1
			m_n_matrix[y][x] = fill
			

		for i in range(move_up):
			if fill >= m * n:
				break
			y -= 1
			fill += 1
			m_n_matrix[y][x] = fill
			

		move_right += 2
		move_down += 2
		move_left += 2
		move_up += 2
	
	# Calculate the sum
	total_sum = 0
	for i in range(m):
		total_sum += m_n_matrix[i][i]

		if not (m - i - 1) == i:
			total_sum += m_n_matrix[m - i - 1][i]

	return total_sum

	
# 2) Each points on diagonal for a n * n square where n is odd and n >= 3 are given by (n ^ 2 - n + 1), (n ^ 2), (n ^ 2 - 2 * n + 2), (n ^ 2 - 3 * n + 3)
# So, we can sum the all diagonal points.
def get_spiral_sum(n):
    return sum([4 * n ** 2 - 6 * n + 6 for n in range(3, 1002, 2)]) + 1


if __name__ == "__main__":
	print(get_sum(1001, 1001))
	print(get_spiral_sum(1001))
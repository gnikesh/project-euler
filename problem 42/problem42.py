"""The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical 
position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text 
file containing nearly two-thousand common English words, how many are triangle words?
"""

if __name__ == "__main__":
	triangle_numbers = set([int(1 / 2 * n * (n + 1)) for n in range(1, 100000)])
	triangle_words = 0
	alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	numbers = list([i for i in range(1, 27)])
	alphabet_dict = {k: v for k, v in zip(alphabets, numbers)}

	with open("words.txt", "r") as fp:
		words_list = [i.strip('"') for i in fp.readline().split(",")]
		for word in words_list:
			value = sum([alphabet_dict.get(i) for i in word])
			if value in triangle_numbers:
				triangle_words += 1
	print(triangle_words)



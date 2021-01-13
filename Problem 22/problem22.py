def get_worth(name):
	alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	name_worth = sum([alphabets.index(ch) + 1 for ch in list(name)])
	return name_worth


if __name__ == "__main__":
	with open("names.txt", "r") as fp:
		names_list = fp.readline().replace('"', "").split(",")

	names_list.sort()
	total_score = 0
	for idx, name in enumerate(names_list):
		total_score += (idx+1) * get_worth(name)
	
	print(total_score)

#!/usr/bin/python


if __name__ == "__main__":

	# Part 1 Solution
	
	with open("day1_input", "r") as infile:
		text = infile.read().strip()
	
	print(text.count("(") - text.count(")"))
	
	# Part 2 Solution
	
	count = 0
	for idx, char in enumerate(text):
		if char == "(":
			count += 1
		else:
			count -= 1
		if count < 0:
			print(idx+1)
			break

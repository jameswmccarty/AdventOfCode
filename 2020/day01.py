#!/usr/bin/python

if __name__ == "__main__":
	

	# Part 1 Solution
	entries = []
	
	with open("day01_input", 'r') as infile:
		entries = [int(f) for f in infile.readlines()]

	while len(entries) > 0:
		head = entries.pop()
		for entry in entries:
			if head + entry == 2020:
				print(head*entry)
				break

	# Part 2 Solution
	entries = []
	doubles = []
	with open("day01_input", 'r') as infile:
		entries = [int(f) for f in infile.readlines()]
	for a in entries:
		for b in entries:
			if a != b:
				doubles.append((a+b, a*b))
	for a in entries:
		for b in doubles:
			if a+b[0] == 2020:
				print(a*b[1])
				exit()

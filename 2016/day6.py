#!/usr/bin/python

def solve(lines, pt2=False):
	rev = True
	if pt2:
		rev = False
	out = ''
	for i in range(len(lines[0])):
		letters = dict()
		for line in lines:
			if line[i] in letters:
				letters[line[i]] += 1
			else:
				letters[line[i]] = 1
		out += sorted(letters.items(), key=lambda a:a[1], reverse=rev)[0][0]
	return out

if __name__ == "__main__":

	# Part 1 Solution

	lines = []

	with open("day6_input", "r") as infile:
		for line in infile.readlines():
			lines.append(line.strip())
	print solve(lines)
	# Part 2 Solution
	print solve(lines,True)

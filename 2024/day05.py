#!/usr/bin/python

# Advent of Code 2024 Day 05

def test(line, rules):
	line = line.strip().split(',')
	for idx, entry in enumerate(line):
		applicable = [rule for rule in rules if rule[0] == entry and rule[1] in line]
		for x, y in applicable:
			if line.index(y) < idx:
				return 0
	return int(line[len(line)//2])

def test_sort(line, rules):
	line = line.strip().split(',')
	while True:
		modified = False
		for idx, entry in enumerate(line):
			applicable = [rule for rule in rules if rule[0] == entry and rule[1] in line]
			for x, y in applicable:
				if line.index(y) < idx:
					other_idx = line.index(y)
					new_line = line[:]
					new_line[idx] = y
					new_line[other_idx] = x
					line = new_line
					modified = True
					break
		if not modified:
			break
	return int(line[len(line)//2])

if __name__ == "__main__":

	# Part 1 Solution
	incorrects = []
	rules = []
	total = 0
	with open("day05_input", "r") as infile:
		for line in infile:
			if '|' in line:
				x,y = line.strip().split('|')
				rules.append((x,y))
			if ',' in line:
				result = test(line, rules)
				if result == 0:
					incorrects.append(line)
				else:
					total += result
	print(total)

	# Part 2 Solution
	total = 0
	for line in incorrects:
		total += test_sort(line, rules)
	print(total)


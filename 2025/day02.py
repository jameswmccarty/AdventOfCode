#!/usr/bin/python

# Advent of Code 2025 Day 02

if __name__ == "__main__":

	# Part 1 Solution
	with open("day02_input", "r") as infile:
		line = infile.read().strip()
	bounds = []
	for entry in line.split(','):
		lo, hi = entry.split('-')
		bounds.append((int(lo), int(hi)))

	i = 1
	total = 0
	while len(str(i)) < 6:
		val = int(str(i)+str(i))
		for lo, hi in bounds:
			if val >= lo and val <= hi:
				total += val
		i += 1
	print(total)


	# Part 2 Solution
	i = 1
	total = 0
	seen = set()
	while len(str(i)) < 6:
		k = 2
		while len(str(i)*k) <= 10:
			val = int(str(i)*k)
			for lo, hi in bounds:
				if val >= lo and val <= hi and val not in seen:
					total += val
					seen.add(val)
			k += 1
		i += 1
	print(total)


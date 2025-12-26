#!/usr/bin/python

# Advent of Code 2024 Day 25

def fits(lock, key):
	return not any(key[i]+height > 5 for i,height in enumerate(lock))

def parse(diag):
	return [sum(diag[i][x] == '#' for i in range(1,6)) for x in range(5)]

if __name__ == "__main__":

	# Part 1 Solution
	keys = []
	locks = []
	with open("day25_input", "r") as infile:
		maps = infile.read().split('\n\n')
	for entry in maps:
		diag = entry.split()
		if diag[0] == '#'*5:
			locks.append(parse(diag))
		else:
			keys.append(parse(diag))
	print(sum(fits(key, lock) for lock in locks for key in keys))


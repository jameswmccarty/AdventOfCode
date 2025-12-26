#!/usr/bin/python


if __name__ == "__main__":

	# Part 1 Solution
	with open("day01_input", "r") as infile:
		food = infile.read().split("\n\n")
	sums = sorted([ sum([int(y) for y in x.split()]) for x in food ], reverse=True)
	print(sums[0])

	# Part 2 Solution
	print(sum(sums[0:3]))

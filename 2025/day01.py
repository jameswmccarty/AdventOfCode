#!/usr/bin/python

# Advent of Code 2025 Day 01

if __name__ == "__main__":

	# Part 1 Solution
	pos = 50
	count = 0
	with open("day01_input", "r") as infile:
		for line in infile:
			rot, val = line[0], int(line[1:])
			pos = (pos + val * [-1,1][rot=='R']) % 100
			if pos == 0:
				count += 1
	print(count)

	# Part 2 Solution
	pos = 50
	count = 0
	with open("day01_input", "r") as infile:
		for line in infile:
			rot, val = line[0], int(line[1:])
			count += val // 100
			val %= 100
			old_pos = pos
			pos = (pos + val * [-1,1][rot=='R'])
			if pos*old_pos < 0 or pos > 100:
				count += 1
			pos %= 100
			if pos == 0:
				count += 1
	print(count)

#!/usr/bin/python

# Advent of Code 2025 Day 04

def adjacent_count(pos, rolls):
	x, y = pos
	count = 0
	for j in (-1,0,1):
		for i in (-1, 0, 1):
			if not (j == 0 and i == 0):
				if (x+i, y+j) in rolls:
					count += 1
	return count

def count_and_remove(rolls):
	total_removed = 0
	last_size = -1
	while len(rolls) != last_size:
		last_size = len(rolls)
		reachable = { p for p in rolls if adjacent_count(p, rolls) < 4 }
		total_removed += len(reachable)
		for roll in reachable:
			rolls.discard(roll)
	return total_removed

if __name__ == "__main__":

	rolls = set()
	with open("day04_input", "r") as infile:
		y = 0
		for line in infile:
			for x, char in enumerate(line.strip()):
				if char == "@":
					rolls.add((x, y))
			y += 1

	print(len([p for p in rolls if adjacent_count(p, rolls) < 4]))
	print(count_and_remove(rolls))


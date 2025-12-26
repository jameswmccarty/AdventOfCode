#!/usr/bin/python

# Advent of Code 2025 Day 07

memo = dict()
splitters = set()
max_y = None
def splitter_total(pos):
	if pos in memo:
		return memo[pos]
	x, y = pos
	if y > max_y:
		return 0
	if (x, y+1) not in splitters:
		memo[pos] = splitter_total((x, y+1))
		return memo[pos]
	left = splitter_total((x-1, y+1))
	right = splitter_total((x+1, y+1))
	memo[pos] = 1 + left + right
	return memo[pos]

if __name__ == "__main__":

	split_count = 0
	start = None
	with open("day07_input", "r") as infile:
		y = 0
		for line in infile.readlines():
			for x, char in enumerate(line.strip()):
				if char == "S":
					start = (x, y)
				elif char == "^":
					splitters.add((x, y))
			y += 1
	max_y = y
	y = start[1]
	beams = { start }
	while y < max_y:
		next_beams = set()
		for beam in beams:
			x, y = beam
			if (x, y+1) not in splitters:
				next_beams.add((x, y+1))
			else:
				split_count += 1
				next_beams.add((x-1, y+1))
				next_beams.add((x+1, y+1))
		beams = next_beams
		y += 1
	print(split_count)

	print(splitter_total(start)+1)

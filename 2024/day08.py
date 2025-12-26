#!/usr/bin/python

# Advent of Code 2024 Day 08


if __name__ == "__main__":

	# Part 1 Solution
	antennas = dict()
	antinodes = dict()
	x_range = 0
	y_range = 0
	with open("day08_input", "r") as infile:
		y = 0
		for line in infile:
			for x, char in enumerate(line.strip()):
				if char != '.':
					if char not in antennas:
						antennas[char] = set()
						antinodes[char] = set()
					antennas[char].add((x,y))
			x_range = len(line.strip())
			y += 1

	y_range = y

	for antenna_freq, locations in antennas.items():
		locations = list(locations)
		for a in locations:
			for b in locations:
				if a != b:
					dx, dy = a[0]-b[0], a[1]-b[1]
					antinodes[antenna_freq].add((a[0]+dx, a[1]+dy))

	total_unique_locs = set()
	for antenna_freq, antinode_set in antinodes.items():
		total_unique_locs = {*total_unique_locs, *antinode_set}

	total_unique_locs = { (x,y) for x,y in total_unique_locs if x >= 0 and y >= 0 and x < x_range and y < y_range }

	print(len(total_unique_locs))

	# Part 2 Solution
	antinodes = dict()
	for key in antennas:
		antinodes[key] = {*antennas[key]}
	for antenna_freq, locations in antennas.items():
		locations = list(locations)
		for a in locations:
			for b in locations:
				if a != b:
					dx, dy = a[0]-b[0], a[1]-b[1]
					nx, ny = a[0]+dx, a[1]+dy
					while nx >= 0 and ny >= 0 and nx < x_range and ny < y_range:
						antinodes[antenna_freq].add((nx, ny))
						nx, ny = nx+dx, ny+dy

	total_unique_locs = set()
	for antenna_freq, antinode_set in antinodes.items():
		total_unique_locs = {*total_unique_locs, *antinode_set}

	total_unique_locs = { (x,y) for x,y in total_unique_locs if x >= 0 and y >= 0 and x < x_range and y < y_range }
	print(len(total_unique_locs))

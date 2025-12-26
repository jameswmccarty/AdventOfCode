#!/usr/bin/python


grid = []

def traverse_grid(slope, inc):
	x = 0
	y = 0
	hits = 0
	while y < len(grid):
		if grid[y][x%len(grid[0])] == '#':
			hits += 1
		x += slope
		y += inc
	return hits


if __name__ == "__main__":

	# Part 1 Solution
	
	with open("day03_input", 'r') as infile:
		grid = [ line.strip() for line in infile.readlines() ]
	print(traverse_grid(3,1))


	# Part 2 Solution
	sol = 1
	for x,y in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
		sol *= traverse_grid(x,y)
	print(sol)


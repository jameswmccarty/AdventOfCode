#!/usr/bin/python


def adj_on(x, y, grid):
	count = 0
	for j in range(max(0,y-1),min(len(grid),y+2)):
		for i in range(max(0,x-1),min(len(grid[0]),x+2)):
			if not (i==x and j==y) and grid[j][i]== '#':
				count += 1
	return count
	
def count_on(grid):
	count = 0
	for row in grid:
		count += row.count("#")
	return count
	
def print_grid(grid):
	for row in grid:
		print ''.join(row)
	print
	
def next_grid(grid):
	next_gen = []
	for y, row in enumerate(grid):
		next_row = []
		for x, char in enumerate(row):
			nc = '.'
			adj = adj_on(x, y, grid)
			if char == '#' and (adj == 2 or adj == 3):
				nc = '#'
			elif char == '.' and adj == 3:
				nc = '#'
			next_row.append(nc)
		next_gen.append(next_row)
	return next_gen		

	
if __name__ == "__main__":

	# Part 1 Solution
	
	grid = []
	
	with open("day18_input", "r") as infile:
		for line in infile.readlines():
			grid.append(list(line.strip()))
			
	for i in range(100):
		#print_grid(grid)
		grid = next_grid(grid)
	print count_on(grid)
	
	# Part 2 Solution
	grid = []
	
	with open("day18_input", "r") as infile:
		for line in infile.readlines():
			grid.append(list(line.strip()))
	# Turn on corners
	grid[0][0] = '#'
	grid[len(grid)-1][0] = '#'
	grid[0][len(grid[0])-1] = '#'
	grid[len(grid)-1][len(grid[0])-1] = '#'
	for i in range(100):
		#print_grid(grid)
		grid = next_grid(grid)
		grid[0][0] = '#'
		grid[len(grid)-1][0] = '#'
		grid[0][len(grid[0])-1] = '#'
		grid[len(grid)-1][len(grid[0])-1] = '#'
	print count_on(grid)
	
	

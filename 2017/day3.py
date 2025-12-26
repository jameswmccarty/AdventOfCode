#!/usr/bin/python


if __name__ == "__main__":
    # Part 1 Solution
	data = 325489
	
	# We have a spiral shape on a grid
	# Odd Squares (9, 25, 49, ...) are on lower right-hand corners
	# An Odd Squares distance from center is N - 1 for N^2 (i.e. 9 is 2, 25 is 4, etc)
	
	# Find the first odd square larger than our input
	ring = 1
	while ring*ring < data:
		ring += 2
	
	# Our input is on the perimeter of the NxN square
	# Find out how far we need to walk around the perimeter
	remainder = (ring*ring) - data
	# sides are symmetrical, so trim off multiples of N
	remainder %= (ring-1)
	
	side = [0] * ring
	corner_distance = ring - 1  #An Odd Squares distance from center is N - 1
	side[0] = corner_distance
	# One fewer step distance as we approach centerline from the corner
	for i in range(1,ring/2 + 1):
		side[i] = side[i-1] - 1
	for i in range(ring/2 + 1,ring):
		side[i] = side[i-1] + 1
	print side[remainder]

	# Part 2 Solution
	
	grid_size = 200 # big enough 2D grid
	
	grid = [[0] * grid_size for i in range(grid_size)]
	
	grid[grid_size/2][grid_size/2] = 1 # start from center
	x = (grid_size / 2) 
	y = (grid_size / 2) 
	
	dirs = ['E', 'N', 'W', 'S']
	dir_idx = 0
	side_max = 1
	step = 0
	toggle = 0
	start = True
	
	while True:
		# sum the grid point
		if not start:
			grid[y][x] = grid[y-1][x+1] + grid[y-1][x] + grid[y-1][x-1] + grid[y+1][x+1] + grid[y+1][x] + grid[y+1][x-1] + grid[y][x-1] + grid[y][x+1]
		else:
			start = False
		
		if grid[y][x] > data:
			print grid[y][x]
			break
		
		if step == side_max:
			if toggle == 1:
				toggle = 0
				side_max += 1
			else:
				toggle = 1
			step = 0
			dir_idx += 1
			dir_idx %= 4			
		
		if dirs[dir_idx]   == 'N':
			y -= 1
		elif dirs[dir_idx] == 'W':
			x -= 1
		elif dirs[dir_idx] == 'E':
			x += 1
		elif dirs[dir_idx] == 'S':
			y += 1
		
		step += 1



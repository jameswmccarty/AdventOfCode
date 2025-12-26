#!/usr/bin/python


if __name__ == "__main__":

	flashed = set()
	levels  = dict()
	flash_count = 0

	adj_steps = []
	for j in (-1,0,1):
		for i in (-1,0,1):
			adj_steps.append((i,j))
	adj_steps.remove((0,0))
			
	def flash_adjacent(coord):
		global flash_count
		global flashed
		global levels
		flashed.add(coord)
		x,y = coord
		flash_count += 1
		levels[coord] = 0
		for dx,dy in adj_steps:
			nx = x+dx
			ny = y+dy
			if nx >=0 and nx < 10 and ny >= 0 and ny < 10:
				if (nx,ny) not in flashed:
					levels[(nx,ny)] += 1
					if levels[(nx,ny)] > 9:
						flash_adjacent((nx,ny))			

	# Part 1 Solution
	with open("day11_input","r") as infile:
		lines = infile.read().strip().split('\n')
	
	for j,line in enumerate(lines):
		for i,char in enumerate(line):
			levels[(i,j)] = int(char)
	
	for step in range(100):
		flashed = set()
		for entry in levels:
			levels[entry] += 1
		for entry in levels:
			if levels[entry] > 9:
				flash_adjacent(entry)
	
	print(flash_count)
				

	# Part 2 Solution
	
	levels  = dict()
	flashed = set()
	
	for j,line in enumerate(lines):
		for i,char in enumerate(line):
			levels[(i,j)] = int(char)
	
	step = 0
	while len(flashed) != 100:
		flashed = set()
		for entry in levels:
			levels[entry] += 1
		for entry in levels:
			if levels[entry] > 9:
				flash_adjacent(entry)
		step += 1
	print(step)

	

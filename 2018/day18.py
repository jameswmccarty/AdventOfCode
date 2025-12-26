#!/usr/bin/python


map = []

def score():
	yards = 0
	trees = 0
	for row in map:
		for char in row:
			if char == "|":
				trees += 1
			elif char == "#":
				yards += 1
	return trees * yards

def score2():
	yards = 0
	trees = 0
	mrt = 0
	mry = 0
	for row in map:
		for char in row:
			if char == "|":
				trees += 1
			elif char == "#":
				yards += 1
		mrt = max(mrt, row.count("|"))
		mry = max(mry, row.count("#"))
	return (trees, yards, mrt, mry)	

def cellcount(loc):
	yards = 0
	trees = 0
	open  = 0
	adj_contents = []
	x, y = loc
	if x > 0:
		if y > 0:
			adj_contents.append(map[y-1][x-1])
		adj_contents.append(map[y][x-1])
		if y < len(map)-1:
			adj_contents.append(map[y+1][x-1])
	if y > 0:
		adj_contents.append(map[y-1][x])
	if y < len(map)-1:
		adj_contents.append(map[y+1][x])
	if x < len(map[0])-1:
		adj_contents.append(map[y][x+1])
		if y > 0:
			adj_contents.append(map[y-1][x+1])
		if y < len(map)-1:
			adj_contents.append(map[y+1][x+1])
	return (adj_contents.count("#"), adj_contents.count("|"), adj_contents.count("."))
		

def grow(map):
	next = []
	for i, map_row in enumerate(map):
		n_gen_row = [None] * len(map[0])
		for j, cell in enumerate(map_row):
			y,t,o = cellcount((j,i))
			if map[i][j] == '.':
				if t >= 3:
					n_gen_row[j] = "|"
				else:
					n_gen_row[j] = '.'
			elif map[i][j] == '|':
				if y >= 3:
					n_gen_row[j] = '#'
				else:
					n_gen_row[j] = '|'
			elif map[i][j] == '#':
				if t >= 1 and y >= 1:
					n_gen_row[j] = "#"
				else:
					n_gen_row[j] = '.'
		next.append(n_gen_row)
	return next

if __name__ == "__main__":

	# Part 1 Solution
	map = []	
	with open("day18_input", "r") as infile:
		for line in infile.readlines():
			map.append(list(line.strip()))	
	for i in range(10):
		map = grow(map)
	print score()
	
	# Part 2 Solution
	map = []	
	with open("day18_input", "r") as infile:
		for line in infile.readlines():
			map.append(list(line.strip()))
			
	target_gen = 1000000000
	
	# give growth a head start to reach stable state
	for i in range(600):
		map = grow(map)
	
	seen_scores = []
	delta = 0
	while delta == 0:
		map = grow(map)
		res = score2()
		if res in seen_scores: # locate  loop
			delta += 1
			map = grow(map)
			while res != score2(): # find loop size
				map = grow(map)
				delta += 1
			break
		seen_scores.append(res)
	
	target_gen = (target_gen - 600 + 1) % delta
	for i in range(target_gen+1):
		map = grow(map)
	print score()

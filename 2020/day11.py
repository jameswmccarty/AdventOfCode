#!/usr/bin/python

floor = set()
occupied = set()
rows = None
cols = None
seen = set()

# does seat become occupied next round?
def check_seat(x,y):
	if (x,y) in floor:
		return False
	adjacent = 0
	for i in range(-1,2,1):
		for j in range(-1,2,1):
			if not (i == 0 and j == 0) and (x+i,y+j) in occupied:
				adjacent += 1
	if (x,y) not in occupied and adjacent == 0:
		return True
	if (x,y) in occupied and adjacent >= 4:
		return False
	if (x,y) in occupied:
		return True
	return False

def next_gen():
	global occupied
	next_occupied = set()
	for j in range(rows):
		for i in range(cols):
			if check_seat(i,j):
				next_occupied.add((i,j))
	occupied = next_occupied

def check_seat2(x,y):
	if (x,y) in floor:
		return False
	adjacent = 0
	for dx,dy in [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]:
		px = x + dx
		py = y + dy
		while px >= 0 and px <= cols and py >= 0 and py <= rows:
			if (px,py) in occupied:
				adjacent += 1
				break
			elif (px,py) not in floor:
				break
			px = px + dx
			py = py + dy
	if (x,y) not in occupied and adjacent == 0:
		return True
	if (x,y) in occupied and adjacent >= 5:
		return False
	if (x,y) in occupied:
		return True
	return False

def next_gen2():
	global occupied
	next_occupied = set()
	for j in range(rows):
		for i in range(cols):
			if check_seat2(i,j):
				next_occupied.add((i,j))
	occupied = next_occupied

def print_grid():
	for j in range(rows):
		line = ''
		for i in range(cols):
			if (i,j) in floor:
				line += '.'
			elif (i,j) in occupied:
				line += '#'
			else:
				line += 'L'
		print(line)

if __name__ == "__main__":

	# Part 1 Solution
	y = 0
	with open("day11_input", 'r') as infile:
		for line in infile.readlines():
			for x,char in enumerate(line.strip()):
				if char == ".":
					floor.add((x,y))
				elif char == "L" or char == "#":
					occupied.add((x,y))
			y += 1
	rows = y
	cols = len(line.strip())
	
	while True:
		#print_grid()
		#print()
		state = hash(frozenset(occupied))
		if state in seen:
			print(len(occupied))
			break
		seen.add(hash(frozenset(occupied)))
		next_gen()


	# Part 2 Solution
	floor = set()
	occupied = set()
	rows = None
	cols = None
	seen = set()
	y = 0
	with open("day11_input", 'r') as infile:
		for line in infile.readlines():
			for x,char in enumerate(line.strip()):
				if char == ".":
					floor.add((x,y))
				elif char == "L" or char == "#":
					occupied.add((x,y))
			y += 1
	rows = y
	cols = len(line.strip())
	
	while True:
		#print_grid()
		#print()
		state = hash(frozenset(occupied))
		if state in seen:
			print(len(occupied))
			break
		seen.add(hash(frozenset(occupied)))
		next_gen2()

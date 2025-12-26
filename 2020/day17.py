#!/usr/bin/python

alive = set()

def alive_neighbors1(x,y,z):
	global alive
	count = 0
	for i in [-1,0,1]:
		for j in [-1,0,1]:
			for k in [-1,0,1]:
				if not (i==0 and j==0 and k==0):
					if (x+i,y+j,z+k) in alive:
						count += 1
	return count

def next_gen1():

	global alive

	next_alive = set()
	x_min = min(x[0] for x in list(alive)) - 2
	x_max = max(x[0] for x in list(alive)) + 2
	y_min = min(x[1] for x in list(alive)) - 2
	y_max = max(x[1] for x in list(alive)) + 2
	z_min = min(x[2] for x in list(alive)) - 2
	z_max = max(x[2] for x in list(alive)) + 2

	for x in range(x_min, x_max):
		for y in range(y_min, y_max):
			for z in range(z_min, z_max):
				count = alive_neighbors1(x, y, z)
				if (x,y,z) in alive and (count == 2 or count == 3):
					next_alive.add((x,y,z))
				elif count == 3:
					next_alive.add((x,y,z))
	
	alive = next_alive

def alive_neighbors2(x,y,z,w):
	global alive
	count = 0
	for i in [-1,0,1]:
		for j in [-1,0,1]:
			for k in [-1,0,1]:
				for l in [-1,0,1]:
					if not (i==0 and j==0 and k==0 and l==0):
						if (x+i,y+j,z+k,w+l) in alive:
							count += 1
	return count

def next_gen2():

	global alive

	next_alive = set()
	x_min = min(x[0] for x in list(alive)) - 2
	x_max = max(x[0] for x in list(alive)) + 2
	y_min = min(x[1] for x in list(alive)) - 2
	y_max = max(x[1] for x in list(alive)) + 2
	z_min = min(x[2] for x in list(alive)) - 2
	z_max = max(x[2] for x in list(alive)) + 2
	w_min = min(x[3] for x in list(alive)) - 2
	w_max = max(x[3] for x in list(alive)) + 2

	for x in range(x_min, x_max):
		for y in range(y_min, y_max):
			for z in range(z_min, z_max):
				for w in range(w_min, w_max):
					count = alive_neighbors2(x, y, z, w)
					if (x,y,z,w) in alive and (count == 2 or count == 3):
						next_alive.add((x,y,z,w))
					elif count == 3:
						next_alive.add((x,y,z,w))
	
	alive = next_alive



if __name__ == "__main__":


	# Part 1 Solution
	with open("day17_input", 'r') as infile:
		row = 0
		for line in infile.readlines():
			for col, char in enumerate(line.strip()):
				if char == "#":
					alive.add((row, col, 0))
			row += 1

	for i in range(6):
		next_gen1()
	print(len(alive))

	# Part 2 Solution
	alive = set()
	with open("day17_input", 'r') as infile:
		row = 0
		for line in infile.readlines():
			for col, char in enumerate(line.strip()):
				if char == "#":
					alive.add((row, col, 0, 0))
			row += 1

	for i in range(6):
		next_gen2()
	print(len(alive))

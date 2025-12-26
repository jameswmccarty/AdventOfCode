#!/usr/bin/python

min_x = None
max_x = None
min_y = None
max_y = None
min_z = None
max_z = None

def unmatched(cubes):
	deltas = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
	total_unmatched = 0
	for cube in cubes:
		x,y,z = cube
		adjacent = 0
		for dx,dy,dz in deltas:
			if (x+dx,y+dy,z+dz) in cubes:
				adjacent += 1
		total_unmatched += (6-adjacent)
	return total_unmatched

def unmatched2(check_set,cubes):
	deltas = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
	total_unmatched = 0
	for cube in check_set:
		x,y,z = cube
		adjacent = 0
		for dx,dy,dz in deltas:
			if (x+dx,y+dy,z+dz) in cubes:
				adjacent += 1
		if adjacent != 0:
			total_unmatched += adjacent
	return total_unmatched

known_bubble = set()

# Determine if a location is part of an interior bubble
# keep track of all coordinates determined to be part of
# a bubble
def loc_is_part_of_a_bubble(loc):
	global min_x,max_x,min_y,max_y,min_z,max_z,known_bubble
	if loc in cubes:
		return False
	seen = set()
	deltas = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
	q = [loc]
	while len(q) > 0:
		x,y,z = q.pop(0)
		if x < min_x or x > max_x or y < min_y or y > max_y or z < min_z or z > max_z:
			return False
		for dx,dy,dz in deltas:
			if (x+dx,y+dy,z+dz) not in cubes and (x+dx,y+dy,z+dz) not in seen:
				seen.add((x+dx,y+dy,z+dz))
				q.append((x+dx,y+dy,z+dz))
	for entry in seen:
		known_bubble.add(entry)
	known_bubble.add(loc)
	return True

if __name__ == "__main__":

	cubes = set()

	# Part 1 Solution
	with open('day18_input','r') as infile:
		for line in infile.readlines():
			x,y,z = map(int,line.split(','))
			cubes.add((x,y,z))
	surf_area = unmatched(cubes)
	print(surf_area)

	# Part 2 Solution
	min_x = min(x[0] for x in cubes)
	max_x = max(x[0] for x in cubes)
	min_y = min(y[1] for y in cubes)
	max_y = max(y[1] for y in cubes)
	min_z = min(z[2] for z in cubes)
	max_z = max(z[2] for z in cubes)

	for x in range(min_x,max_x):
		for y in range(min_y,max_y):
			for z in range(min_z,max_z):
				if (x,y,z) not in known_bubble:
					loc_is_part_of_a_bubble((x,y,z))
	print(surf_area - unmatched2(known_bubble,cubes))

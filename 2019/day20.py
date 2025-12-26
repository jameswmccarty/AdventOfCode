#!/usr/bin/python

import heapq

world = dict()
portals = dict()
outers = dict()

def parse_line(idx, line):
	global world
	line = line.rstrip()
	for col, char in enumerate(line):
		world[(idx,col)] = char

def find_portals():
	global world
	global portals
	for pos in list(world.keys()):
		x,y = pos
		if 'A' <= world[pos] <= 'Z':
			U = world[(x,y-1)] if (x,y-1) in world else None
			D = world[(x,y+1)] if (x,y+1) in world else None
			L = world[(x-1,y)] if (x-1,y) in world else None
			R = world[(x+1,y)] if (x+1,y) in world else None
			if '.' in [U,D,L,R]:
				# find portal ID
				name = None
				if U != None and 'A' <= U <= 'Z':
					name = U + world[pos]
				elif D != None and 'A' <= D <= 'Z':
					name = world[pos] + D
				elif L != None and 'A' <= L <= 'Z':
					name = L + world[pos]
				elif R != None and 'A' <= R <= 'Z':
					name = world[pos] + R
				# fine portal coordinates
				coord = None
				if U != None and U == '.':
					coord = (x,y-1)
				elif D != None and D == '.':
					coord = (x,y+1)
				elif L != None and L == '.':
					coord = (x-1,y)
				elif R != None and R == '.':
					coord = (x+1,y)
				portals[coord] = name	

def warp_point(pos):
	if pos not in portals:
		return None
	name = portals[pos]
	for exit in portals.keys():
		if portals[exit] == name and exit != pos:
			return exit
	return None	

def path_search(start, finish):
	global world
	# (steps, (x,y))
	loc    = start
	steps  = 0 # Time spent searching
	h = []
	heapq.heappush(h, (steps, loc) )
	min_search = float('inf')
	seen = set()
	seen.add(loc)
	while len(h) > 0 and h[0][0] <= min_search:
		steps, loc = heapq.heappop(h)
		x, y = loc
		if loc == finish:
			min_search = min(min_search, steps)			
		else: # still possible shorter path
			next_locs = []
			if (x-1,y) in world:
				next_locs.append(((x-1, y), 1))
			if (x,y-1) in world:
				next_locs.append(((x, y-1), 1))
			if (x+1,y) in world:
				next_locs.append(((x+1, y), 1))
			if (x,y+1) in world:
				next_locs.append(((x, y+1), 1))
			if warp_point(loc) != None:
				next_locs.append((warp_point(loc),1))
			for next_loc in next_locs:
					coord, delta = next_loc
					path = world[coord]
					if path == '.' and next_loc not in seen:
						seen.add(next_loc)
						heapq.heappush(h, (steps + delta, coord))
	return min_search

def warp_point_rec(pos, depth):
	if pos not in portals:
		return None
	name = portals[pos]
	if (name == 'ZZ' or name == 'AA') and depth > 0:
		return None
	if depth == 0 and pos in outers:
		return None
	for exit in portals.keys():
		if portals[exit] == name and exit != pos:
			return exit
	return None

# return True if portal is an 'outside' portal
def is_outer(pos):
	loc = pos
	h = []
	heapq.heappush(h, loc)
	seen = set()
	seen.add(loc)
	while len(h) > 0:
		loc = heapq.heappop(h)
		x, y = loc
		next_locs = []
		next_locs.append((x-1, y))
		next_locs.append((x, y-1))
		next_locs.append((x+1, y))
		next_locs.append((x, y+1))
		for next_loc in next_locs:
			if next_loc not in world: # Fell off the map
				return True
			else:
				path = world[next_loc]
				if (path == ' ' or ('A' <= path <= 'Z')) and next_loc not in seen:
					seen.add(next_loc)
					heapq.heappush(h, next_loc)
	return False

def path_search_rec(start, finish):
	global world
	# (steps, (x,y), level)
	loc    = start
	level  = 0
	steps  = 0 # Time spent searching
	h = []
	heapq.heappush(h, (steps, loc, level) )
	min_search = float('inf')
	seen = set()
	seen.add((loc, level))
	while len(h) > 0 and h[0][0] <= min_search:
		steps, loc, level = heapq.heappop(h)
		x, y = loc
		if loc == finish and level == 0:
			min_search = min(min_search, steps)			
		else: # still possible shorter path
			next_locs = []
			if (x-1,y) in world:
				next_locs.append((x-1, y))
			if (x,y-1) in world:
				next_locs.append((x, y-1))
			if (x+1,y) in world:
				next_locs.append((x+1, y))
			if (x,y+1) in world:
				next_locs.append((x, y+1))
			for next_loc in next_locs:
					path = world[next_loc]		
					if path == '.' and (next_loc, level) not in seen:
						seen.add((next_loc, level))
						heapq.heappush(h, (steps + 1, next_loc, level))
			next_loc = warp_point_rec(loc, level)
			if next_loc != None:
				if loc in outers:
					level -= 1
				else:
					level += 1
				path = world[next_loc]
				if path == '.' and (next_loc, level) not in seen:
					seen.add((next_loc, level))
					heapq.heappush(h, (steps + 1, next_loc, level))

	return min_search

if __name__ == "__main__":

	# Part 1 Solution
	with open('day20_input', 'r') as infile:
		idx = 0
		for line in infile.readlines():
			parse_line(idx,line)
			idx += 1
	find_portals()
	start = None
	finish = None
	for k, v in portals.items():
		if v == 'AA':
			start = k
		elif v == 'ZZ':
			finish = k
	print(path_search(start, finish))

	# Part 2 Solution
	for k, v in portals.items():
		if is_outer(k):
			outers[k] = v
	print(path_search_rec(start, finish))

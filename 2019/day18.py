#!/usr/bin/python

import heapq


world = dict()
key_locs = dict()
start = None
starts = []

def parse_line(idx, line):
	global start
	for col, char in enumerate(line):
		pos = (idx,col)
		world[pos] = char
		if char >= 'a' and char <= 'z':
			key_locs[char] = pos
		elif char == '@':
			start = pos
			world[pos] = '.'

def parse_line2(idx, line):
	global starts
	for col, char in enumerate(line):
		pos = (idx,col)
		world[pos] = char
		if char >= 'a' and char <= 'z':
			key_locs[char] = pos
		elif char == '@':
			starts.append(pos)
			world[pos] = '.'

def key_search(start):
	# ( steps, (x,y), 'keys' )
	loc    = start
	steps  = 0 # Time spent searching
	keys = ''
	h = []
	heapq.heappush(h, (steps, loc, keys) )
	min_search = float('inf')
	max_x = 0
	max_y = 0
	seen = set()
	seen.add((loc, keys))
	for key in world.keys():
		x, y = key
		max_x = max(x, max_x)
		max_y = max(y, max_y)
	while len(h) > 0 and h[0][0] <= min_search and len(keys) < len(key_locs):
		steps, loc, keys = heapq.heappop(h)
		x, y = loc
		if world[loc] in key_locs.keys() and world[loc] not in keys:
			keys += world[loc]
			keys = ''.join(sorted(keys))
		if len(keys) == len(key_locs):
			min_search = min(min_search, steps)			
		else: # still possible shorter path
			next_locs = []
			if x > 0:
				next_locs.append((x-1, y))
			if y > 0:
				next_locs.append((x, y-1))
			if x < max_x:
				next_locs.append((x+1, y))
			if y < max_y:
				next_locs.append((x, y+1))
			for next_loc in next_locs:
					t = world[next_loc]
					if (t == '.' or (t.lower() in keys) or (t >= 'a' and t <= 'z')) and ((next_loc, keys) not in seen):
						seen.add((next_loc, keys))
						heapq.heappush(h, ( steps + 1, next_loc, keys ) )
	return min_search

def key_search2(starts):
	"""
	Gives incorrect solution for Test problem #3, but solves puzzle input.
	"""
	#            bot   bot   bot   bot
	# ( steps, ((x,y),(x,y),(x,y),(x,y)), 'keys' )
	locs   = starts
	steps  = 0
	keys = ''
	h = []
	heapq.heappush(h, ( steps, locs, keys) )
	min_search = float('inf')
	max_x = 0
	max_y = 0
	seen = [ set(), set(), set(), set() ]
	for z, loc in enumerate(locs):
		seen[z].add(hash((loc, keys)))
	for key in world.keys():
		x, y = key
		max_x = max(x, max_x)
		max_y = max(y, max_y)
	while len(h) > 0 and h[0][0] <= min_search:
		steps, locs, keys = heapq.heappop(h)
		#print(steps, locs, keys)
		locs = list(locs)
		for z, loc in enumerate(locs):
			l_keys = keys
			x, y = loc
			if world[loc] in key_locs.keys() and world[loc] not in l_keys:
				l_keys = ''.join(sorted(l_keys+world[loc]))
			if len(l_keys) == len(key_locs):
				min_search = min(min_search, steps)
			else:			
				next_locs = []
				if x > 0:
					next_locs.append(((x-1, y),1))
				if y > 0:
					next_locs.append(((x, y-1),1))
				if x < max_x:
					next_locs.append(((x+1, y),1))
				if y < max_y:
					next_locs.append(((x, y+1),1))
				next_locs.append((loc,0))
				for next_loc in next_locs:
					next_loc, d = next_loc
					t = world[next_loc]
					g_locs = locs
					g_locs[z] = next_loc
					g_locs = tuple(g_locs)
					state = hash((next_loc, l_keys))
					if (state not in seen[z]) and (t == '.' or (t.lower() in l_keys) or ('a' <= t <= 'z')):
						seen[z].add(state)
						heapq.heappush(h, ( steps + d, g_locs, l_keys ) )
	return min_search

if __name__ == "__main__":

	# Part 1 Solution
	with open('day18_input', 'r') as infile:
		idx = 0
		for line in infile.readlines():
			parse_line(idx, line.strip())
			idx += 1
	"""
	max_x = 0
	max_y = 0
	for key in world.keys():
		x, y = key
		max_x = max(x, max_x)
		max_y = max(y, max_y)
	for x in range(max_x):
		line = ''
		for y in range(max_y):
			line += world[(x,y)]
		print(line)
	"""
	#print(key_search(start))

	# Part 2 Solution
	world = dict()
	key_locs = dict()
	start = None
	starts = []
	with open('day18_input2', 'r') as infile:
		idx = 0
		for line in infile.readlines():
			parse_line2(idx, line.strip())
			idx += 1
	print(key_search2(tuple(starts)))

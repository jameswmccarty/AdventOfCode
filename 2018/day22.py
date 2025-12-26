#!/usr/bin/python

import heapq


target = None
cavemap = dict()
locmin  = dict()
depth = None

# (Torch, Climbing Gear)
# (True or False tuple in binary)
region_valid = { 0 : {2, 1}, # Rocky
				 1 : {0, 1}, # Wet
				 2 : {2, 0}} # Narrow

def geo_idx(x, y):
	if x == 0  and y == 0:
		return 0
	elif target != None and x == target[0] and y == target[1]:
		return 0
	elif x == 0:
		return y * 48271
	elif y == 0:
		return x * 16807
	else:
		if (x-1,y) not in cavemap:
			cavemap[(x-1, y)] = erosion_lvl(x-1,y)
		if (x, y-1) not in cavemap:
			cavemap[(x, y-1)] = erosion_lvl(x, y-1)
		return cavemap[(x-1,y)] * cavemap[(x,y-1)]

def erosion_lvl(x, y):
	return (geo_idx(x,y) + depth) % 20183

def region(x, y):
	if (x,y) not in cavemap:
		cavemap[(x,y)] = erosion_lvl(x,y)
	return cavemap[(x,y)] % 3

def loc_score(x, y, t):
	if (x,y,t) not in locmin:
		locmin[(x,y,t)] = float('inf')
	return locmin[(x,y,t)]

def cave_heap_bfs():
	#          (Torch, Climbing Gear)
	tools = 2 #(True, False)
	loc   = (0,0)
	mins  = 0 # Time spent searching
	locmin[(0,0,2)] = 0
	seen = set()
	seen.add((mins, loc, tools))
	h = []
	heapq.heappush(h, (0, (0,0), 2))
	min_search = float('inf')
	while len(h) > 0 and h[0][0] <= min_search:
		mins, loc, tools = heapq.heappop(h)
		#print mins, loc, tools
		x, y = loc
		locmin[(x,y,tools)] = min(mins, loc_score(x,y,tools))
		if loc == target:
			if tools != 2: # need to switch gear
				mins += 7
			min_search = min(mins, min_search)
			locmin[(x,y,2)] = min_search
			seen.add((mins, loc, tools))
			return min_search
		else: # still possible shorter path
			current_valid = region_valid[region(x,y)]
			for valid in current_valid:
				if valid != tools:
					heapq.heappush(h, (mins+7, loc, valid))
					seen.add((mins+7, loc, valid))
			next_locs = []
			if x > 0:
				next_locs.append((x-1, y))
			if y > 0:
				next_locs.append((x, y-1))
			if x < 70: # problem specific bound, selected to be reasonable limit
				next_locs.append((x+1, y))
			next_locs.append((x, y+1))
			for next_loc in next_locs:
				next_set = current_valid.intersection(region_valid[region(next_loc[0], next_loc[1])])
				for toolset in next_set:
						if tools == toolset and mins+1 <= loc_score(next_loc[0], next_loc[1], tools):
							if (mins+1, next_loc, toolset) not in seen:
								heapq.heappush(h, (mins+1, next_loc, toolset))
								seen.add((mins+1, next_loc, toolset))
	return min_search


if __name__ == "__main__":

	# Part 1 Solution
	
	depth = 4002
	target = (5, 746)
		
	#depth = 510
	#target = (10,10)

	risk = 0
	
	for i in range(target[0]+1):
		for j in range(target[1]+1):
			cavemap[(i,j)] = erosion_lvl(i,j)
			risk += cavemap[(i,j)] % 3
	print risk
	
	# Part 2 Solution
	print cave_heap_bfs()

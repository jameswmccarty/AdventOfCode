#!/usr/bin/python

# Advent of Code 2024 Day 16

import heapq

def bfs(start, end, walls):
	seen = set()
	q = []
	heapq.heapify(q)
	dirs = [(1,0),(0,-1),(-1,0),(0,1)]
	seen.add((start,0))
	heapq.heappush(q, (0,start,0))
	while q:
		score, pos, facing = heapq.heappop(q)
		if pos == end: return score
		x, y = pos
		dx, dy = dirs[facing]
		nx, ny = x+dx, y+dy
		if (nx, ny) not in walls and ((nx, ny), facing) not in seen:
			seen.add(((nx,ny),facing))
			heapq.heappush(q,(score+1,(nx,ny),facing))
		if (pos, (facing+1)%4) not in seen:
			seen.add((pos, (facing+1)%4))
			heapq.heappush(q,(score+1000,pos,(facing+1)%4))
		if (pos, (facing-1)%4) not in seen:
			seen.add((pos, (facing-1)%4))
			heapq.heappush(q,(score+1000,pos,(facing-1)%4))
	return "None"

def bfs_tiles(start, end, walls, cap):
	pt_costs = dict()
	q = []
	heapq.heapify(q)
	dirs = [(1,0),(0,-1),(-1,0),(0,1)]
	heapq.heappush(q, (0,start,0, {start}))
	found_routes = set()
	while q:
		score, pos, facing, route = heapq.heappop(q)
		if pos == end:
			if score <= cap:
				for pt in route:
					found_routes.add(pt)
		if score > cap:
			return found_routes
		if pos not in pt_costs:
			pt_costs[pos] = score + 1000
		if score <= pt_costs[pos]:
			x, y = pos
			dx, dy = dirs[facing]
			nx, ny = x+dx, y+dy
			if (nx, ny) not in walls and (nx, ny) not in route:
				heapq.heappush(q,(score+1,(nx,ny),facing, {*route, (nx,ny)}))
		if score+1000 <= pt_costs[pos]:
			heapq.heappush(q,(score+1000,pos,(facing+1)%4, route))
			heapq.heappush(q,(score+1000,pos,(facing-1)%4, route))
	return "None"

if __name__ == "__main__":

	# Part 1 Solution
	walls = set()
	start = None
	end = None
	with open("day16_input", "r") as infile:
		y = 0
		for line in infile.readlines():
			for x, char in enumerate(line.strip()):
				if char == '#': walls.add((x,y))
				elif char == 'S': start = (x,y)
				elif char == 'E': end = (x,y)
			y = y + 1
	cost = bfs(start, end, walls)
	print(cost)

	# Part 2 Solution
	print(len(bfs_tiles(start, end, walls, cost)))
		

#!/usr/bin/python

from itertools import permutations
from collections import deque


world = []

def bfs(start, dest):
	search_queue = deque()
	search_queue.append((start, 0))
	seen = set()
	seen.add(start)
	while len(search_queue) > 0:
		posit, steps = search_queue.popleft()
		x, y = posit
		if posit == dest:
			return steps
			
		if x > 0 and (x-1, y) not in seen and world[y][x-1] != '#':
			search_queue.append(((x-1,y), steps + 1))
			seen.add((x-1,y))
		if y > 0 and (x,y-1) not in seen and world[y-1][x] != '#':
			search_queue.append(((x,y-1), steps + 1))
			seen.add((x, y-1))
		if y < len(world)-1 and (x, y+1) not in seen and world[y+1][x] != '#':
			search_queue.append(((x,y+1), steps + 1))
			seen.add((x, y+1))
		if x < len(world[0])-1 and (x+1,y) not in seen and world[y][x+1] != '#':
			search_queue.append(((x+1,y), steps + 1))
			seen.add((x, y+1))
	
	return float('inf') # no solution

if __name__ == "__main__":

	# Part 1 Solution
	
	coords = dict()
	stops = []
	adj_matrix = []
	
	short_trip = float('inf')
	
	with open("day24_input", "r") as infile:
		row_num = 0
		for line in infile.readlines():
			world.append(line.strip())
			for col_num, char in enumerate(line.strip()):
				if char >= '0' and char <= '9':
					coords[char] = (col_num, row_num)
			row_num += 1
	
	stops = coords.keys()
	stops = [ int(x) for x in stops ]
	stops.sort()
	for i in range(len(stops)):
		adj_matrix.append([0]*len(stops))
		
	for i in range(len(stops)):
		for j in range(i, len(stops)):
			adj_matrix[j][i] = bfs(coords[str(i)], coords[str(j)])
			adj_matrix[i][j] = adj_matrix[j][i]

	stops.remove(0) # always start from 0	
	for trip in permutations(stops):
		length = 0
		last = 0
		while len(trip) > 0:
			length += adj_matrix[last][trip[0]]
			last = trip[0]
			trip = trip[1:]
		short_trip = min(short_trip, length)
		
	print short_trip
	
	# Part 2 Solution
	
	short_trip = float('inf')
	
	for trip in permutations(stops):
		length = 0
		last = 0
		trip = list(trip) + [0]
		while len(trip) > 0:
			length += adj_matrix[last][trip[0]]
			last = trip[0]
			trip = trip[1:]
		short_trip = min(short_trip, length)
		
	print short_trip
	
		
			
			

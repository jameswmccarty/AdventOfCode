#!/usr/bin/python

from collections import deque


def bfs_to_G(map):
	goal = None
	open = None
	seen = set()
	for y, row in enumerate(map):
		for x, char in enumerate(row):
			if char == 'G':
				goal = (x,y)
			elif char == '_':
				open = (x,y)
	if goal == None or open == None:
		return float('inf')
	search_queue = deque()
	search_queue.append((open, 0))
	seen.add(open)
	while len(search_queue) > 0:
		current, steps = search_queue.popleft()
		x, y = current
		if current == goal:
			return steps
		if x > 0 and (x-1, y) not in seen and map[y][x-1] != '#':
			search_queue.append(((x-1, y), steps+1))
			seen.add((x-1, y))
		if x < len(map[0])-1 and (x+1, y) not in seen and map[y][x+1] != '#':
			search_queue.append(((x+1, y), steps+1))
			seen.add((x+1,y))
		if y < len(map)-1 and (x, y+1) not in seen and map[y+1][x] != '#':
			search_queue.append(((x, y+1), steps+1))
			seen.add((x, y+1))
		if y > 0 and (x, y-1) not in seen and map[y-1][x] != '#':
			search_queue.append(((x, y-1), steps+1))
			seen.add((x, y-1))
	return float('inf')
			
def parse_node(line):
	line = ' '.join(line.split())
	line = line.split(' ')
	path, x, y = line[0].split("-")
	return Node(int(x.replace("x",'')),
				int(y.replace("y",'')),
				int(line[1].replace("T",'')),
				int(line[2].replace("T",'')),
				int(line[3].replace("T",'')))	

class Node:

	def __init__(self, x, y, size, used, avail):
		self.x = x
		self.y = y
		self.size = size
		self.used = used
		self.avail= avail

if __name__ == "__main__":

	nodes = []
	
	viable = 0

	# Part 1 Solution
	with open("day22_input", "r") as infile:
		junk = infile.readline()
		junk = infile.readline()
		for line in infile.readlines():
			nodes.append(parse_node(line.strip()))
			
	for i, node in enumerate(nodes):
		for j in range(i, len(nodes)):
			if (node.used != 0 and node.used <= nodes[j].avail) or (nodes[j].used != 0 and nodes[j].used <= node.avail):
				viable += 1
				
	print viable
	
	# Part 2 Solution
	
	map = []
	x_dim = 0
	y_dim = 0
	for node in nodes:
		x_dim = max(x_dim, node.x)
		y_dim = max(y_dim, node.y)
	
	x_dim += 1
	y_dim += 1
	
	for j in range(y_dim):
		map.append(['#'] * x_dim)
		
	for i, node in enumerate(nodes):
		for j in range(i, len(nodes)):
			if (node.used != 0 and node.used <= nodes[j].avail) or (nodes[j].used != 0 and nodes[j].used <= node.avail):
				map[node.y][node.x] = '.'
				map[nodes[j].y][nodes[j].x] = '.'
				
	map[0][x_dim-1] = 'G'
	
	for node in nodes:
		if node.used == 0:
			map[node.y][node.x] = '_'
	
	"""
	# print map
	for row in map:
		print ''.join(row)
	"""
	
	"""
	.....................................G
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	......................................
	.........#############################
	......................................
	.................................._...
	......................................
	"""
	
	## Move the open space to the corner with the Goal
	steps = bfs_to_G(map)
	## Then move the Goal to the (0,0) mark.
	## It takes 5 actions to move the Goal one spot to the left
	## And moving the open space to the goal placed it one 
	## position to the left, out of the corner
	print steps + (len(map[0])-2) * 5

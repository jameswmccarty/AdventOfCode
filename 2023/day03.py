#!/usr/bin/python

from collections import deque
import math

digits = '0123456789'

engine_map = dict()
gear_map   = dict()

def symbol_adjacent(x,y):
	q = deque()
	pos = (x,y)
	seen = set()
	seen.add(pos)
	q.append(pos)
	while q:
		pos = q.popleft()
		if pos in engine_map and engine_map[pos] not in digits:
			return True
		x,y = pos
		for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)):
			nx,ny = x+dx,y+dy
			if (nx,ny) in engine_map and (nx,ny) not in seen:
				q.append((nx,ny))
				seen.add((nx,ny))
	return False

def gears_adjacent(x,y):
	q = deque()
	pos = (x,y)
	seen = set()
	seen.add(pos)
	q.append(pos)
	touching_pos = []
	while q:
		pos = q.popleft()
		if pos in gear_map:
			touching_pos.append(pos)
		x,y = pos
		for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)):
			nx,ny = x+dx,y+dy
			if (nx,ny) in engine_map and (nx,ny) not in seen and engine_map[(nx,ny)] in digits+'*':
				q.append((nx,ny))
				seen.add((nx,ny))
	return touching_pos

if __name__ == "__main__":

	map_x_dim = 0
	map_y_dim = 0

	# Part 1 Solution
	with open("day03_input", "r") as infile:
		y = 0
		for line in infile:
			map_x_dim = len(line)
			for idx,char in enumerate(line.strip()):
				if char != '.':
					engine_map[(idx,y)] = char
				if char == '*':
					gear_map[(idx,y)] = []
			y += 1
		map_y_dim = y

	total = 0
	for y in range(map_y_dim):
		x = 0
		while x < map_x_dim:
			if (x,y) in engine_map and engine_map[(x,y)] in digits and symbol_adjacent(x,y):
				built = ''
				while (x,y) in engine_map and engine_map[(x,y)] in digits:
					built += engine_map[(x,y)]
					x += 1
				total += int(built)
			x += 1
	print(total)

	# Part 2 Solution

	for y in range(map_y_dim):
		x = 0
		while x < map_x_dim:
			if (x,y) in engine_map and engine_map[(x,y)] in digits:
				gear_adj_list = gears_adjacent(x,y)
				if len(gear_adj_list) == 1:
					built = ''
					while (x,y) in engine_map and engine_map[(x,y)] in digits:
						built += engine_map[(x,y)]
						x += 1
					gear_map[gear_adj_list[0]].append(int(built))
			x += 1

	print(sum(math.prod(e) for e in gear_map.values() if len(e) == 2))

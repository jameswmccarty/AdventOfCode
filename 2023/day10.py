#!/usr/bin/python


diagram = dict()
from collections import deque

# LEFT is neg
# RIGHT is pos
# UP is neg
# DOWN is pos

deltas = {	'|' : ((0,1),(0,-1)),
			'-' : ((-1,0),(1,0)),
			'L' : ((1,0),(0,-1)),
			'J' : ((-1,0),(0,-1)),
			'7' : ((-1,0),(0,1)),
			'F' : ((1,0),(0,1)),
			'.' : ((0,0)),
			'S' : ((0,1),(0,-1),(1,0),(-1,0)) }

def bfs(start):
	q = deque()
	seen = set()
	seen.add(start)
	q.append((start))
	count_map = dict()
	count_map[start] = 0
	while q:
		pos = q.popleft()
		x,y = pos
		for dx,dy in deltas[diagram[pos]]:
			if (x+dx,y+dy) not in seen and (x+dx,y+dy) in diagram and diagram[(x+dx,y+dy)] != '.':
				seen.add((x+dx,y+dy))
				count_map[(x+dx,y+dy)] = count_map[pos] + 1
				q.append((x+dx,y+dy))
	return count_map

def exclude_border_points_bfs(points_forming_loop):
	max_y = max(p[1] for p in diagram.keys())+2
	max_x = max(p[0] for p in diagram.keys())+2
	q = deque()
	seen = set()
	seen.add((-1,-1))
	q.append((-1,-1))
	while q:
		pos = q.popleft()
		x,y = pos
		for dx,dy in ((0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)):
			pt = (x+dx,y+dy)
			if pt not in seen and pt not in points_forming_loop and pt[0] >= -1 and pt[0] < max_x and pt[1] >= -1 and pt[1] < max_y:
				seen.add(pt)
				q.append(pt)
	return seen

def check_pos(pos):
	x_row_pipes = { pt for pt in points_forming_loop if pt[1] == pos[1] }
	x_row_pipes.add(pos)
	x_row_str = ''.join( diagram[x] for x in sorted(x_row_pipes) )
	in_loop = False
	x_row_str = deque(x_row_str)
	while x_row_str:
		char = x_row_str.popleft()
		if char in '|7F':
			in_loop ^= True
		if char == '.' and in_loop:
			return True
	return False

if __name__ == "__main__":

	# Part 1 Solution
	with open("day10_input", "r") as infile:
		y = 0
		start = None
		for line in infile:
			for x,char in enumerate(line.strip()):
				diagram[(x,y)] = char
				if char == 'S':
					start = (x,y)
			y += 1

	max_step = -1
	best_char = None
	points_forming_loop = set()
	for char in '|-LJ7F':
		diagram[start] = char
		count_map = bfs(start)
		for k,v in count_map.items():
			if v > max_step:
				x,y = k
				if all( (x+dx,y+dy) in count_map for dx,dy in deltas[diagram[k]] ) and all( count_map[(x+dx,y+dy)] == v-1 for dx,dy in deltas[diagram[k]] ):
						max_step = v
						best_char = char
						points_forming_loop = { p for p,c in count_map.items() if c <= v }
	print(max_step)

	# Part 2 Solution

	excludes = exclude_border_points_bfs(points_forming_loop)
	candidates = set()
	for y in range(max(p[1] for p in diagram.keys())):
		for x in range(max(p[0] for p in diagram.keys())):
			if (x,y) not in points_forming_loop and (x,y) not in excludes:
				candidates.add((x,y))
				diagram[(x,y)] = '.'

	print(len({ pt for pt in candidates if check_pos(pt) }))

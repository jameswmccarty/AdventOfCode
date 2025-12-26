#!/usr/bin/python


height_map = dict() # store the map as height at (x,y)

def bfs(pos,goal):
	seen = set()
	seen.add(pos)
	steps = 0
	q = []
	q.append((steps,pos))
	while len(q) > 0:
		steps,current = q.pop(0)
		if current == goal:
			return steps
		x,y = current
		for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
			if (x+dx,y+dy) in height_map and (x+dx,y+dy) not in seen and height_map[(x+dx,y+dy)]-height_map[current] <= 1:
				seen.add((x+dx,y+dy))
				q.append((steps+1,(x+dx,y+dy)))
	return float('inf')

def bfs2(pos):
	seen = set()
	seen.add(pos)
	steps = 0
	q = []
	q.append((steps,pos))
	while len(q) > 0:
		steps,current = q.pop(0)
		if height_map[current] == 0:
			return steps
		x,y = current
		for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
			if (x+dx,y+dy) in height_map and (x+dx,y+dy) not in seen and height_map[current]-height_map[(x+dx,y+dy)] <= 1:
				seen.add((x+dx,y+dy))
				q.append((steps+1,(x+dx,y+dy)))
	return float('inf')

if __name__ == "__main__":

	# Part 1 Solution
	pos = None
	goal = None
	with open("day12_input","r") as infile:
		j = 0
		for line in infile.readlines():
			for i,char in enumerate(line.strip()):
				if char == 'S':
					pos = (i,j)
					height_map[(i,j)] = 0
				elif char == 'E':
					goal = (i,j)
					height_map[(i,j)] = ord('z') - ord('a')
				else:
					height_map[(i,j)] = ord(char)- ord('a')
			j += 1
	print(bfs(pos,goal))

	# Part 2 Solution
	"""
	best_score = float('inf')
	for pos,height in height_map.items():
		if height == 0:
			best_score = min(best_score,bfs(pos,goal))
	print(best_score)
	"""
	print(bfs2(goal))

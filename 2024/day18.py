#!/usr/bin/python

# Advent of Code 2024 Day 18

def bfs(walls):
	pos = (0,0)
	q = [(pos,0)]
	seen = set()
	seen.add(pos)
	while q:
		pos, steps = q.pop(0)
		x, y = pos
		if pos == (70,70):
			return steps
		for dx,dy in ((0,1),(1,0),(0,-1),(-1,0)):
			nx, ny = x+dx, y+dy
			if nx >= 0 and nx < 71 and ny >= 0 and ny < 71 and (nx,ny) not in walls and (nx,ny) not in seen:
				seen.add((nx,ny))
				q.append(((nx,ny),steps+1))
	return float('inf')

if __name__ == "__main__":

	# Part 1 Solution
	walls = set()
	with open("day18_input", "r") as infile:
		for i in range(1024):
			line = infile.readline().strip()
			x, y = line.split(',')
			walls.add((int(x), int(y)))

	print(bfs(walls))

	# Part 2 Solution
	walls = set()
	with open("day18_input", "r") as infile:
		for i in range(1024):
			line = infile.readline().strip()
			x, y = line.split(',')
			walls.add((int(x), int(y)))

		cost = bfs(walls)
		last = None
		while cost != float('inf'):
			line = infile.readline().strip()
			x, y = line.split(',')
			last = line.strip()
			walls.add((int(x), int(y)))
			cost = bfs(walls)
		print(line)

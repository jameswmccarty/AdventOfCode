#!/usr/bin/python

from collections import deque

def walk_dists(plots,start,max_steps):
	dists = dict()
	q = deque()
	seen = set()
	dists[start] = 0
	seen.add(start)
	q.append((start,0))
	while q:
		pos,steps = q.popleft()
		dists[pos] = steps
		if steps < max_steps:
			x,y = pos
			for dx,dy in ((0,1),(1,0),(0,-1),(-1,0)):
				p2 = (x+dx,y+dy)
				if p2 not in seen and p2 in plots:
					q.append((p2,steps+1))
					seen.add(p2)
	return dists

if __name__ == "__main__":

	plots = set()
	start = None

	# Part 1 Solution
	with open("day21_input", "r") as infile:
		y = 0
		for line in infile:
			for x,c in enumerate(line.strip()):
				if c == 'S':
					start = (x,y)
				elif c == '.':
					plots.add((x,y))
			y += 1

	dists = walk_dists(plots,start,64)
	positions = sum( 1 if (64-x)%2 == 0 else 0 for x in dists.values() )
	print(positions)




	# Part 2 Solution


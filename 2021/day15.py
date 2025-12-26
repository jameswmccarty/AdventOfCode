#!/usr/bin/python


if __name__ == "__main__":

	import heapq

	cave_map = dict()
	cave_dim = None

	def cost_at(x,y):
		risk = cave_map[x%cave_dim,y%cave_dim] + x//cave_dim + y//cave_dim
		return risk%10+1 if risk > 9 else risk

	def search(goal,scale):
		q = []
		heapq.heapify(q)
		seen = set((0,0))
		heapq.heappush(q,(0,0,0))
		while len(q) > 0:
			risk,x,y = heapq.heappop(q)
			if (x,y) == goal:
				return risk
			for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
				nx,ny = x+dx, y+dy
				if (nx,ny) not in seen and nx >= 0 and nx < cave_dim*scale and ny >= 0 and ny < cave_dim*scale:
					heapq.heappush(q,(risk+cost_at(nx,ny),nx,ny))
					seen.add((nx,ny))
		return float('inf')

	# Part 1 Solution

	with open("day15_input","r") as infile:
		cave = infile.read().strip().split('\n')
	for j,line in enumerate(cave):
		for i,val in enumerate(line):
			cave_map[(i,j)] = int(val)

	cave_dim = len(cave)

	print(search((cave_dim-1,cave_dim-1),1))

	# Part 2 Solution

	print(search((cave_dim*5-1,cave_dim*5-1),5))


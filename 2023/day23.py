#!/usr/bin/python


from collections import deque
import sys

longs = dict()
def max_bfs2(start,end,opens,forced):
	global longs
	forcing = { '>' : (1,0),
		    '<' : (-1,0),
		    'v' : (0,1),
		    '^' : (0,-1) }
	seen = set()
	seen.add(start)
	q = deque()
	most_steps = 0
	q.append((start,seen,0))
	while q:
		pos,seen,steps = q.popleft()
		if pos == end:
			most_steps = max(most_steps,steps)
		elif steps >= longs[pos]:
			longs[pos] = steps
			if pos in forced:
				x,y = pos	
				dx,dy = forcing[forced[pos]]
				if (x+dx,y+dy) not in seen and ((x+dx,y+dy) in opens or (x+dx,y+dy) in forced):
					q.append(((x+dx,y+dy),{*seen,(x+dx,y+dy)},steps+1))
			else:
				x,y = pos
				for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
					nx,ny = x+dx,y+dy
					if (nx,ny) not in seen and ((nx,ny) in opens or (nx,ny) in forced):
						q.append(((nx,ny),{*seen,(nx,ny)},steps+1))
	return most_steps

most_steps = 0
def max_dfs2(pos,graph,seen,steps):
	global most_steps
	if pos.end:
		most_steps = max(most_steps,steps)
		#print(most_steps)
	else:
		for entry in pos.connections:
			if entry not in seen:
				max_dfs2(entry,graph,{*seen,entry},steps+pos.weight)

class Node:
	
	def __init__(self):
		self.weight = 1
		self.connections = set()
		self.end = False
		self.start = False
	
	def connect(self,a):
		self.connections.add(a)
	
	def remove(self,a):
		self.connections.discard(a)
	
	def compress(self):
		if len(self.connections) == 2 and not self.end and not self.start:
			t_conn = list(self.connections)
			if len(t_conn[0].connections) == 2 and len(t_conn[1].connections) == 2:
				if not t_conn[0].end and not t_conn[1].end and not t_conn[0].start and not t_conn[1].start: 
					left  = self.connections.pop()
					right =	self.connections.pop()
					left.remove(self)
					right.remove(self)
					left.connect(right)
					right.connect(left)
					right.weight += self.weight
					return True
		return False

if __name__ == "__main__":
	sys.setrecursionlimit(6000)
	start = None
	end   = None
	forcing = dict()
	opens   = set()
	# Part 1 Solution
	with open("day23_input", "r") as infile:
		y = 0
		for line in infile:
			for x,c in enumerate(line.strip()):
				if c in 'v^<>':
					forcing[(x,y)] = c
				elif c == '.':
					opens.add((x,y))
			y += 1
	
	start = [ (x,y) for x,y in opens if y == 0 ][0]
	end =   [ (i,j) for i,j in opens if j == (y-1) ][0]
	for pt in opens:
		longs[pt] = 0
	for pt in forcing.keys():
		longs[pt] = 0
	print(max_bfs2(start,end,opens,forcing))

	# Part 2 Solution
	
	nodes = dict()
	for pt in forcing.keys():
		opens.add(pt)
	for pt in opens:
		nodes[pt] = Node()
	for pt in opens:
		x,y = pt
		for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
			nx,ny = x+dx,y+dy
			if (nx,ny) in opens:
				nodes[pt].connect(nodes[(nx,ny)])
				nodes[(nx,ny)].connect(nodes[pt])
		
	nodes[end].end = True
	nodes[start].start = True	
	new_start = nodes[start]
		
	graph = [ x for x in nodes.values() ]
	while any( x.compress() for x in graph ):
		continue;
		
	graph = [ x for x in graph if len(x.connections) > 0]
	max_dfs2(new_start,graph,{new_start},0)
	print(most_steps)



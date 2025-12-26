#!/usr/bin/python

from collections import deque

def next_blizzards(walls,blizzards,max_x,max_y):
	next_blizz = []
	for blizzard in blizzards:
		x,y,direction = blizzard
		if direction == '>':
			if x+1 == max_x:
				next_blizz.append((1,y,direction))
			else:
				next_blizz.append((x+1,y,direction))
		elif direction == '<':
			if x-1 == 0:
				next_blizz.append((max_x-1,y,direction))
			else:
				next_blizz.append((x-1,y,direction))
		elif direction == '^':
			if y-1 == 0:
				next_blizz.append((x,max_y-1,direction))
			else:
				next_blizz.append((x,y-1,direction))
		elif direction == 'v':
			if y+1 == max_y:
				next_blizz.append((x,1,direction))
			else:
				next_blizz.append((x,y+1,direction))
	return sorted(next_blizz)	

# too slow
def bfs(start,end,walls,blizzards):
	max_x = max([p[0] for p in walls])
	max_y = max([p[1] for p in walls])
	deltas = ((0,1),(1,0),(0,-1),(-1,0),(0,0))
	seen = set()
	q = deque()
	q.append((start,blizzards,0))
	while len(q) > 0:
		pos,blizzards,t = q.popleft()
		if pos == end:
			return t
		else:
			x,y = pos
			blizzards = next_blizzards(walls,blizzards,max_x,max_y)
			blocked = { (x,y) for x,y,d in blizzards }
			for dx,dy in deltas:
				step = (x+dx,y+dy)
				if step not in blocked and step not in walls:
					state = hash((step,tuple(blizzards)))
					if state not in seen:
						q.append((step,blizzards,t+1))
						seen.add(state)

def time_map_bfs(start,end,open_at_t,start_t=0):
	deltas = ((0,1),(1,0),(0,-1),(-1,0),(0,0))
	q = deque()
	q.append((start,start_t))
	seen = set()
	while len(q) > 0:
		pos,t = q.popleft()
		if pos == end:
			return t
		else:
			x,y = pos
			t += 1
			for dx,dy in deltas:
				step = (x+dx,y+dy)
				state = hash((step,t%len(open_at_t)))
				if step in open_at_t[t%len(open_at_t)] and state not in seen:
					seen.add(state)
					q.append((step,t))


def find_open_spots(walls,blizzards,max_x,max_y):
	blocked = { (x,y) for x,y,d in blizzards }
	opened = set()
	for x in range(max_x):
		for y in range(max_y+1):
			if (x,y) not in blocked and (x,y) not in walls:
				opened.add((x,y))
	return opened			

def time_map(walls,blizzards):
	open_at_t = dict()
	t = 0	
	max_x = max([p[0] for p in walls])
	max_y = max([p[1] for p in walls])
	orig_blizzards = sorted(blizzards)
	open_at_t[t] = find_open_spots(walls,blizzards,max_x,max_y)
	blizzards = next_blizzards(walls,blizzards,max_x,max_y)
	while blizzards != orig_blizzards:
		t += 1
		open_at_t[t] = find_open_spots(walls,blizzards,max_x,max_y)
		blizzards = next_blizzards(walls,blizzards,max_x,max_y)
	return open_at_t

if __name__ == "__main__":

	walls = set()
	blizzards = list()

	# Part 1 Solution
	with open('day24_input','r') as infile:
		y = 0
		for line in infile.readlines():
			for x,char in enumerate(line.strip()):
				if char == '#':
					walls.add((x,y))
				elif char in '<>^v':
					blizzards.append((x,y,char))
			y += 1

	start_x = 0
	start = None
	while True:
		if (start_x,0) not in walls:
			start = (start_x,0)
			break
		start_x += 1
	end_x = 0
	end = None
	while True:
		if (end_x,y-1) not in walls:
			end = (end_x,y-1)
			break
		end_x += 1
	open_map = time_map(walls,blizzards)
	t1 = time_map_bfs(start,end,open_map)
	print(t1)

	# Part 2 Solution
	t2 = time_map_bfs(end,start,open_map,t1)
	t3 = time_map_bfs(start,end,open_map,t2)
	print(t3)




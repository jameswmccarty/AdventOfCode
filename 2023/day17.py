#!/usr/bin/python


import heapq

deltas = {	(1,0) : ((1,0),(0,1),(0,-1)),
			(-1,0): ((-1,0),(0,1),(0,-1)),
			(0,-1): ((0,-1),(1,0),(-1,0)),
			(0,1) : ((0,1),(1,0),(-1,0)) }

def search(dest,layout):
	pos = (0,0) # begin upper left
	q = []
	seen = set()
	heapq.heapify(q)
	# heat lost, pos, direction, steps_before_turn
	heapq.heappush(q,(0,pos,(1,0),1))
	heapq.heappush(q,(0,pos,(0,-1),1))
	while q:
		loss,pos,direction,steps = heapq.heappop(q)
		if pos == dest:
			return loss
		if hash((pos,direction,steps)) not in seen:
			seen.add(hash((pos,direction,steps)))
			next_dirs = set(deltas[direction])
			if steps == 3:
				next_dirs.discard(direction)
			x,y = pos
			for dx,dy in next_dirs:
				nx,ny = x+dx,y+dy
				if (nx,ny) in layout:
					if (dx,dy) != direction:
						heapq.heappush(q,(loss+layout[(nx,ny)],(nx,ny),(dx,dy),1))
					else:
						heapq.heappush(q,(loss+layout[(nx,ny)],(nx,ny),(dx,dy),steps+1))
	return float('inf')

def search2(dest,layout):
	pos = (0,0) # begin upper left
	q = []
	seen = set()
	heapq.heapify(q)
	# heat lost, pos, direction, steps_before_turn, steps_taken
	heapq.heappush(q,(0,pos,(1,0),3,0))
	heapq.heappush(q,(0,pos,(0,-1),3,0))
	while q:
		loss,pos,direction,steps_before_turn,steps_taken = heapq.heappop(q)
		if pos == dest and steps_before_turn == 0 and steps_taken <= 10:
			return loss
		if hash((pos,direction,steps_before_turn,steps_taken)) not in seen:
			seen.add(hash((pos,direction,steps_before_turn,steps_taken)))
			next_dirs = set(deltas[direction])
			if steps_before_turn > 0:
				next_dirs = { direction }
			if steps_taken == 10:
				next_dirs.discard(direction)
			x,y = pos
			for dx,dy in next_dirs:
				nx,ny = x+dx,y+dy
				if (nx,ny) in layout:
					if (dx,dy) != direction:
						heapq.heappush(q,(loss+layout[(nx,ny)],(nx,ny),(dx,dy),3,1))
					else:
						heapq.heappush(q,(loss+layout[(nx,ny)],(nx,ny),(dx,dy),max(0,steps_before_turn-1),steps_taken+1))
	return float('inf')

if __name__ == "__main__":

	# Part 1 Solution
	layout = dict()
	with open("day17_input", "r") as infile:
		y = 0
		for line in infile:
			x_dim = len(line.strip())
			for x,c in enumerate(line.strip()):
				layout[(x,y)] = int(c)
			y += 1

	print(search((x_dim-1,y-1),layout))

	# Part 2 Solution
	print(search2((x_dim-1,y-1),layout))


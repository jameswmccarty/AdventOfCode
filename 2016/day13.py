#!/usr/bin/python

from collections import deque


favorite = 0

# Return True if open or False if wall
def pop_square(x, y):
	global favorite
	value = x*x + 3*x + 2*x*y + y + y*y + favorite
	popcount = 0
	while value > 0:
		if value & 0x01 == 0x01:
			popcount += 1
		value = value >> 1
	if popcount % 2 == 0:
		return True
	return False
	
# Perform a breadth first search.  Return number of steps to destination
# We begin at location (1,1)
def bfs(dest_x, dest_y):
	search_queue = deque()
	seen = set()
	search_queue.append(((1,1),0))
	while len(search_queue) > 0:
		posit, steps = search_queue.popleft()
		x, y = posit
		if x == dest_x and y == dest_y:
			return steps
		seen.add(posit)

		if x > 0 and (x-1,y) not in seen and pop_square(x-1,y):
			search_queue.append(((x-1,y), steps+1))
		if y > 0 and (x,y-1) not in seen and pop_square(x,y-1):
			search_queue.append(((x,y-1), steps+1))
		if (x,y+1) not in seen and pop_square(x,y+1):
			search_queue.append(((x,y+1),steps+1))
		if (x+1,y) not in seen and pop_square(x+1,y):
			search_queue.append(((x+1,y),steps+1))
	
	return float('inf') # no solution

# Perform a breadth first search.  Return number of reachable locations within a given max number of steps.
def area_count(max_steps):
	search_queue = deque()
	seen = set()
	search_queue.append(((1,1),0))
	while len(search_queue) > 0:
		posit, steps = search_queue.popleft()
		x, y = posit
		seen.add(posit)

		if x > 0 and (x-1,y) not in seen and pop_square(x-1,y) and steps < max_steps:
			search_queue.append(((x-1,y), steps+1))
		if y > 0 and (x,y-1) not in seen and pop_square(x,y-1) and steps < max_steps:
			search_queue.append(((x,y-1), steps+1))
		if (x,y+1) not in seen and pop_square(x,y+1) and steps < max_steps:
			search_queue.append(((x,y+1),steps+1))
		if (x+1,y) not in seen and pop_square(x+1,y) and steps < max_steps:
			search_queue.append(((x+1,y),steps+1))
	
	return len(seen)
	
if __name__ == "__main__":

	# Part 1 Solution
	
	# favorite = 10
	# print bfs(7,4)
	
	favorite = 1358
	print bfs(31,39)
	
	# Part 2 Solution
	print area_count(50)

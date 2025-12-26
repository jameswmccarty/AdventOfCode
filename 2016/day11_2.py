#!/usr/bin/python

import itertools
from collections import deque
import time


# Return True if all components are on the 4th floor
def all_top(items):
	for item in items:
		if item != 3:
			return False
	return True

def valid_combos(items):
	valid = []
	for i in range(len(items)):
		for j in range(i, len(items)):
			if items[i] & 0x01 == 0x01:
				if items[j] == items[i]+1:
					valid.append((items[i],items[j]))
				elif items[j] & 0x01 == 0x01:
					valid.append((items[i],items[j]))
			elif items[j] & 0x01 == 0:
				valid.append((items[i], items[j]))
	return valid

# Return True if a microchip is on the same floor with
# a generator it is not paired with.
# Paired Generators and Microchips are at adjacent indexes, with
# Generators in Odd numbered indexes	
def fried_list(items):
	for i in range(1, len(items), 2):
		if items[i] != items[i+1]: # not on same floor	
			for j in range(1, len(items), 2): # another gen on floor
				if items[j] == items[i+1]:
					return True
	return False
	
def bfs_list_solve(start):
	seen = set()
	search_queue = deque()
	seen.add(hash(tuple(start)))
	start.append(0)
	search_queue.append(start)
	while len(search_queue) > 0:
		items = search_queue.popleft()
		steps = items.pop()
		elev_floor = items[0]
		if all_top(items):
			return steps
			
		"""
		#
		# Below section only runs if we have not found a solution yet.
		#
		"""
		
		# We can move anything on the floor with the elevator
		moveable_idx = [ i for i in range(1,len(items)) if items[i] == elev_floor ]
		# We must move either 1 or 2 items
		base_poss =  moveable_idx
		#base_poss += valid_combos(moveable_idx)
		base_poss += [ x for x in itertools.combinations(moveable_idx, 2) ]
		if elev_floor < 3: # not on top floor
			for move in base_poss:
				next_items = items[:]
				if type(move) == tuple:
					for step in move:
						next_items[step] = elev_floor + 1
				else:
					next_items[move] = elev_floor + 1
				next_items[0] = elev_floor + 1
				thash = hash(tuple(next_items))
				if thash not in seen and not fried_list(next_items):
					seen.add(thash) # prevent back-tracking
					next_items.append(steps+1)
					search_queue.append(next_items)
		if elev_floor > 0: # not on bottom floor
			for move in base_poss:
				next_items = items[:]
				if type(move) == tuple:
					for step in move:
						next_items[step] = elev_floor - 1
				else:
					next_items[move] = elev_floor - 1
				next_items[0] = elev_floor - 1
				thash = hash(tuple(next_items))
				if thash not in seen and not fried_list(next_items):
					seen.add(thash) # prevent back-tracking
					next_items.append(steps+1)
					search_queue.append(next_items)

	return float('inf') # Did not find a solution	
				
		

		
if __name__ == "__main__":

	# Part 1 Solution
	
	"""
	# The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
	# The second floor contains a hydrogen generator.
	# The third floor contains a lithium generator.
	# The fourth floor contains nothing relevant.
	comps = [ 0, 1,0,2,0]
	print bfs_list_solve(comps)
	"""

	# elev_floor | G M | G M | G M | ...
	comps = [ 0,  0,0 , 0,0 , 1,1 , 1,1 , 1,2 ]
	print bfs_list_solve(comps)	

	# Part 2 Solution
	comps = [ 0,  0,0 , 0,0 , 0,0 , 0,0 , 1,1 , 1,1 , 1,2 ]
	print bfs_list_solve(comps)

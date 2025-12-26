#!/usr/bin/python

import itertools
from collections import deque

# Return True if all components are on the 4th floor
def move_complete(items):
	#if items.values().count(3) != len(items):
	for item in set(items.values()):
		if item != 3:
			return False
	return True

# Return true if a microchip is on a floor with a generator
# that it is not paired with	
def fried(items):
	for i in range(4):
		floor = [ x for x in items if items[x] == i ]
		if len([ x for x in floor if x[1] == 'G' ]) > 0:
			for component in floor:
				if component[1] == 'M' and component[0]+'G' not in floor:
						return True
	return False

# return only legal move tuples ( no unmatched generators and microchips )
# The first letters must match if the second letters do not
"""
  Integrated into bfs_move_solve
"""
def legal_moves(moves):
	return [ x for x in moves if not (x[0][1] != x[1][1] and x[0][0] != x[1][0]) ]
	
def bfs_move_solve(start):
	seen = set()
	search_queue = deque()
	seen.add(frozenset(start.items()))
	search_queue.append((start, 0))
	while len(search_queue) > 0:
		items, steps = search_queue.popleft()
		elev_floor = items.pop('floor')
		if move_complete(items):
			return steps
			
		"""
		#
		# Below section only runs if we have not found a solution yet.
		#
		"""
		
		# We can move anything on the floor with the elevator
		moveable_items = [ x for x in items if items[x] == elev_floor ]
		# We must move either 1 or 2 items
		base_poss =  moveable_items
		base_poss += [ x for x in itertools.combinations(moveable_items, 2) if not (x[0][1] != x[1][1] and x[0][0] != x[1][0]) ]
		if elev_floor < 3: # not on top floor
			for move in base_poss:
				next_items = dict(items)
				if type(move) == tuple:
					for step in move:
						next_items[step] = elev_floor + 1
				else:
					next_items[move] = elev_floor + 1
				next_items['floor'] = elev_floor + 1
				if frozenset(next_items.items()) not in seen and not fried(next_items):
					seen.add(frozenset(next_items.items())) # prevent back-tracking
					search_queue.append((next_items, steps+1))
		if elev_floor > 0: # not on bottom floor
			for move in base_poss:
				next_items = dict(items)
				if type(move) == tuple:
					for step in move:
						next_items[step] = elev_floor - 1
				else:
					next_items[move] = elev_floor - 1
				next_items['floor'] = elev_floor - 1
				if frozenset(next_items.items()) not in seen and not fried(next_items):
					seen.add(frozenset(next_items.items())) # prevent back-tracking
					search_queue.append((next_items, steps+1))

	return float('inf') # Did not find a solution
		
if __name__ == "__main__":

	# Part 1 Solution

	components = dict() # [name] = floor	
	components['floor'] = 0 # starting level of the elevator
	
	"""
	# The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
	components['HM'] = 0
	components['LM'] = 0
	# The second floor contains a hydrogen generator.
	components['HG'] = 1
	# The third floor contains a lithium generator.
	components['LG'] = 2
	# The fourth floor contains nothing relevant.
	"""
	
	# The first floor contains a strontium generator, a strontium-compatible microchip, a plutonium generator, and a plutonium-compatible microchip.
	components['SG'] = 0
	components['SM'] = 0
	components['PG'] = 0
	components['PM'] = 0
	# The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
	components['TG'] = 1
	components['RG'] = 1
	components['RM'] = 1
	components['CG'] = 1
	components['CM'] = 1
	# The third floor contains a thulium-compatible microchip.
	components['TM'] = 2
	# The fourth floor contains nothing relevant.

	print bfs_move_solve(components)
	"""
	# Part 2 Input
	
	components = dict() # reset	
	components['floor'] = 0
	components['SG'] = 0
	components['SM'] = 0
	components['PG'] = 0
	components['PM'] = 0
	components['TG'] = 1
	components['RG'] = 1
	components['RM'] = 1
	components['CG'] = 1
	components['CM'] = 1
	components['TM'] = 2
	components['EG'] = 0 # Added for part 2
	components['EM'] = 0
	components['DG'] = 0
	components['DM'] = 0

	# Too slow to solve
	print bfs_move_solve(components)
	"""

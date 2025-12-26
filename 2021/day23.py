#!/usr/bin/python


if __name__ == "__main__":

	import heapq
	from collections import deque
	
	# index map
	
	"""
	  0123456789012
	0 #############
	1 #...........#
	2 ###A#B#C#D###
	3   #A#B#C#D#
	4   #########
	"""

	walls = set()

	hall_spots = [(1,1),(2,1),(4,1),(6,1),(8,1),(10,1),(11,1)]

	stack_depth = 2

	goals_idx = {'A' : 3,
		 'B' : 5,
		 'C' : 7,
		 'D' : 9}

	goals_y_idx = {'A':0,'B':1,'C':2,'D':3}

	costs = {'A' : 1,
		 'B' : 10,
		 'C' : 100,
		 'D' : 1000}

	def set_goals(posits):
		goals = [2,2,2,2]
		for letter in ['A','B','C','D']:
			for j in range(1+stack_depth,1,-1):
				if (letter,goals_idx[letter],j) not in posits:
					goals[goals_y_idx[letter]] = j
					break
		return goals

	def letter_sat(char,occupied):
		return True if sum([ (char,goals_idx[char],y) in occupied for y in range(2,2+stack_depth) ]) == stack_depth else False

	def hall_blocked(char,occupied):
		for i,x,y in occupied:
			if i != char and x == goals_idx[char]:
				return True
		return False

	def spot_reachable(char,current_pos,goal_pos,occupied):
		if goal_pos in occupied and current_pos != goal_pos:
			return (False,float('inf'))
		if goal_pos == current_pos:
			return (True,0)
		seen = set()
		seen.add(current_pos)
		q = deque()
		q.append((0,current_pos))
		while len(q) > 0:
			steps,pos = q.popleft()
			if pos == goal_pos:
				return (True,steps)
			x,y = pos
			for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
				nx,ny = x+dx,y+dy
				if (nx,ny) not in walls and (nx,ny) not in occupied and (nx,ny) not in seen:
					q.append((steps+1,(nx,ny)))
					seen.add((nx,ny))
		return (False,float('inf'))
	
	def goal_reachable(char,current_pos,occupied,goals):
		# is hallway blocked by another type of char?
		if hall_blocked(char,occupied):
			return (False,float('inf'))
		x,y = current_pos
		if x == goals_idx[char] and y >= goals[goals_y_idx[char]]:
			return (False,float('inf'))
		blocked_set = { (x,y) for i,x,y in occupied }
		seen = set()
		seen.add(current_pos)
		q = deque()
		q.append((current_pos,0))
		while len(q) > 0:
			pos,steps = q.popleft()
			x,y = pos
			# reached a goal, already verified hall not blocked
			if x == goals_idx[char] and y == goals[goals_y_idx[char]]:
				return(True,steps)
			else:
				for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
					nx,ny = x+dx,y+dy
					if (nx,ny) not in walls and (nx,ny) not in blocked_set and (nx,ny) not in seen:
						q.append(((nx,ny),steps+1))
						seen.add((nx,ny))
		return (False,float('inf'))
	
	def heap_search(posits,goals):

		seen_configs = { hash(frozenset(posits)) }
		q = []
		heapq.heapify(q)
		heapq.heappush(q,(0,goals[:],posits[:]))
		while len(q) > 0:
			cost, goals, elements = heapq.heappop(q)
			#print(cost,elements)
			all_sat = True
			for letter in ['A','B','C','D']:
				if not letter_sat(letter,elements):
					all_sat = False
			if all_sat:
				return cost
			for element in elements:
				char,x,y = element
				# don't continue if this letter is solved or if this
				# current letter is in the goal position
				if not letter_sat(char,elements):
					rest_elements = [ j for j in elements if j != element ]
					success,steps = goal_reachable(char,(x,y),rest_elements,goals)
					# can we move this letter to a goal position?
					if success:
						gy = goals[goals_y_idx[char]]
						new_goals = goals[:]
						new_goals[goals_y_idx[char]] = max(2,goals[goals_y_idx[char]]-1)
						config = { p for p in rest_elements }
						config.add((char,goals_idx[char],gy))
						heapq.heappush(q,(cost+costs[char]*steps,new_goals,rest_elements+[(char,goals_idx[char],gy)]))
						seen_configs.add(hash(frozenset(config)))
					elif y != 1:
						blocked_set = { (p,q) for i,p,q in elements }
						for spot in hall_spots:
							reachable,steps = spot_reachable(char,(x,y),spot,blocked_set)
							if reachable:
								config = { p for p in rest_elements }
								nx,ny = spot
								config.add((char,nx,ny))
								if hash(frozenset(config)) not in seen_configs:
									heapq.heappush(q,(cost+costs[char]*steps,goals,rest_elements+[(char,nx,ny)]))
									seen_configs.add(hash(frozenset(config)))
		return float('inf')

	# Part 1 Solution

	posits = []

	with open("day23_input","r") as infile:
		y = 0
		for line in infile.readlines():
			for idx,char in enumerate(line.rstrip()):
				if char == '#':
					walls.add((idx,y))
				elif char in ['A','B','C','D']:
					posits.append((char,idx,y))
			y += 1
	goals = set_goals(posits)
	print(heap_search(posits,goals))

	# Part 2 Solution

	posits = []
	walls = set()
	add1='  #D#C#B#A#'
	add2='  #D#B#A#C#'
	lines = []
	with open("day23_input","r") as infile:
		for line in infile.readlines():
			lines.append(line.rstrip())
	lines.insert(3,add1)
	lines.insert(4,add2)
	stack_depth = 4
	y = 0
	for line in lines:
		for idx,char in enumerate(line.rstrip()):
			if char == '#':
				walls.add((idx,y))
			elif char in ['A','B','C','D']:
				posits.append((char,idx,y))
		y += 1
	goals = set_goals(posits)
	print(heap_search(posits,goals))


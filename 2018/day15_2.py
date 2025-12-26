#!/usr/bin/python

from collections import deque


map = []
elfs = []
goblins = []

class Pathway:

	def __init__(self, steps):
		self.steps = steps

# print the map, including all Elf and Goblin positions
def print_map():
	row_idx = 0
	for row in map:
		out = row[:]
		for unit in elfs:
			if unit.y == row_idx and unit.alive():
				out[unit.x] = unit.char
		for unit in goblins:
			if unit.y == row_idx and unit.alive():
				out[unit.x] = unit.char
		print ''.join(out)
		row_idx += 1

# list of all Elf and Goblin occupied spaces
#def occupied():
#	return [ e.loc() for e in elfs if e.alive() ] + [ g.loc() for g in goblins if g.alive() ]

def occ_set():
	o = { e.loc() for e in elfs if e.alive() }
	return o.union( { g.loc() for g in goblins if g.alive() } )
	
# return enemy unit to attack
def get_adjacent_target(loc, char):
	targets = []
	x = loc[0]
	y = loc[1]
	dirs = { (x+1, y) , (x-1 , y), (x, y+1), (x, y-1) }
	if char == "E":
		targets = [ g for g in goblins if g.alive() and g.loc() in dirs ]
	else:
		targets = [ e for e in elfs if e.alive() and e.loc() in dirs ]
	if len(targets) == 0:
		return None
	if len(targets) == 1:
		return targets[0]
	targets.sort(key = lambda x : x.hp)
	min_hp = targets[0].hp
	targets = filter(lambda x : x.hp == min_hp, targets)
	targets = sorted(targets, key = lambda a : a.sort_loc())
	return targets[0]
	
def bfs_paths(start, dest):
	if start == dest:
		return None
		
	valid_paths = []
	min_path_len = 1000000000
	
	paths_to_eval = deque()
	paths_to_eval.append( Pathway([start]) )
		
	blocked = occ_set()
	
	while len(paths_to_eval) != 0:
		current_path = paths_to_eval.popleft() # Remove a path from the queue
		current_path = current_path.steps
		pathset = set(current_path)
		#print pathset
		#print current_path
		current_node = current_path[-1] # Look at the last location visited
		if current_node == dest: # Found a valid pathway to the destination
			if len(current_path) <= min_path_len:
				min_path_len = len(current_path)
				valid_paths.append(current_path)
		else:
			blocked.add(current_node)
		if len(current_path) < min_path_len - 1: # continue exploring from this node (if on shorter path)
			x,y = current_node			
			if y > 0: # search up
				n = (x,y-1)
				if n not in blocked and n not in pathset and map[y-1][x] == '.':
					current_path.append(n)
					paths_to_eval.append( Pathway(list(current_path)) )
					current_path.pop()
					blocked.add(n)
			if x > 0: # search left
				n = (x-1,y)
				if n not in blocked and n not in pathset and map[y][x-1] == '.':
					current_path.append(n)
					paths_to_eval.append( Pathway(list(current_path))  )
					current_path.pop()
					blocked.add(n)
			if x < len(map[y])-1: # search right
				n = (x+1,y)
				if n not in blocked and n not in pathset and map[y][x+1] == '.':
					current_path.append(n)
					paths_to_eval.append( Pathway(list(current_path)) )
					current_path.pop()
					blocked.add(n)
			if y < len(map)-1: # search down
				n = (x,y+1)
				if n not in blocked and n not in pathset and map[y+1][x] == '.':
					current_path.append(n)
					paths_to_eval.append( Pathway(list(current_path)) )
					current_path.pop()
					blocked.add(n)
	if len(valid_paths) == 0:
		return None
	
	return filter( lambda x : len(x) == min_path_len, valid_paths )
	
def bfs_steps(start, dest):
	if start == dest:
		return 0
	to_visit = []		
	to_visit.append((start, 0))
		
	blocked = occ_set()
		
	while len(to_visit) != 0:
		current, depth = to_visit[0]
		x,y = current
		blocked.add(current)
		if current == dest:
			return depth
		if y > 0: # search up
			n = (x,y-1)
			if map[y-1][x] == '.' and n not in blocked:
				to_visit.append( (n, depth + 1))
				blocked.add(n)
		if x < len(map[y])-1: # search right
			n = (x+1,y)
			if map[y][x+1] == '.' and n not in blocked:
				to_visit.append( (n, depth + 1) )
				blocked.add(n)
		if y < len(map)-1: # search down
			n = (x,y+1)
			if map[y+1][x] == '.' and n not in blocked:
				to_visit.append( (n, depth + 1) )
				blocked.add(n)
		if x > 0: # search left
			n = (x-1,y)
			if map[y][x-1] == '.' and n not in blocked:
				to_visit.append( (n, depth + 1) )
				blocked.add(n)
		to_visit = to_visit[1:]
	
	# No path
	return None
		
	
def choose_target(loc, targets):
	accessible = []
	evaluated = []
	if len(targets) == 0:
		return None
	accessible = [ (bfs_steps(loc, target), target) for target in targets ]
	if len(accessible) == 0:
		return None
	evaluated = [ t for t in accessible if t[0] != None ]
	if len(evaluated) == 0:
		return None
	evaluated.sort(key = lambda x : x[0])
	min_dist = evaluated[0][0]
	accessible = [ t[1] for t in evaluated if t[0] == min_dist ]
	accessible = sorted(accessible, key = lambda a : (a[1],a[0]))
	return accessible[0]	

class Unit:

	def __init__(self, x, y, char, pow):
		self.hp = 200
		self.x = x
		self.y = y
		self.char = char
		self.pow = pow
		
	def loc(self):
		return (self.x,self.y)
		
	# for reading order
	def sort_loc(self):
		return (self.y,self.x)
		
	def alive(self):
		if self.hp > 0:
			return True
		return False
	
	def in_range(self):
		spots = set()
		if self.x > 0 and map[self.y][self.x-1] == '.':
			spots.add((self.x-1,self.y))
		if self.x < len(map[self.y])-1 and map[self.y][self.x+1] == '.':
			spots.add((self.x+1,self.y))
		if self.y > 0 and map[self.y-1][self.x] == '.':
			spots.add((self.x,self.y-1))
		if self.y < len(map)-1 and map[self.y+1][self.x] == '.':
			spots.add((self.x,self.y+1))
		return spots		

if __name__ == "__main__":

	# Part 2 Solution
	
	low = 1
	high = 40
	pow_up = (high + low) / 2
	while low <= high:
		
		# game reset
		print "Reset with power up set to: ", pow_up
		fail = False		
		map = []
		elfs = []
		goblins = []
		
		with open("day15_input", "r") as infile:
			row_idx = 0
			for line in infile.readlines():
				line = list(line.strip())
				for x in range(len(line)):
					if line[x] == "E":
						elfs.append(Unit(x,row_idx,line[x],3+pow_up))
						line[x] = '.'
					elif line[x] == "G":
						goblins.append(Unit(x,row_idx,line[x],3))
						line[x] = '.'
				map.append(line)
				row_idx += 1

		round = 0
		endgame = False
		while True:
			# Find living units
			units = [ e for e in elfs if e.alive() ] + [ g for g in goblins if g.alive() ]
			# Sorted by reading order for turn order

			for elf in elfs:
				if not elf.alive():		
					endgame = True
			
			units = sorted(units, key = lambda a : a.sort_loc())
			if endgame == True:
				break
			
			# take each turn
			for unit in units:
				#print "Unit ", unit.char, " at ", unit.loc(), " begins turn."
				range_locs = set()
				if unit.char == "E":
					alive = [ g for g in goblins if g.alive() ]
					for g in alive:
						range_locs = range_locs.union( g.in_range() )
				else: # is a Goblin
					alive = [ e for e in elfs if e.alive() ]
					for e in alive:
						range_locs = range_locs.union( e.in_range() )
				if len(range_locs) == 0:
					endgame = True
					break
				# Don't move if in range, or if there is nowhere to move to
				if unit.alive() and unit.loc() not in range_locs and len(range_locs.difference(occ_set())) != 0:				
					opponent = choose_target(unit.loc(), range_locs.difference(occ_set()))
					next_step = None
					moves = bfs_paths(unit.loc(), opponent)
					if moves != None:
						if len(moves) > 1:
							first_steps = []
							for move in moves:
								first_steps.append(move[1])
							first_steps = sorted(first_steps, key = lambda a : (a[1],a[0]))
							next_step = first_steps[0]
						else:
							next_step = moves[0][1]
						unit.x = next_step[0]
						unit.y = next_step[1]
				# Begin attack if in range
				if unit.alive() and unit.loc() in range_locs:
					target = get_adjacent_target(unit.loc(), unit.char)
					if target != None:
						target.hp -= unit.pow
			
			# Check for End Game
			if endgame == True:
				break
			round += 1
			
		### END GAME SCORE ###
		
		for elf in elfs:
			if not elf.alive():
				fail = True
		if not fail:
			hp_total = 0
			hp_total += sum( [ e.hp for e in elfs if e.alive() ] )
			hp_total += sum( [ g.hp for g in goblins if g.alive() ] )
			print "Power Up", pow_up
			print "Rounds: ", round
			print "HP Left: ", hp_total	
			print "Score", round * hp_total
			high = pow_up
		else:
			low = pow_up
		pow_up = (high + low) / 2

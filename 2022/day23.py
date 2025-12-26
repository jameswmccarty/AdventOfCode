#!/usr/bin/python

def calc_area(elves):
	min_x = min([e[0] for e in elves])
	max_x = max([e[0] for e in elves])
	min_y = min([e[1] for e in elves])
	max_y = max([e[1] for e in elves])	
	return (max_x+1-min_x)*(max_y+1-min_y)-len(elves)

def pretty_print(elves):
	min_x = min([e[0] for e in elves])
	max_x = max([e[0] for e in elves])
	min_y = min([e[1] for e in elves])
	max_y = max([e[1] for e in elves])	
	for y in range(min_y,max_y+1):
		for x in range(min_x,max_x+1):
			if (x,y) in elves:
				print('#',end='')
			else:
				print('.',end='')
		print()

def bfs_rounds(elves,rounds,find_stop=False):
	all_dirs = ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1))
	checks = { 'N' : ((-1,-1),(0,-1),(1,-1)),
		   'S' : ((-1,1),(0,1),(1,1)),
		   'W' : ((-1,0),(-1,1),(-1,-1)),
		   'E' : ((1,0),(1,1),(1,-1)) }
	deltas = { 'N' : (0,-1),
		   'S' : (0,1),
		   'W' : (-1,0),
		   'E' : (1,0) }
	check_order = ['N','S','W','E']
	for r in range(rounds):
		#pretty_print(elves)
		#print('-----',r,'-----')
		next_elves = set()
		area_counts = dict()
		next_area_by_elf = dict()
		for elf in elves:
			x,y = elf
			moving = False
			for dx,dy in all_dirs:
				if (x+dx,y+dy) in elves:
					moving = True
			if not moving:
				next_elves.add(elf)
			elif moving:
				found_move = False
				for option in check_order:
					blocked = False
					for dx,dy in checks[option]:
						if (x+dx,y+dy) in elves:
							blocked = True
					if not blocked and not found_move:
						next_pos = (x+deltas[option][0],y+deltas[option][1])
						if next_pos not in area_counts:
							area_counts[next_pos] = 1
						else:
							area_counts[next_pos] += 1
						next_area_by_elf[elf] = next_pos
						found_move = True
				if not found_move:
					next_elves.add(elf)
		for e,p in next_area_by_elf.items():
			if area_counts[p] == 1:
				next_elves.add(p)
			else:
				next_elves.add(e)
		elves = next_elves
		head = check_order.pop(0)
		check_order.append(head)
	return elves			

def stable_rounds(elves):
	all_dirs = ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1))
	checks = { 'N' : ((-1,-1),(0,-1),(1,-1)),
		   'S' : ((-1,1),(0,1),(1,1)),
		   'W' : ((-1,0),(-1,1),(-1,-1)),
		   'E' : ((1,0),(1,1),(1,-1)) }
	deltas = { 'N' : (0,-1),
		   'S' : (0,1),
		   'W' : (-1,0),
		   'E' : (1,0) }
	check_order = ['N','S','W','E']
	r = 0
	while True:
		next_elves = set()
		area_counts = dict()
		next_area_by_elf = dict()
		for elf in elves:
			x,y = elf
			moving = False
			for dx,dy in all_dirs:
				if (x+dx,y+dy) in elves:
					moving = True
			if not moving:
				next_elves.add(elf)
			elif moving:
				found_move = False
				for option in check_order:
					blocked = False
					for dx,dy in checks[option]:
						if (x+dx,y+dy) in elves:
							blocked = True
					if not blocked and not found_move:
						next_pos = (x+deltas[option][0],y+deltas[option][1])
						if next_pos not in area_counts:
							area_counts[next_pos] = 1
						else:
							area_counts[next_pos] += 1
						next_area_by_elf[elf] = next_pos
						found_move = True
				if not found_move:
					next_elves.add(elf)
		if len(next_elves) == len(elves):
			return r+1
		for e,p in next_area_by_elf.items():
			if area_counts[p] == 1:
				next_elves.add(p)
			else:
				next_elves.add(e)
		elves = next_elves
		head = check_order.pop(0)
		check_order.append(head)
		r += 1


if __name__ == "__main__":

	elves = set()

	# Part 1 Solution
	with open('day23_input','r') as infile:
		y = 0
		for line in infile.readlines():
			for x,char in enumerate(line.strip()):
				if char == '#':
					elves.add((x,y))
			y += 1

	print(calc_area(bfs_rounds(elves,10)))

	# Part 2 Solution
	print(stable_rounds(elves))




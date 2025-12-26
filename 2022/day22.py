#!/usr/bin/python

air = set()
walls = set()
face_map = dict()
for _ in range(1,7):
	face_map[_] = set()

# new direction of motion from rotation
def rotate(facing,d):
	if d == 'L':
		if facing == (1,0): # >
			return (0,-1)
		if facing == (0,1): # v
			return (1,0)
		if facing == (-1,0): # <
			return (0,1)
		if facing == (0,-1): # ^
			return (-1,0)
	elif d == 'R':
		if facing == (1,0): # >
			return (0,1)
		if facing == (0,1): # v
			return (-1,0)
		if facing == (-1,0): # <
			return (0,-1)
		if facing == (0,-1): # ^
			return (1,0)

def solve_path(pos,facing,path):
	path = list(path)
	while len(path) > 0:
		move = ' '
		while len(path) > 0 and move[-1] != 'R' and move[-1] != 'L':
			move += path.pop(0)
		steps = int(move.strip('R').strip('L').strip())
		for step in range(steps):
			x,y = pos
			if (x+facing[0],y+facing[1]) in air: # open
				pos = (x+facing[0],y+facing[1])
			elif (x+facing[0],y+facing[1]) in walls: # hit wall
				break
			else: # wrap if not blocked
				if facing[0] == 0: # movement in the y dir
					if facing[1] == -1:
						max_y = max(max([ p[1] for p in air if p[0] == x]),max([ p[1] for p in walls if p[0] == x]))
						if (x,max_y) not in walls:
							pos = (x,max_y)
					elif facing[1] == 1:
						min_y = min(min([ p[1] for p in air if p[0] == x]),min([ p[1] for p in walls if p[0] == x]))
						if (x,min_y) not in walls:
							pos = (x,min_y)
				elif facing[1] == 0: # movement in the x dir
					if facing[0] == -1:
						max_x = max(max([ p[0] for p in air if p[1] == y]),max([ p[0] for p in walls if p[1] == y]))
						if (max_x,y) not in walls:
							pos = (max_x,y)
					elif facing[0] == 1:
						min_x = min(min([ p[0] for p in air if p[1] == y]),min([ p[0] for p in walls if p[1] == y]))
						if (min_x,y) not in walls:
							pos = (min_x,y)
		if 'R' in move or 'L' in move:
			facing = rotate(facing,move[-1])
	password = pos[0]*4 + pos[1]*1000
	if facing == (1,0):
		password += 0
	if facing == (-1,0):
		password += 2
	if facing == (0,1):
		password += 1
	if facing == (0,-1):
		password += 3
	return(password)

# if we are moving off of a cube face
# return the landing point and new facing direction
def transition_face(pos,facing):
	""" # input map (manually determined)
	-12
	-3-
	45-
	6--
	"""

	"""
	(1,0 ): # >
	(0,1) : # v
	(-1,0): # <
	(0,-1): # ^
	"""

	""" # moves off faces (manually determined)
	1U -> 6R
	1L -> 4R
	2U -> 6U
	2R -> 5L
	2D -> 3L
	3L -> 4D
	3R -> 2U
	5R -> 2L
	5D -> 6L
	4U -> 3R
	4L -> 1R
	6R -> 5U
	6D -> 2D
	6L -> 1D
	"""

	x,y = pos
	face = None
	for k,v in face_map.items():
		if pos in v:
			face = k
			break

	#print("Pos ",pos,"facing",facing,"face",face)

	#1U -> 6R
	if face == 1 and facing == (0,-1):
		return (1, x+100),(1,0) 
	#1L -> 4R
	if face == 1 and facing == (-1,0):
		return (1, (51-y)+100 ),(1,0) # check
	#2U -> 6U
	if face == 2 and facing == (0,-1):
		return (x-100,200),(0,-1) 
	#2R -> 5L
	if face == 2 and facing == (1,0):
		return (100,(51-y)+100),(-1,0) 
	#2D -> 3L
	if face == 2 and facing == (0,1):
		return (100,x-50),(-1,0) 
	#3L -> 4D
	if face == 3 and facing == (-1,0):
		return (y-50,101),(0,1) 
	#3R -> 2U
	if face == 3 and facing == (1,0):
		return (y+50,50),(0,-1) 
	#5R -> 2L
	if face == 5 and facing == (1,0):
		return (150,51-(y-100)),(-1,0) 
	#5D -> 6L
	if face == 5 and facing == (0,1):
		return (50,x+100),(-1,0)
	#4U -> 3R
	if face == 4 and facing == (0,-1):
		return (51,50+x),(1,0) 
	#4L -> 1R
	if face == 4 and facing == (-1,0):
		return (51,51-(y-100)),(1,0) 
	#6R -> 5U
	if face == 6 and facing == (1,0):
		return (y-100,150),(0,-1) 
	#6D -> 2D
	if face == 6 and facing == (0,1):
		return (x+100,1),(0,1) 
	#6L -> 1D
	if face == 6 and facing == (-1,0):
		return (y-100,1),(0,1) 


def solve_cube(pos,facing,path):
	path = list(path)
	while len(path) > 0:
		move = ' '
		while len(path) > 0 and move[-1] != 'R' and move[-1] != 'L':
			move += path.pop(0)
		steps = int(move.strip('R').strip('L').strip())
		for step in range(steps):
			x,y = pos
			if (x+facing[0],y+facing[1]) in air: # open
				pos = (x+facing[0],y+facing[1])
			elif (x+facing[0],y+facing[1]) in walls: # hit wall
				break
			else: # wrap if not blocked
				new_pos,new_facing = transition_face(pos,facing)
				if new_pos in air:
					pos = new_pos
					facing = new_facing
				else: # hit wall
					break
		if 'R' in move or 'L' in move:
			facing = rotate(facing,move[-1])
	password = pos[0]*4 + pos[1]*1000
	if facing == (1,0):
		password += 0
	if facing == (-1,0):
		password += 2
	if facing == (0,1):
		password += 1
	if facing == (0,-1):
		password += 3
	return(password)

if __name__ == "__main__":


	path = ''
	pos = None

	# Part 1 Solution
	with open('day22_input','r') as infile:
		y = 1
		for line in infile.readlines():
			if '.' in line or '#' in line:
				for x,char in enumerate(line.rstrip()):
					if char == '.':
						air.add((x+1,y))
					elif char == '#':
						walls.add((x+1,y))
				y += 1
			elif len(line.strip()) > 0:
				path = line.strip()

	x = 1
	while True:
		if (x,1) in air:
			pos = (x,1)
			break
		x += 1

	print(solve_path(pos,(1,0),path))


	# Part 2 Solution
	""" # input map (manually determined)
	-12
	-3-
	45-
	6--
	"""

	# x // 50, y // 50
	faces = { (1,0) : 1,
			  (2,0) : 2,
			  (1,1) : 3,
			  (0,2) : 4,
			  (1,2) : 5,
			  (0,3) : 6 }

	with open('day22_input','r') as infile:
		y = 1
		for line in infile.readlines():
			if '.' in line or '#' in line:
				for x,char in enumerate(line.rstrip()):
					if char == '.':
						face = faces[(x//50,(y-1)//50)]
						face_map[face].add((x+1,y))
				y += 1

	"""
	for y in range(0,202):
		print(str(y).zfill(3),end=' ')
		for x in range(0,152):
			found = False
			for k,v in face_map.items():
				if (x,y) in v:
					print(k,end='')
					found = True
			if (x,y) in walls:
				print('#',end='')
			elif not found:
				print('.',end='')
		print()
	"""

	print(solve_cube(pos,(1,0),path))



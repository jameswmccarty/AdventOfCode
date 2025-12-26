#!/usr/bin/python

moveable_rock_pos = set()

class Rock:

	deltas = { "N" : (0,-1),
			   "S" : (0,1),
			   "E" : (1,0),
			   "W" : (-1,0) }

	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.x_dim = None
		self.y_dim = None

	def dims(self,x,y):
		self.x_dim = x
		self.y_dim = y

	def pos(self):
		return (self.x,self.y)

	def move(self,d,cubes):
		global moveable_rock_pos
		dx,dy = self.deltas[d]
		nx,ny = self.x+dx,self.y+dy
		if (nx,ny) not in moveable_rock_pos and (nx,ny) not in cubes and nx >= 0 and ny >= 0 and nx < self.x_dim and ny < self.y_dim:
			while (nx,ny) not in moveable_rock_pos and (nx,ny) not in cubes and nx >= 0 and ny >= 0 and nx < self.x_dim and ny < self.y_dim:
				moveable_rock_pos.discard((self.x,self.y))
				moveable_rock_pos.add((nx,ny))
				self.x,self.y = nx,ny
				nx,ny = nx+dx,ny+dy
			return True
		return False

	def score(self):
		return self.y_dim - self.y


if __name__ == "__main__":

	# Part 1 Solution
	fixed_rocks = set()
	moveable_rocks = set()
	with open("day14_input", "r") as infile:
		y = 0
		for line in infile:
			x_dim = len(line.strip())
			for x,c in enumerate(line.strip()):
				if c == "O":
					moveable_rocks.add(Rock(x,y))
				if c == "#":
					fixed_rocks.add((x,y))
			y += 1

	for e in moveable_rocks:
		e.dims(y,x_dim)

	moveable_rock_pos = { r.pos() for r in moveable_rocks }
	while any( r.move("N",fixed_rocks) for r in moveable_rocks ):
		continue

	print(sum( r.score() for r in moveable_rocks ))

	# Part 2 Solution

	fixed_rocks = set()
	moveable_rocks = set()
	with open("day14_input", "r") as infile:
		y = 0
		for line in infile:
			x_dim = len(line.strip())
			for x,c in enumerate(line.strip()):
				if c == "O":
					moveable_rocks.add(Rock(x,y))
				if c == "#":
					fixed_rocks.add((x,y))
			y += 1

	for e in moveable_rocks:
		e.dims(y,x_dim)

	moveable_rock_pos = { r.pos() for r in moveable_rocks }
	cycles = dict()
	cycles[hash(frozenset(moveable_rock_pos))] = 0
	c = 0
	c_max = 1000000000
	looped = False
	while c < c_max:

		for d in "NWSE":
			while any( r.move(d,fixed_rocks) for r in moveable_rocks ):
				continue
		cycle_set = hash(frozenset(moveable_rock_pos))
		if cycle_set in cycles and not looped:
			#print(cycles[cycle_set],sum( r.score() for r in moveable_rocks ),c)
			cycles[cycle_set].append(c)
			c_max = ( c_max - cycles[cycle_set][0] )  % (cycles[cycle_set][1] - cycles[cycle_set][0])
			looped = True
			c = 0
		else:
			cycles[cycle_set] = [c]
		#print(cycle,sum( r.score() for r in moveable_rocks ))
		c += 1
print(sum( r.score() for r in moveable_rocks ))

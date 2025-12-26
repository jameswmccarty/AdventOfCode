#!/usr/bin/python

# Advent of Code 2024 Day 15

walls = set()
move_deltas = {'^': (0,-1), '>': (1,0), '<':(-1,0), 'v': (0,1)}
x_dim, y_dim = 0, 0

class Box:

	boxes = dict()

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.boxes[(x,y)] = self

	def gps(self):
		return self.x + 100*self.y

	def move_by(self, dx, dy):
		nx, ny = self.x + dx, self.y + dy
		if (nx, ny) in walls:
			return False
		if (nx, ny) in Box.boxes:
			if Box.boxes[(nx, ny)].move_by(dx, dy):
				t = Box.boxes.pop((self.x, self.y))
				self.x = nx
				self.y = ny
				Box.boxes[(nx, ny)] = t
				return True
			return False
		t = Box.boxes.pop((self.x, self.y))
		self.x = nx
		self.y = ny
		Box.boxes[(nx, ny)] = t
		return True

class WideBox:

	boxes = dict()

	def __init__(self, lx, y):
		self.lx = lx
		self.rx = lx+1
		self.y = y
		self.boxes[(self.lx,y)] = self
		self.boxes[(self.rx,y)] = self

	def gps(self):
		return self.lx + 100*self.y

	def can_move_by(self, dx, dy):
		lnx = self.lx + dx
		rnx = self.rx + dx
		ny = self.y + dy
		if (lnx, ny) in walls or (rnx, ny) in walls:
			return False
		moved1 = False
		moved2 = False
		cased1 = False
		cased2 = False
		if (lnx, ny) in WideBox.boxes and WideBox.boxes[(lnx, ny)] != self:
			cased1 = True
			if WideBox.boxes[(lnx, ny)].can_move_by(dx, dy):
				moved1 = True
		if (rnx, ny) in WideBox.boxes and WideBox.boxes[(rnx, ny)] != self:
			cased2 = True
			if WideBox.boxes[(rnx, ny)].can_move_by(dx, dy):
				moved2 = True
		if cased1 and cased2:
			if moved1 and moved2: 
				return True
			return False
		elif cased2:
			if moved2: 
				return True
			return False
		elif cased1:
			if moved1: 
				return True
			return False
		return True

	def move_by(self, dx, dy):
		lnx = self.lx + dx
		rnx = self.rx + dx
		ny = self.y + dy
		if (lnx, ny) in walls or (rnx, ny) in walls:
			return False
		moved1 = False
		moved2 = False
		cased1 = False
		cased2 = False
		if (lnx, ny) in WideBox.boxes and WideBox.boxes[(lnx, ny)] != self:
			cased1 = True
			if WideBox.boxes[(lnx, ny)].move_by(dx, dy):
				moved1 = True
		if (rnx, ny) in WideBox.boxes and WideBox.boxes[(rnx, ny)] != self:
			cased2 = True
			if WideBox.boxes[(rnx, ny)].move_by(dx, dy):
				moved2 = True
		if cased1 and cased2:
			if moved1 and moved2: 
				t1 = WideBox.boxes.pop((self.lx, self.y))
				t2 = WideBox.boxes.pop((self.rx, self.y))
				self.lx = lnx
				self.rx = rnx
				self.y = ny
				WideBox.boxes[(lnx, ny)] = self
				WideBox.boxes[(rnx, ny)] = self
				return True
			return False
		elif cased2:
			if moved2: 
				t1 = WideBox.boxes.pop((self.lx, self.y))
				t2 = WideBox.boxes.pop((self.rx, self.y))
				self.lx = lnx
				self.rx = rnx
				self.y = ny
				WideBox.boxes[(lnx, ny)] = self
				WideBox.boxes[(rnx, ny)] = self
				return True
			return False
		elif cased1:
			if moved1: 
				t1 = WideBox.boxes.pop((self.lx, self.y))
				t2 = WideBox.boxes.pop((self.rx, self.y))
				self.lx = lnx
				self.rx = rnx
				self.y = ny
				WideBox.boxes[(lnx, ny)] = self
				WideBox.boxes[(rnx, ny)] = self
				return True
			return False
		t1 = WideBox.boxes.pop((self.lx, self.y))
		t2 = WideBox.boxes.pop((self.rx, self.y))
		self.lx = lnx
		self.rx = rnx
		self.y = ny
		WideBox.boxes[(lnx, ny)] = self
		WideBox.boxes[(rnx, ny)] = self
		return True

def print_state(pos):
	print("Bot pos",pos)
	for y in range(y_dim):
		for x in range(x_dim):
			if (x,y) in walls: print('#', end='')
			elif (x,y) in Box.boxes: print('O',end='')
			elif (x,y) == pos: print('@',end='')
			else: print('.',end='')
		print()
	print()

def print_state2(pos):
	print("Bot pos",pos)
	for y in range(y_dim):
		for x in range(x_dim):
			if (x,y) in walls: print('#', end='')
			elif (x,y) in WideBox.boxes:
				if WideBox.boxes[(x,y)].lx == x: print('[',end='')
				else: print(']',end='')
			elif (x,y) == pos: print('@',end='')
			else: print('.',end='')
		print()
	print()

if __name__ == "__main__":

	# Part 1 Solution
	bot = None
	moves = ''
	y = 0
	with open("day15_input", "r") as infile:
		for line in infile.readlines():
			if any(c in line for c in '<v>^'):
				moves += line.strip()
			elif len(line.strip()) > 0:
				x_dim = len(line.strip())
				for x, char in enumerate(line.strip()):
					if char == '#': walls.add((x, y))
					elif char == 'O': Box(x, y)
					elif char == '@': bot = (x, y)
				y += 1
	y_dim = y

	for move in moves:
		#print("Move",move)
		#print_state(bot)
		x, y = bot
		dx, dy = move_deltas[move]
		nx, ny = x+dx, y+dy
		if (nx, ny) not in walls and (nx, ny) not in Box.boxes:
			bot = (nx, ny)
		elif (nx, ny) not in walls and (nx, ny) in Box.boxes:
			if Box.boxes[(nx, ny)].move_by(dx, dy):
				bot = (nx, ny)
	print(sum(box.gps() for box in Box.boxes.values()))

	# Part 2 Solution
	bot = None
	moves = ''
	y = 0
	walls = set()
	with open("day15_input", "r") as infile:
		for line in infile.readlines():
			if any(c in line for c in '<v>^'):
				moves += line.strip()
			elif len(line.strip()) > 0:
				x_dim = 2*len(line.strip())
				x = 0
				for char in line.strip():
					if char == '#': walls.add((x, y)); walls.add((x+1, y))
					elif char == 'O': WideBox(x, y)
					elif char == '@': bot = (x, y)
					x += 2
				y += 1
	y_dim = y

	for move in moves:
		#print("Move",move)
		#print_state2(bot)
		x, y = bot
		dx, dy = move_deltas[move]
		nx, ny = x+dx, y+dy
		if (nx, ny) not in walls and (nx, ny) not in WideBox.boxes:
			bot = (nx, ny)
		elif (nx, ny) not in walls and (nx, ny) in WideBox.boxes:
			if WideBox.boxes[(nx, ny)].can_move_by(dx, dy):
				WideBox.boxes[(nx, ny)].move_by(dx, dy)
				bot = (nx, ny)
	print(sum(box.gps() for box in WideBox.boxes.values())//2)

#!/usr/bin/python

carts = []
map = []

def display_map():
	row_idx = 0
	for row in map:
		line = ''.join(row)
		for cart in carts:
			if cart.y == row_idx:
				line = list(line)
				line[cart.x] = cart.as_char()
				line = ''.join(line)
		row_idx += 1
		print line,
	print

class Cart:

	def __init__(self, x, y, pic):
		
		# 0 - left
		# 1 - straight
		# 2 - right
		self.turn = 0
		
		# 0 - ^ - up
		# 1 - > - right
		# 2 - v - down
		# 3 - < - left
		if pic == "^":
			self.dir  = 0
		elif pic == ">":
			self.dir  = 1
		elif pic == "v":
			self.dir  = 2
		elif pic == "<":
			self.dir  = 3
		
		self.x = x
		self.y = y
		self.rmv = False

	def as_char(self):
		if self.dir == 0:
			return "^"
		elif self.dir == 1:
			return ">"
		elif self.dir == 2:
			return "v"
		elif self.dir == 3:
			return "<"
	
	def move(self):
		if self.dir == 0:
			self.y -= 1
		elif self.dir == 1:
			self.x += 1
		elif self.dir == 2:
			self.y += 1
		elif self.dir == 3:
			self.x -= 1
		
		for cart in carts:
			if cart != self:
				if cart.x == self.x and cart.y == self.y:
					return False
			
		track = map[self.y][self.x]
		
		if track == '/':
			if self.dir == 3:
				self.dir = 2
			elif self.dir == 0:
				self.dir = 1
			elif self.dir == 2:
				self.dir = 3
			elif self.dir == 1:
				self.dir = 0
		elif track == '\\':
			if self.dir == 3:
				self.dir = 0
			elif self.dir == 0:
				self.dir = 3
			elif self.dir == 2:
				self.dir = 1
			elif self.dir == 1:
				self.dir = 2
		elif track == '+':
			if self.turn == 0: # left
				self.dir -= 1
				if self.dir < 0:
					self.dir = 3
			elif self.turn == 2: # right
				self.dir += 1
				self.dir %= 4
			self.turn += 1
			self.turn %= 3
		return True

	def rm_move(self):
		if self.dir == 0:
			self.y -= 1
		elif self.dir == 1:
			self.x += 1
		elif self.dir == 2:
			self.y += 1
		elif self.dir == 3:
			self.x -= 1
		
		for cart in carts:
			if cart != self:
				if cart.x == self.x and cart.y == self.y:
					self.rmv = True	
					cart.rmv = True
			
		track = map[self.y][self.x]
		
		if track == '/':
			if self.dir == 3:
				self.dir = 2
			elif self.dir == 0:
				self.dir = 1
			elif self.dir == 2:
				self.dir = 3
			elif self.dir == 1:
				self.dir = 0
		elif track == '\\':
			if self.dir == 3:
				self.dir = 0
			elif self.dir == 0:
				self.dir = 3
			elif self.dir == 2:
				self.dir = 1
			elif self.dir == 1:
				self.dir = 2
		elif track == '+':
			if self.turn == 0: # left
				self.dir -= 1
				if self.dir < 0:
					self.dir = 3
			elif self.turn == 2: # right
				self.dir += 1
				self.dir %= 4
			self.turn += 1
			self.turn %= 3
		
if __name__ == "__main__":

	# Part 1 Solution
	with open("day13_input", "r") as infile:
		row_idx = 0
		for line in infile.readlines():
			map.append(list(line))
			for i in range(len(map[row_idx])):
				if map[row_idx][i] == "^" or map[row_idx][i] == "v":
					carts.append(Cart(i,row_idx,map[row_idx][i]))
					map[row_idx][i] = "|"
				if map[row_idx][i] == "<" or map[row_idx][i] == ">":
					carts.append(Cart(i,row_idx,map[row_idx][i]))
					map[row_idx][i] = "-"
			row_idx += 1
	
	crashed = False
	while not crashed:
		#display_map()
		carts = sorted(carts, key=lambda a: (a.y,a.x))
		for cart in carts:
			if not cart.move():
				print str(cart.x) + ", " + str(cart.y)
				crashed = True
				break
		if not crashed:
			for i in range(len(carts)):
				for j in range(i+1, len(carts)):
					if carts[i].x == carts[j].x and carts[i].y == carts[j].y:
						print str(carts[i].x) + ", " + str(carts[i].y)
						crashed = True
						break


	# Part 2 Solution
	map = []
	carts = []
	with open("day13_input", "r") as infile:
		row_idx = 0
		for line in infile.readlines():
			map.append(list(line))
			for i in range(len(map[row_idx])):
				if map[row_idx][i] == "^" or map[row_idx][i] == "v":
					carts.append(Cart(i,row_idx,map[row_idx][i]))
					map[row_idx][i] = "|"
				if map[row_idx][i] == "<" or map[row_idx][i] == ">":
					carts.append(Cart(i,row_idx,map[row_idx][i]))
					map[row_idx][i] = "-"
			row_idx += 1
	
	
	while True:
		#display_map()
		if len(carts) == 1:
			print str(carts[0].x) + "," + str(carts[0].y)
			break
		carts = sorted(carts, key=lambda a: (a.y,a.x))
		for cart in carts:
			if not cart.rmv:
				cart.rm_move()
		for cart in carts:
			if cart.rmv:
				carts.remove(cart)
		if len(carts) == 1:
			print str(carts[0].x) + "," + str(carts[0].y)
			break
		for i in range(len(carts)):
			for j in range(i+1,len(carts)):
					if carts[i].x == carts[j].x and carts[i].y == carts[j].y:
						carts[i].rmv = True
						carts[j].rmv = True
		for cart in carts:
			if cart.rmv:
				carts.remove(cart)			
			
			
		

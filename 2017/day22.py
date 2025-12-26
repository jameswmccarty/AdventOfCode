#!/usr/bin/python


infected = set()
weak = set()
flagged = set()

class Carrier:

	# Directions
	# 0 - Up   ( y -= 1 )
	# 1 - Down ( y += 1 )
	# 2 - Left ( x -= 1 )
	# 3 - Right( x += 1 )

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.dir = 0
		self.infections = 0
		
	def move(self): # Part 1 Mover
		# if current node is infected
		if (self.x, self.y) in infected:
			# Turn Right
			if self.dir == 0:
				self.dir = 3
			elif self.dir == 1:
				self.dir = 2
			elif self.dir == 3:
				self.dir = 1
			elif self.dir == 2:
				self.dir = 0
			# Clean the Node
			infected.remove((self.x, self.y))
		else:
			# Turn Left
			if self.dir == 0:
				self.dir = 2
			elif self.dir == 1:
				self.dir = 3
			elif self.dir == 3:
				self.dir = 0
			elif self.dir == 2:
				self.dir = 1
			# Infect the Node
			infected.add((self.x, self.y))
			self.infections += 1
		# Move forward
		if self.dir == 0:
			self.y -= 1
		elif self.dir == 1:
			self.y += 1
		elif self.dir == 3:
			self.x += 1
		elif self.dir == 2:
			self.x -= 1

	def adv_move(self): # Part 2 Mover
		# If currnt is clean
		if (self.x, self.y) not in weak and (self.x, self.y) not in flagged and (self.x, self.y) not in infected:
			# Turn Left
			if self.dir == 0:
				self.dir = 2
			elif self.dir == 1:
				self.dir = 3
			elif self.dir == 3:
				self.dir = 0
			elif self.dir == 2:
				self.dir = 1
			# Weaken the Node
			weak.add((self.x, self.y))
		# no direction change for Weakened
		elif (self.x, self.y) in weak:
			infected.add((self.x, self.y))
			weak.remove((self.x, self.y))
			self.infections += 1
		# if current node is infected
		elif (self.x, self.y) in infected:
			# Turn Right
			if self.dir == 0:
				self.dir = 3
			elif self.dir == 1:
				self.dir = 2
			elif self.dir == 3:
				self.dir = 1
			elif self.dir == 2:
				self.dir = 0
			# Flag the Node
			flagged.add((self.x, self.y))
			infected.remove((self.x, self.y))
		# Reverse if flagged node
		elif (self.x, self.y) in flagged:
			if self.dir == 0:
				self.dir = 1
			elif self.dir == 1:
				self.dir = 0
			elif self.dir == 3:
				self.dir = 2
			elif self.dir == 2:
				self.dir = 3
			# clean the node
			flagged.remove((self.x, self.y))		

		# Move forward
		if self.dir == 0:
			self.y -= 1
		elif self.dir == 1:
			self.y += 1
		elif self.dir == 3:
			self.x += 1
		elif self.dir == 2:
			self.x -= 1
			
if __name__ == "__main__":

	# Part 1 Solution

	row_width = 0
	row_idx = 0
	with open("day22_input", "r") as infile:
		for line in infile.readlines():
			for x, char in enumerate(line.strip()):
				if char == "#":
					infected.add((x,row_idx))
			row_idx += 1
			row_width = len(line)
	
	mover = Carrier(row_width / 2, row_idx / 2) # map center
	
	for i in range(10000):
		mover.move()
	print mover.infections
	
	# Part 2 Solution
	
	infected = set() # Reset
	
	row_width = 0
	row_idx = 0
	with open("day22_input", "r") as infile:
		for line in infile.readlines():
			for x, char in enumerate(line.strip()):
				if char == "#":
					infected.add((x,row_idx))
			row_idx += 1
			row_width = len(line)
	
	mover = Carrier(row_width / 2, row_idx / 2) # map center
	
	for i in range(10000000):
		mover.adv_move()
	print mover.infections
	


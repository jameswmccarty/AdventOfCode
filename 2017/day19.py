#!/usr/bin/python

map = []
letters = [chr(i) for i in range(65,91)] # Upper ASCII
path = []

class Packet:

	# Directions
	"""
		0 - Up
		1 - Down
		2 - Left
		3 - Right
	"""

	def __init__(self, x, y):
		self.x = x 
		self.y = y 
		self.dir = 1 # Down by default on both Example and Problem Input
		self.steps = 0
		
	def move(self):
	
		# Go to next spot on the map
		if self.dir == 0:
			self.y -= 1
		elif self.dir == 1:
			self.y += 1
		elif self.dir == 2:
			self.x -= 1
		elif self.dir == 3:
			self.x += 1
	
		# if we moved out of bounds, terminate movement
		if self.y < 0 or self.y > len(map):
			return False
		if self.x < 0 or self.x > len(map[self.y]):
			return False
	
		# see what character is on the map
		mapchar = map[self.y][self.x]
		
		if mapchar == " ": # ran off the track
			return False
	
		if mapchar in letters: # passing a Letter
			path.append(mapchar)
		#elif mapchar == "|" or mapchar == "-":
			# continue same direction
		elif mapchar == "+": # turn
			if self.dir == 0 or self.dir == 1: # if moving up or down
				# check left and right for more track, or a letter.  
				if self.x > 0 and map[self.y][self.x-1] in letters or map[self.y][self.x-1] == "-":
					self.dir = 2
				elif self.x < len(map[self.y]) and map[self.y][self.x+1] in letters or map[self.y][self.x+1] == "-":
					self.dir = 3
			else: # were moving left to right or right to left
				# check above or below for more track, or a letter
				if self.y > 0 and map[self.y-1][self.x] in letters or map[self.y-1][self.x] == "|":
					self.dir = 0
				elif self.y < len(map) and map[self.y+1][self.x] in letters or map[self.y+1][self.x] == "|":
					self.dir = 1

		# Completed movement
		self.steps += 1
		return True
		

if __name__ == "__main__":

	# Part 1 Solution
	
	pkt = None

	with open("day19_input", "r") as infile:
		for line in infile.readlines():
			map.append(list(line))
	
	# Get initial cart position
	
	for i in range(len(map[0])):
		if map[0][i] == "|":
			pkt = Packet(i,0)
			break
	
	while pkt.move():
		continue
	print ''.join(path)
	print pkt.steps+1 # include final step
	
			

			
	

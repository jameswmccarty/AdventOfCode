#!/usr/bin/python


grid = []

class Block:

	def __init__(self, x, y):
		self.visited = False
		self.x = x
		self.y = y
	
	def explore(self, seen):
		if self.visited == True:
			return seen
		seen.add(self)
		self.visited = True
		if self.x > 0:
			if grid[self.y][self.x - 1] != None and not grid[self.y][self.x - 1].visited:
				seen = seen.union(grid[self.y][self.x - 1].explore(seen))
		if self.x < len(grid[self.y])-1:
			if grid[self.y][self.x + 1] != None and not grid[self.y][self.x + 1].visited:
				seen = seen.union(grid[self.y][self.x + 1].explore(seen))
		if self.y > 0:
			if grid[self.y-1][self.x] != None and not grid[self.y-1][self.x].visited:
				seen = seen.union(grid[self.y-1][self.x].explore(seen))
		if self.y < len(grid)-1:
			if grid[self.y+1][self.x] != None and not grid[self.y+1][self.x].visited:
				seen = seen.union(grid[self.y+1][self.x].explore(seen))
		return seen		

hex_bits = { 	'0' : 0,
				'1' : 1,
				'2' : 1,
				'3' : 2,
				'4' : 1,
				'5' : 2,
				'6' : 2,
				'7' : 3,
				'8' : 1,
				'9' : 2,
				'a' : 2,
				'b' : 3,
				'c' : 2,
				'd' : 3,
				'e' : 3,
				'f' : 4}

hex_val = { 	'0' : 0,
				'1' : 1,
				'2' : 2,
				'3' : 3,
				'4' : 4,
				'5' : 5,
				'6' : 6,
				'7' : 7,
				'8' : 8,
				'9' : 9,
				'a' : 10,
				'b' : 11,
				'c' : 12,
				'd' : 13,
				'e' : 14,
				'f' : 15}
				
def knot_hash(val):
	list = []
	for i in range(256):
		list.append(i)
	pos = 0
	skip = 0	
	lengths = []
	input = val
	suffix = [17, 31, 73, 47, 23]
	for char in input:
		lengths.append(ord(char))
	for val in suffix:
		lengths.append(val)	
	for round in range(64):
		for length in lengths:
			sublist = []
			for i in range(length):
				sublist.append(list[(pos+i)%len(list)])
			sublist.reverse()
			for i in range(length):
				list[(pos+i)%len(list)] = sublist[i]		
			pos += length + skip
			pos %= len(list)
			skip += 1
	hash = ''
	for i in range(16):
		char = 0
		for z in range(16):
			char ^= list[i*16 + z]
		hash += '%02x' % char	
	return hash
	
def hash_gen(val):
	tot = 0
	for i in range(128):
		tot += hash_sum(val + "-" + str(i))
	return tot
	
def hash_sum(val):
	return sum(hex_bits[x] for x in knot_hash(val))
	
def print_grid():
	for row in grid:
		line = ''
		for item in row:
			if item != None:
				line += "#"
			else:
				line += "."
		print line

def populate_grid(val):
	for i in range(128):
		row = [None] * 128
		hash = knot_hash(val + "-" + str(i))
		for j in range(len(hash)):
			for k in range(3,-1,-1):
				if (1<<k) & hex_val[hash[j]] != 0:
					row[j*4 + (3-k)] = Block(j*4 + (3-k),i)
		grid.append(row)

if __name__ == "__main__":

	# Part 1 Solution
	print hash_gen("jzgqcdpd")
	#print hash_gen("flqrgnkx")
	
	# Part 2 Solution
	blocks = []
	populate_grid("jzgqcdpd")
	#print_grid()
	for i in range(128):
		for j in range(128):
			if grid[j][i] != None and not grid[j][i].visited:
				blocks.append(grid[j][i].explore(set()))
	print len(blocks)

#!/usr/bin/python


rocks = set()
sands = set()
max_depth = None

class sand:

	def __init__(self,x,y):
		self.x = x
		self.y = y

	# try to move this grain
	# if we are out of bounds, return -1
	# if we moved, return 0
	# if we are blocked, return 1
	def move(self,p2=False):
		# out of bounds
		if not p2 and self.y > max_depth:
			return -1
		if p2 and self.y == max_depth-1:
			sands.add((self.x,self.y))
			return 1
		# check down one step
		if (self.x,self.y+1) not in rocks and (self.x,self.y+1) not in sands:
			self.y += 1
			return 0
		# something was blocking us
		# try down and left
		if (self.x-1,self.y+1) not in rocks and (self.x-1,self.y+1) not in sands:
			self.x -= 1
			self.y += 1
			return 0
		# try down and right
		if (self.x+1,self.y+1) not in rocks and (self.x+1,self.y+1) not in sands:
			self.x += 1
			self.y += 1
			return 0
		# we are fully stopped.  add self to sand
		sands.add((self.x,self.y))
		return 1


def parse_line(line):
	global rocks
	points = line.split(' -> ')
	start = points.pop(0)
	x0,y0 = start.split(',')
	x0,y0 = int(x0),int(y0)
	while len(points) > 0:
		next = points.pop(0)
		x1,y1 = next.split(',')
		x1,y1 = int(x1),int(y1)
		if x0 == x1: # y direction changes
			if y0 > y1:
				delta = -1
			else:
				delta = 1
			for y in range(y0,y1+delta,delta):
				rocks.add((x0,y))
		else: # x direction changes
			if x0 > x1:
				delta = -1
			else:
				delta = 1
			for x in range(x0,x1+delta,delta):
				rocks.add((x,y0))
		x0,y0 = x1,y1

def pretty_print():
	min_x = min(min([ x[0] for x in sands ]), min([ x[0] for x in rocks ]))-1
	max_x = max(max([ x[0] for x in sands ]), max([ x[0] for x in rocks ]))+1
	min_y = min(min([ x[1] for x in sands ]), min([ x[1] for x in rocks ]))-1
	max_y = max(max([ x[1] for x in sands ]), max([ x[1] for x in rocks ]))+1
	max_x -= min_x
	max_y -= min_y
	for j in range(max_y):
		for i in range(max_x):
			if (i+min_x,j+min_y) in rocks:
				print('#',end='')
			elif (i+min_x,j+min_y) in sands:
				print('o',end='')
			else:
				print('.',end='')
		print()

if __name__ == "__main__":

	# Part 1 Solution
	with open('day14_input','r') as infile:
		for line in infile.readlines():
			parse_line(line.strip())
	made_sand = 0
	max_depth = max([ x[1] for x in rocks ])
	while True:
		grain = sand(500,0)
		status = grain.move()
		while status == 0:
			status = grain.move()
		if status == -1:
			break
		made_sand += 1
	print(made_sand)

	# Part 2 Solution
	max_depth += 2
	while True:
		grain = sand(500,0)
		status = grain.move(p2=True)
		while status == 0:
			status = grain.move(p2=True)
		if status == 1 and grain.x==500 and grain.y==0:
			break
		made_sand += 1
	print(made_sand+1)
	#pretty_print()


#!/usr/bin/python



seen_posits = set((0,0))
intersections = set()
timings = dict()

def taxi(coord):
	return abs(coord[0])+abs(coord[1])

def populate(path):
	x = 0
	y = 0
	for step in path:
		way, val = step[0], int(step[1:])
		for i in range(val):
			if way == 'U':
				y += 1
			elif way == 'D':
				y -= 1
			elif way == 'L':
				x -= 1
			elif way == 'R':
				x += 1
			seen_posits.add((x,y))

def trace(path):
	x = 0
	y = 0
	for step in path:
		way, val = step[0], int(step[1:])
		for i in range(val):
			if way == 'U':
				y += 1
			elif way == 'D':
				y -= 1
			elif way == 'L':
				x -= 1
			elif way == 'R':
				x += 1
			if (x,y) in seen_posits:
				intersections.add((x,y))

def delay(path, wire):
	x = 0
	y = 0
	time = 0
	for step in path:
		way, val = step[0], int(step[1:])
		for i in range(val):
			if way == 'U':
				y += 1
			elif way == 'D':
				y -= 1
			elif way == 'L':
				x -= 1
			elif way == 'R':
				x += 1
			time += 1
			if (x,y) in intersections:
				if time < timings[(x,y)][wire]:
					u,v = timings[(x,y)]
					if wire == 0:
						u = time
					else:
						v = time
					timings[(x,y)] = (u,v)

if __name__ == "__main__":
	
	# Part 1 Solution
	with open("day03_input", 'r') as infile:
		populate(infile.readline().strip().split(','))
		trace(infile.readline().strip().split(','))
	print(min([ taxi(x) for x in intersections ]))
	
	# Part 2 Solution
	for posit in intersections:
		timings[posit] = (float('inf'), float('inf'))
	with open("day03_input", 'r') as infile:
		delay(infile.readline().strip().split(','),0)
		delay(infile.readline().strip().split(','),1)
	print(min([ taxi(x) for x in timings.values() ]))



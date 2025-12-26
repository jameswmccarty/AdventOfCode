#!/usr/bin/python

from collections import deque

def print_shape(pts):
	for y in range(min(pt[1] for pt in pts),max(pt[1] for pt in pts)+1):
		for x in range(min(pt[0] for pt in pts),max(pt[0] for pt in pts)+1):
			if (x,y) in pts:
				print('#',end='')
			else:
				print('.',end='')
		print()

def count_shape(pts):
	total = 0
	for y in range(min(pt[1] for pt in pts),max(pt[1] for pt in pts)+1):
		xs = sorted({ pt[0] for pt in pts if pt[1] == y })
		print(xs)
		while len(xs) > 1:
			total += xs[1] - xs[0]
			xs.pop(0)
			xs.pop(0)
	return total

def cross(a,b):
	return a[0]*b[1] - a[1]*b[0]

def shoelace(pts):
	values = pts[:]
	total = 0
	while len(values) > 1:
		total += cross(values[0],values[1])
		values.pop(0)
	return total//2

def build_shape(instructions):
	deltas = {	'D' : (0,1),
				'L' : (-1,0),
				'R' : (1,0),
				'U' : (0,-1) }
	shape = list()
	pos = (0,0)
	shape.append(pos)
	for d,l,c in instructions:
		for i in range(int(l)+1):
			nx,ny = pos[0]+deltas[d][0]*i,pos[1]+deltas[d][1]*i
			shape.append((nx,ny))
		pos = (nx,ny)
	return shape

def build_shape2(instructions):
	deltas = {	'1' : (0,1),
				'2' : (-1,0),
				'0' : (1,0),
				'3' : (0,-1) }
	shape = list()
	pos = (0,0)
	shape.append(pos)
	per = 0
	for d,t,c in instructions:
		l = int(c[2:-2],16)
		per += l
		d = c[-2]
		nx,ny = pos[0]+deltas[d][0]*int(l),pos[1]+deltas[d][1]*int(l)
		shape.append((nx,ny))
		pos = (nx,ny)
	return shoelace(shape)+per//2 + 1


if __name__ == "__main__":

	# Part 1 Solution
	with open("day18_input", "r") as infile:
		instructions = [ x.split() for x in infile.read().strip().split('\n') ]
	shape = build_shape(instructions)
	shape = set(shape)
	pt = (1,1)
	q = deque()
	q.append(pt)
	shape.add(pt)
	while q:
		pt = q.popleft()
		x,y = pt
		for dx,dy in ((0,1),(1,0),(-1,0),(0,-1)):
			if (x+dx,y+dy) not in shape:
				shape.add((x+dx,y+dy))
				q.append((x+dx,y+dy))

	print(len(shape))


	# Part 2 Solution

	with open("day18_input", "r") as infile:
		instructions = [ x.split() for x in infile.read().strip().split('\n') ]
	print(build_shape2(instructions))

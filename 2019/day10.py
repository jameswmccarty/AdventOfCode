#!/usr/bin/python

import math


asteroids = []

def colinear(a, b, c): # Cross Product (All three form a line)
	return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])

def between(a, b, c): # Dot Product (Does C fall between A and B)
    dot = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1])*(b[1] - a[1])
    if dot < 0:
        return False
    sqlen = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dot > sqlen:
        return False
    return True

def parse_line(row, line):
	for col, char in enumerate(line):
		if char == '#':
			asteroids.append((col, row))

def polar(p):
	theta = (math.atan2(p[1], p[0]) + math.pi / 2.0) % (2.0*math.pi)
	r = math.sqrt(p[0]*p[0]+p[1]*p[1])
	return (theta, r)


if __name__ == "__main__":

	max_count = 0
	best_point = (-1,-1)
	
	# Part 1 Solution
	with open("day10_input", 'r') as infile:
		idx = 0
		for line in infile.readlines():
			parse_line(idx, line.strip())
			idx += 1
	for i in range(len(asteroids)):
		count = 0
		for j in range(len(asteroids)):
			if i != j:
				blocked = False
				for z in range(len(asteroids)):
					if z != i and z != j:
						if colinear(asteroids[i],asteroids[z],asteroids[j]) and between(asteroids[i],asteroids[j],asteroids[z]):
							blocked = True
							break
				if not blocked:
					count += 1
		if count > max_count:
			max_count = count
			best_point = asteroids[i]
	print(max_count)

	# Part 2 Solution
	visible = set()
	for i in range(len(asteroids)):
		if best_point != asteroids[i]:
			blocked = False
			for z in range(len(asteroids)):
				if z != i and asteroids[z] != best_point:
					if colinear(best_point,asteroids[z],asteroids[i]) and between(best_point,asteroids[i],asteroids[z]):
						blocked = True
						break
			if not blocked:
				visible.add(asteroids[i])
	visible = list(visible)
	visible = [ (x[0]-best_point[0], x[1]-best_point[1]) for x in visible ]
	visible = [ (x,polar(x)) for x in visible ]
	visible = sorted(visible, key=lambda vis: vis[1][0])
	visible = [ ((x[0][0]+best_point[0], x[0][1]+best_point[1]), x[1]) for x in visible ]
	print(visible[199][0][0]*100+visible[199][0][1])					
	

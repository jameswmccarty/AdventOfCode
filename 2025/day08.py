#!/usr/bin/python

# Advent of Code 2025 Day 08

import math

def dist(p1, p2):
	x1, y1, z1 = p1
	x2, y2, z2 = p2
	return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

if __name__ == "__main__":

	dists = dict()
	set_map = dict()
	points = []
	with open("day08_input", "r") as infile:
		for line in infile:
			x, y, z = map(int, line.strip().split(','))
			pt = (x, y, z)
			points.append(pt)
			set_map[pt] = { pt }

	for p1 in points:
		for p2 in points:
			if p1 != p2:
				dists[tuple(sorted((p1, p2)))] = dist(p1, p2)

	min_dists = sorted([ (v,k) for k,v in dists.items() ])

	for i in range(1000):
		_, pair = min_dists.pop(0)
		p1, p2 = pair
		a = set_map[p1]
		b = set_map[p2]
		c = a.union(b)
		set_map[p1] = c
		set_map[p2] = c
		for d in c:
			set_map[d] = c

	prod_map = { frozenset(x) for x in set_map.values() }
	sizes = sorted([len(x) for x in prod_map], reverse=True)
	print(math.prod(sizes[0:3]))

	# Reset for part 2

	dists = dict()
	set_map = dict()
	points = []
	with open("day08_input", "r") as infile:
		for line in infile:
			x, y, z = map(int, line.strip().split(','))
			pt = (x, y, z)
			points.append(pt)
			set_map[pt] = { pt }

	all_pts = { pt for pt in set_map.keys() }

	for p1 in points:
		for p2 in points:
			if p1 != p2:
				dists[tuple(sorted((p1, p2)))] = dist(p1, p2)

	min_dists = sorted([ (v,k) for k,v in dists.items() ])

	while True:
		_, pair = min_dists.pop(0)
		p1, p2 = pair
		a = set_map[p1]
		b = set_map[p2]
		c = a.union(b)
		if c == all_pts:
			print(p1[0] * p2[0])
			break
		set_map[p1] = c
		set_map[p2] = c
		for d in c:
			set_map[d] = c



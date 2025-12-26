#!/usr/bin/python

# Advent of Code 2025 Day 09

import math

if __name__ == "__main__":

	pts = set()
	with open("day09_input", "r") as infile:
		for line in infile:
			x, y = map(int, line.strip().split(','))
			pts.add((x,y))
	largest = 0
	for a in pts:
		for b in pts:
			largest = max(largest, abs(a[0]-b[0]+1)*abs(a[1]-b[1]+1))
	print(largest)

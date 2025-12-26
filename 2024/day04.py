#!/usr/bin/python

# Advent of Code 2024 Day 04

if __name__ == "__main__":

	grid = dict()

	# Part 1 Solution
	with open("day04_input", "r") as infile:
		y = 0
		for line in infile:
			for x, char in enumerate(line.strip()):
				if char in "XMAS":
					grid[(x,y)] = char
			max_x = len(line.strip())
			y += 1
	max_y = y
	count = 0
	for y in range(max_y):
		for x in range(max_x):
			for dx,dy in ((0,1),(1,0),(1,1),(1,-1)):
				if all((x+dx*i,y+dy*i) in grid for i in range(4)):
					test = ''.join(grid[(x+dx*i,y+dy*i)] for i in range(4))
					if test == "XMAS" or test[::-1] == "XMAS":
						count += 1
	print(count)

	# Part 2 Solution
	count = 0
	for y in range(max_y):
		for x in range(max_x):
			if all(pt in grid for pt in ((x,y),(x+1,y+1),(x+2,y+2),(x,y+2),(x+2,y))):
				side1 = grid[(x,y)]+grid[(x+1,y+1)]+grid[(x+2,y+2)]
				side2 = grid[(x+2,y)]+grid[(x+1,y+1)]+grid[(x,y+2)]
				if (side1 == "MAS" or side1 == "SAM") and (side2 == "MAS" or side2 == "SAM"):
					count += 1
	print(count) 

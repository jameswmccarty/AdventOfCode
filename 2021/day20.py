#!/usr/bin/python


if __name__ == "__main__":

	lit = set()

	x_min = None
	x_max = None
	y_min = None
	y_max = None
	
	def resolve_px(x,y,t):
		out = 0
		idx = 8
		for j in (-1,0,1):
			for i in (-1,0,1):
				if (x+i,y+j) in lit:
					out |= 1 << idx
				elif t%2 == 1 and  (x+i < x_min or x+i > x_max or y+j < y_min or y+j > y_max):
					out |= 1 << idx
				idx -= 1
		return out

	# Part 1 Solution
	
	with open("day20_input","r") as infile:
		kernel = infile.readline().strip()
		throw  = infile.readline()
		y = 0
		for line in infile.readlines():
			x_max = len(line)
			for x,char in enumerate(line.strip()):
				if char == "#":
					lit.add((x,y))
			y += 1
		x_min = 0
		y_min = 0
		y_max = y		
	
	orig_x_min = x_min # save initial state
	orig_x_max = x_max
	orig_y_min = y_min
	orig_y_max = y_max
	orig_points = lit

	for _ in range(2):
		next_lit = set()
		for y in range(y_min-1,y_max+2):
			for x in range(x_min-1,x_max+2):
				if kernel[resolve_px(x,y,_)] == "#":
					next_lit.add((x,y))
		lit = next_lit
		y_min -= 1
		x_min -= 1
		x_max += 1
		y_max += 1
	print(len(lit))

	# Part 2 Solution

	#reset
	lit = orig_points
	x_min = orig_x_min
	x_max = orig_x_max
	y_min = orig_y_min
	y_max = orig_y_max

	for _ in range(50):
		next_lit = set()
		for y in range(y_min-1,y_max+2):
			for x in range(x_min-1,x_max+2):
				if kernel[resolve_px(x,y,_)] == "#":
					next_lit.add((x,y))
		lit = next_lit
		y_min -= 1
		x_min -= 1
		x_max += 1
		y_max += 1
	print(len(lit))


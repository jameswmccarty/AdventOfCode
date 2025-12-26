#!/usr/bin/python


if __name__ == "__main__":

	grid = []
	for i in range(1000):
		grid.append([False] * 999)
	
	# Part 1 Solution
	with open("day6_input", "r") as infile:
		for line in infile.readlines():
			if "turn on" in line:
				line = line.replace("turn on ", '')
				start, finish = line.split(" through ")
				s_x, s_y = start.split(",")
				f_x, f_y = finish.split(",")
				for x in range(int(s_x),int(f_x)+1):
					for y in range(int(s_y),int(f_y)+1):
						grid[y][x] = True
			elif "turn off" in line:
				line = line.replace("turn off ", '')
				start, finish = line.split(" through ")
				s_x, s_y = start.split(",")
				f_x, f_y = finish.split(",")
				for x in range(int(s_x),int(f_x)+1):
					for y in range(int(s_y),int(f_y)+1):
						grid[y][x] = False
			elif "toggle" in line:
				line = line.replace("toggle ", '')
				start, finish = line.split(" through ")
				s_x, s_y = start.split(",")
				f_x, f_y = finish.split(",")
				for x in range(int(s_x),int(f_x)+1):
					for y in range(int(s_y),int(f_y)+1):
						grid[y][x] ^= True	
	
	print sum(x.count(True) for x in grid)
	
	# Part 2 Solution
	
	grid = []
	for i in range(1000):
		grid.append([0] * 999)
	
	with open("day6_input", "r") as infile:
		for line in infile.readlines():
			if "turn on" in line:
				line = line.replace("turn on ", '')
				start, finish = line.split(" through ")
				s_x, s_y = start.split(",")
				f_x, f_y = finish.split(",")
				for x in range(int(s_x),int(f_x)+1):
					for y in range(int(s_y),int(f_y)+1):
						grid[y][x] += 1
			elif "turn off" in line:
				line = line.replace("turn off ", '')
				start, finish = line.split(" through ")
				s_x, s_y = start.split(",")
				f_x, f_y = finish.split(",")
				for x in range(int(s_x),int(f_x)+1):
					for y in range(int(s_y),int(f_y)+1):
						grid[y][x] = max(0,grid[y][x]-1)
			elif "toggle" in line:
				line = line.replace("toggle ", '')
				start, finish = line.split(" through ")
				s_x, s_y = start.split(",")
				f_x, f_y = finish.split(",")
				for x in range(int(s_x),int(f_x)+1):
					for y in range(int(s_y),int(f_y)+1):
						grid[y][x] += 2
	
	print sum(sum(x) for x in grid)

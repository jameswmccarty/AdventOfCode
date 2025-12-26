#!/usr/bin/python


grid = []
for i in range(6):
	grid.append(['.']*50)
	
def count_on():
	total = 0
	for row in grid:
		total += ''.join(row).count('#')
	return total
	
def print_grid():
	for row in grid:
		print ''.join(row)
	print
	
def parse(line):
	global grid
	if "rect" in line:
		cmd, dim = line.split(" ")
		x, y = dim.split("x") 
		for i in range(int(x)):
			for j in range(int(y)):
				grid[j][i] = '#'
	elif "rotate" in line:
		if "column" in line:
			line = line.replace("rotate column x=", '')
			col, amt = line.split(" by ")
			next_col = ['.'] * len(grid)
			for idx in range(len(next_col)):
				next_col[(idx+int(amt))%len(next_col)] = grid[idx][int(col)]
			for idx in range(len(next_col)):
				grid[idx][int(col)] = next_col[idx]
		elif "row" in line:
			line = line.replace("rotate row y=", '')
			row, amt = line.split(" by ")
			next_row = ['.'] * len(grid[0])
			for idx in range(len(next_row)):
				next_row[(idx+int(amt))%len(next_row)] = grid[int(row)][idx]
			for idx in range(len(next_row)):
				grid[int(row)][idx] = next_row[idx]		
	
if __name__ == "__main__":

	# Part 1 and 2 Solution
	with open("day8_input", "r") as infile:
		for line in infile.readlines():
			parse(line.strip())
			#print_grid()
	print count_on()
	print_grid()
	
	

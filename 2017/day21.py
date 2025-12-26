#!/usr/bin/python

grid = [] # main map
t_grid = [] # swap space

# mirror input
def flip(pattern):
	out = []
	for row in pattern:
		row.reverse()
		out.append(row)
	return out
	
# rotate a matrix 
def rotate(pattern):
	out = []
	for i in range(len(pattern)):
		out.append([None] * len(pattern[0]))
	for i,row in enumerate(pattern):
		for j, c in enumerate(row):
			out[j][i] = c
	return out
	
def str_to_grid(string):
	return [ list(x) for x in string.split("/") ]
	
def grid_to_str(grid):
	out = ''
	for i,row in enumerate(grid):
		out += ''.join(row)
		if i < len(grid)-1:
			out += "/"
	return out
	
# return a sub-section at location x,y with size w*w
def grid_sample(x, y, w):
	out = []
	for i in range(w):
		out.append(grid[y+i][x:x+w])
	return out

def gen_rules(inpt, outpt):
	transforms = set()
	transforms.add(inpt)
	inpt = str_to_grid(inpt)
	transforms.add(grid_to_str(flip(inpt)))
	for i in range(3):
		inpt = rotate(inpt)
		transforms.add(grid_to_str(inpt))
		transforms.add(grid_to_str(flip(inpt)))
	inpt = flip(inpt)
	transforms.add(grid_to_str(inpt))
	return (transforms, outpt)
	
# number of "#" in the grid
def count_on():
	count = 0
	for row in grid:
		count += row.count("#")
	return count
		
def print_grid():
	for row in grid:
		print ''.join(row)


# wipe the temporary grid, enlarge for next gen
def t_grid_init(w):
	global t_grid
	t_grid = []
	next_len = len(grid) / w 
	for i in range(next_len * (w+1)):
		t_grid.append( [ None ] * next_len * (w+1) )
		
def t_grid_pop(x,y,w,subgrid):
	for j,row in enumerate(subgrid):
		for k,char in enumerate(row):
			t_grid[y*(w+1)+j][x*(w+1)+k] = char
		
if __name__ == "__main__":

	rules = []

	with open("day21_input", "r") as infile:
		for line in infile.readlines():
			inpt, outpt = line.split(" => ")
			rules.append(gen_rules(inpt.strip(), outpt.strip()))
	
	# Default Pattern
	grid = []
	grid.append(list('.#.'))
	grid.append(list('..#'))
	grid.append(list('###'))
	
	# Part 1 and 2 Solution

	max_gens = 18
	
	for _ in range(max_gens):
		if len(grid) % 2 == 0: # 2x2 squares
			w = 2
		elif len(grid) % 3 == 0: # 3x3 squares
			w = 3
		else:
			print "Unexpected grid size."
			exit()
		t_grid_init(w) # fill in next generation
		for i in range(0,len(grid),w):
			for j in range(0,len(grid),w):
				samp = grid_to_str(grid_sample(i,j,w))
				o = None
				for rule in rules:
					if samp in rule[0]:
						o = rule[1]
				if o == None:
					print "Unable to match for input: ", samp
					print rules
					exit()
				else:
					t_grid_pop(i/w,j/w,w,str_to_grid(o))
		grid = t_grid[:] # copy buffer
		if _ == 4: # Part 1
			print count_on()
	print count_on()
				
		

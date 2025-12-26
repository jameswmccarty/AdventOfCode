#!/usr/bin/python


flowed = set() # water has passed through
filled = set() # settled water
clay = set() # boundaries

MAX_X = 0
MAX_Y = 0

def print_map():
	for row_idx in range(MAX_Y):
		out = list('.' * MAX_X)
		for loc in clay:
			if loc[1] == row_idx:
				out[loc[0]] = '#'
		for loc in flowed:
			if loc[1] == row_idx:
				out[loc[0]]= '|'
		for loc in filled:
			if loc[1] == row_idx:
				out[loc[0]] = '~'
		print ''.join(out)
	print
	
def write_map(n):
	with open("map_out." + str(n) + ".txt", "w") as outfile:
		for row_idx in range(MAX_Y):
			out = list('.' * MAX_X)
			for loc in clay:
				if loc[1] == row_idx:
					out[loc[0]] = '#'
			for loc in flowed:
				if loc[1] == row_idx:
					out[loc[0]]= '|'
			for loc in filled:
				if loc[1] == row_idx:
					out[loc[0]] = '~'
			outfile.write(''.join(out))
			outfile.write('\n')
		outfile.close()

def count_water(y_min, y_threshold):
	count = 0
	for item in flowed:
		if item[1] < y_threshold and item[1] >= y_min:
			count += 1
	return count
	
def count_filled(y_min, y_threshold):
	count = 0
	for item in filled:
		if item[1] < y_threshold and item[1] >= y_min:
			count += 1
	return count

def flow(loc):

	global filled
	global flowed

	path = []
	path.append(loc)
	flowed.add(loc)
	
	#print len(flowed), len(filled)
	
	x,y = loc
	x0 = x
	ldrain = False
	rdrain = False
	
	while (x,y+1) not in filled and (x,y+1) not in clay and (x, y+1) not in flowed and y < MAX_Y:
		y += 1
		flowed.add((x,y))
		path.append((x,y))
		
	if y >= MAX_Y:
		return True
	if (x,y+1) in flowed and (x,y+1) not in filled:
		return True

	# reached bottom or blocked
	
	while len(path) > 0 and not (ldrain or rdrain):
	
		# so go left and see if there is a drop
		lseen = set()
		while x > 0 and (x-1, y) not in clay and not ldrain and (x-1,y) not in filled:
			x -= 1
			flowed.add((x,y))
			lseen.add((x,y))
			if y < MAX_Y and (x,y+1) not in clay and (x,y+1) not in filled: # found drop off
				ldrain |= flow((x,y))
				if ldrain:
					break
					
		# then go right for orignal drop down poinmt
		x = x0
		rseen = set()
		while x < MAX_X and (x+1,y) not in clay and not rdrain and (x+1,y) not in filled:
			x += 1
			flowed.add((x,y))
			rseen.add((x,y))
			if y < MAX_Y and (x,y+1) not in clay and (x,y+1) not in filled: # found drop off
				rdrain |= flow((x,y))
				if rdrain:
					break

		if not ldrain and not rdrain:
			filled = filled.union(rseen, lseen)
			filled.add((x0,y))
				
		#print path
		if len(path) > 0 and not rdrain and not ldrain:
			x,y = path.pop()
			x0 = x
			
		if len(path) == 0 and not rdrain and not ldrain:
			return False
		
	return ldrain|rdrain
	
if __name__ == "__main__":

	# Part 1 and 2 Solution

	# Determine X/Y boundaries for map
	fname = "day17_input"
	source_x = 500 # default source location	
	min_x = 1000
	min_y = 1000
	max_x = 0
	max_y = 0
	with open(fname, "r") as infile:
		for line in infile.readlines():
			y_line = line[:]
			idx = line.index("x=")
			line = line[idx:]
			if "," in line: # x listed before y
				line = line.split(",")[0]
				line = line.replace("x=",'')
				min_x = min(min_x, int(line))
				max_x = max(max_x, int(line))
			else: # x gives a range
				line = line.replace("x=",'')
				line = line.split("..")
				min_x = min(min_x, int(line[0]))
				max_x = max(max_x, int(line[1]))
				
			idx = y_line.index("y=")
			y_line = y_line[idx:]
			if "," in y_line: # y listed before x
				y_line = y_line.split(",")[0]
				y_line = y_line.replace("y=",'')
				max_y = max(max_y, int(y_line))
				min_y = min(min_y, int(y_line))
			else: # y gives a range
				y_line = y_line.replace("y=",'')
				y_line = y_line.split("..")
				max_y = max(max_y, int(y_line[1]))
				min_y = min(min_y, int(y_line[0]))
			
	# Provide buffer and set min to 0
	min_x -= 3
	max_x += 3
	source_x -= min_x
	max_x -= min_x
	
	MAX_X = max_x
	
	with open(fname, "r") as infile:
		for line in infile.readlines():
			line = line.split(",")
			if "x=" in line[0]: # x listed before y
				mapx = int(line[0].replace("x=", '').replace(",",''))
				mapx -= min_x
				y_range = line[1].replace("y=", '')
				lo, hi = y_range.split('..')
				for y in range(int(lo),int(hi)+1):
					
					clay.add((mapx,y))
					#map[y][mapx] = "#"
			else: # y listed before x
				mapy = int(line[0].replace("y=", '').replace(",",''))
				x_range = line[1].replace("x=", '')
				lo, hi = x_range.split('..')
				for x in range(int(lo)-min_x,int(hi)-min_x+1):
					# map[mapy][x] = "#"
					clay.add((x,mapy))
	
	MAX_Y = max_y+3
	flow((source_x,0))
	flowed.remove((source_x,0))
	print count_water(min_y,max_y+1)
	print count_filled(min_y,max_y+1)
	write_map(0)

	
	
	
	

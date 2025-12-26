#!/usr/bin/python


if __name__ == "__main__":

	south_map = set()
	east_map  = set()
	
	width = None
	height = None
	
	def move_south():
		global south_map
		move_made = False
		next_south = set()
		for c in south_map:
			x,y = c
			ny = (y+1)%height
			if (x,ny) not in south_map and (x,ny) not in east_map:
				next_south.add((x,ny))
				move_made = True
			else:
				next_south.add((x,y))
		south_map = next_south
		return move_made

	def move_east():
		global east_map
		move_made = False
		next_east= set()
		for c in east_map:
			x,y = c
			nx = (x+1)%width
			if (nx,y) not in south_map and (nx,y) not in east_map:
				next_east.add((nx,y))
				move_made = True
			else:
				next_east.add((x,y))
		east_map = next_east
		return move_made

	# Part 1 Solution
	with open("day25_input","r") as infile:
		y = 0
		for line in infile.readlines():
			width = len(line.strip())
			for x,char in enumerate(line.strip()):
				if char == ">":
					east_map.add((x,y))
				elif char == "v":
					south_map.add((x,y))
			y += 1
		height = y
	step = 1
	
	while True:
		state = False
		state |= move_east()
		state |= move_south()
		if not state:
			print(step)
			exit()
		step += 1


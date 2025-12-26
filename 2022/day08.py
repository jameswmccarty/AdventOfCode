#!/usr/bin/python


if __name__ == "__main__":

	def is_visible(forest,x,y,max_x,max_y):
		north,south,east,west = True,True,True,True
		if (x,y) not in forest:
			return False
		for i in range(x-1,-1,-1):
			if forest[(x,y)] <= forest[(i,y)]:
				west = False
				break
		for i in range(x+1,max_x):
			if forest[(x,y)] <= forest[(i,y)]:
				east = False
				break
		for j in range(y-1,-1,-1):
			if forest[(x,y)] <= forest[(x,j)]:
				north = False
				break
		for j in range(y+1,max_y):
			if forest[(x,y)] <= forest[(x,j)]:
				south = False
				break
		return True in [north,south,east,west]

	def scenic_score(forest,x,y,max_x,max_y):
		north,south,east,west = 0,0,0,0
		if (x,y) not in forest:
			return 0
		for i in range(x-1,-1,-1):
			west += 1
			if forest[(x,y)] <= forest[(i,y)]:
				break
		for i in range(x+1,max_x):
			east += 1
			if forest[(x,y)] <= forest[(i,y)]:
				break
		for j in range(y-1,-1,-1):
			north += 1
			if forest[(x,y)] <= forest[(x,j)]:
				break
		for j in range(y+1,max_y):
			south += 1
			if forest[(x,y)] <= forest[(x,j)]:
				break
		return north*south*east*west

	# Part 1 Solution
	forest = dict()
	max_x, max_y = 0,0
	with open("day08_input","r") as infile:
		j = 0
		for line in infile.readlines():
			max_x = len(line.strip())
			for i,height in enumerate(line.strip()):
				forest[(i,j)] = int(height)
			j += 1
		max_y = j
	visible = 0
	for i in range(1,max_x-1):
		for j in range(1,max_y-1):
			if is_visible(forest,i,j,max_x,max_y):
				visible += 1
	visible += max_x*2
	visible += (max_y-2)*2
	print(visible)

	# Part 2 Solution
	print(max( [ scenic_score(forest,i,j,max_x,max_y) for j in range(1,max_y-1) for i in range(1,max_x-1) ] ))

#!/usr/bin/python


if __name__ == "__main__":

	# 0 - North
	# 1 - East
	# 2 - South
	# 3 - West
	dir_idx = 0
	dirs = [1, 1, -1, -1]
	vert = 0
	horiz = 0

	# Part 1 Solution
	with open("day1_input", "r") as infile:
		directions = infile.read().strip().split(",")
	for step in directions:
		if "R" in step:
			dir_idx += 1
			dir_idx %= 4
			step = int(step.replace("R",''))
		else:
			dir_idx -= 1
			dir_idx %= 4
			step = int(step.replace("L",''))
		if dir_idx % 2 == 0:
			vert += dirs[dir_idx]*step
		else:
			horiz += dirs[dir_idx]*step
	print abs(vert)+abs(horiz)
	
	# Part 2 Solution
	seen = set()
	last = (0,0)
	seen.add(last)
	for step in directions:
		if "R" in step:
			dir_idx += 1
			dir_idx %= 4
			step = int(step.replace("R",''))
		else:
			dir_idx -= 1
			dir_idx %= 4
			step = int(step.replace("L",''))
		if dir_idx % 2 == 0:
			for i in range(step):
				next = (last[0]+dirs[dir_idx], last[1])
				if next in seen:
					print abs(next[0])+abs(next[1])
					exit()
				seen.add(next)
				last = next
		else:
			for i in range(step):
				next = (last[0], last[1]+dirs[dir_idx])
				if next in seen:
					print abs(next[0])+abs(next[1])
					exit()
				seen.add(next)
				last = next

#!/usr/bin/python


if __name__ == "__main__":

	# Part 1 Solution
	
	visited = set()
	pos = (0,0)
	visited.add(pos)
	
	with open("day3_input", "r") as infile:
		path = infile.read().strip()

	for char in path:
		if char == "^":
			pos = (pos[0], pos[1]-1)
		elif char == "v":
			pos = (pos[0], pos[1]+1)
		elif char == "<":
			pos = (pos[0]-1, pos[1])
		elif char == ">":
			pos = (pos[0]+1, pos[1])
		visited.add(pos)
	
	print(len(visited))
	
	# Part 2 Solution
	
	visited = set()
	pos = [(0,0), (0,0)]
	visited.add(pos[0])
	idx = 0

	for char in path:
		p = pos[idx]
		if char == "^":
			p = (p[0], p[1]-1)
		elif char == "v":
			p = (p[0], p[1]+1)
		elif char == "<":
			p = (p[0]-1, p[1])
		elif char == ">":
			p = (p[0]+1, p[1])
		visited.add(p)
		pos[idx] = p
		idx += 1
		idx %= 2
		
	print(len(visited))

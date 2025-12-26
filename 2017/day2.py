#!/usr/bin/python


if __name__ == "__main__":

	#Part 1 Solution
	
	lines = []
	
	with open("day2_input", "r") as infile:
		for line in infile.readlines():
			row = line.strip().split("\t")
			row = [ int(x) for x in row ]
			lines.append(row)
	
	sum = 0
	for line in lines:
		sum += max(line) - min(line)
	
	print sum
	
	#Part 2 solution
	
	sum = 0
	
	for line in lines:
		found = False
		for x in line:
			if found == False:
				for y in line:
					if x % y == 0 and x != y:
						a = max(x,y)
						b = min(x,y)
						sum += (a / b)
						found = True
						break
	print sum
					
	
	
	

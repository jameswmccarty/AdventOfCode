#!/usr/bin/python


if __name__ == "__main__":


	# Part 1 Solution
	with open("day01_input", "r") as infile:
		depths = [ int(x) for x in infile.read().strip().split('\n') ]
	print(sum([ depths[i] > depths[i-1] for i in range(1,len(depths)) ]))

	# Part 2 Solution
	windows = [ sum(depths[i:i+3]) for i in range(len(depths)-2) ]
	print(sum([ windows[i] > windows[i-1] for i in range(1,len(windows)) ]))


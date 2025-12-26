#!/usr/bin/python


if __name__ == "__main__":


	# Part 1 Solution
	with open("day07_input","r") as infile:
		horiz = [ int(x) for x in infile.read().strip().split(',') ]
	cost = float('inf')
	for pos in range(min(horiz),max(horiz)):
		cost = min(cost,sum( [ abs(x-pos) for x in horiz ] ))
	print(cost)

	# Part 2 Solution
	cost = float('inf')
	for pos in range(min(horiz),max(horiz)):
		# sum 1..n === N * (N+1) / 2
		cost = min(cost,sum( [ (abs(x-pos)*(abs(x-pos)+1)//2) for x in horiz ] ))
	print(cost)


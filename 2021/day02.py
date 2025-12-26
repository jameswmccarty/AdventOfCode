#!/usr/bin/python


if __name__ == "__main__":


	# Part 1 Solution

	with open("day02_input","r") as infile:
		orders = infile.read().strip().split('\n')
		orders = [ x.split(' ') for x in orders ]
		orders = [ (x[0],int(x[1])) for x in orders ]
	horiz = 0
	up    = 0
	down  = 0
	for command, unit in orders:
		if command == 'forward':
			horiz += unit
		elif command == 'up':
			up += unit
		elif command == 'down':
			down += unit
	print(horiz * (down-up))


	# Part 2 Solution

	horiz = 0
	aim   = 0
	depth = 0
	for command, unit in orders:
		if command == 'forward':
			horiz += unit
			depth += unit*aim
		elif command == 'up':
			aim -= unit
		elif command == 'down':
			aim += unit
	print(horiz * depth)

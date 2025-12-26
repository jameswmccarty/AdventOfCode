#!/usr/bin/python


import math

def quadradic(a,b,c):
	radical = math.sqrt(b**2 - 4*a*c)
	return (-b+radical)/(2*a),(-b-radical)/(2*a)	


if __name__ == "__main__":

	# Part 1 Solution
	with open("day06_input", "r") as infile:
		times = [ int(x) for x in infile.readline().lstrip("Time:").strip().split() ]
		dists = [ int(x) for x in infile.readline().lstrip("Distance:").strip().split() ]

	wins = []
	while times:
		lo,hi = quadradic(-1,times.pop(0),-dists.pop(0))
		lo_bound = math.ceil(abs(lo))
		hi_bound = math.floor(abs(hi))
		if not ((lo_bound - lo) > 0):
			lo_bound += 1
		if not ((hi - hi_bound) > 0):
			hi_bound -= 1
		wins.append(hi_bound-lo_bound+1)
	print(math.prod(wins))

	# Part 2 Solution
	with open("day06_input", "r") as infile:
		time  = int( ''.join( x for x in infile.readline() if x in '0123456789') )
		dist  = int( ''.join( x for x in infile.readline() if x in '0123456789') )
	lo,hi = quadradic(-1,time,-dist)
	lo_bound = math.ceil(abs(lo))
	hi_bound = math.floor(abs(hi))
	if not ((lo_bound - lo) > 0):
		lo_bound += 1
	if not ((hi - hi_bound) > 0):
		hi_bound -= 1
	print(hi_bound-lo_bound+1)

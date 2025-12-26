#!/usr/bin/python

# Advent of Code 2024 Day 13

def cost_if_winable(config,pt2):
	cost = float('inf')
	config = config.split('\n')
	a1 = int(config[0].split(':')[1].split(',')[0].lstrip(' X+'))
	a2 = int(config[0].split(':')[1].split(',')[1].lstrip(' Y+'))
	b1 = int(config[1].split(':')[1].split(',')[0].lstrip(' X+'))
	b2 = int(config[1].split(':')[1].split(',')[1].lstrip(' Y+'))
	c1 = int(config[2].split(':')[1].split(',')[0].lstrip(' X='))
	c2 = int(config[2].split(':')[1].split(',')[1].lstrip(' Y='))
	if pt2:
		c1 += 10000000000000
		c2 += 10000000000000
	x0 = -((b1*c2 - b2*c1) / (a1*b2 - a2*b1))
	y0 = -((c1*a2 - c2*a1) / (a1*b2 - a2*b1))
	if x0.is_integer() and y0.is_integer():
		return int(3*x0 + y0)
	return 0

if __name__ == "__main__":


	# Part 1 Solution
	with open("day13_input", "r") as infile:
		configs = infile.read().strip().split('\n\n')
	print(sum(cost_if_winable(c, False) for c in configs))

	# Part 2 Solution
	print(sum(cost_if_winable(c, True) for c in configs))

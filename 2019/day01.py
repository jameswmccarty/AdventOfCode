#!/usr/bin/python

def counter_up(mass):
	mass = int(mass) // 3
	return mass - 2

def counter_up_fuel(mass):
	total = 0
	mass = int(mass)
	while counter_up(mass) >= 0:
		mass = counter_up(mass)		
		total += mass
	return total

if __name__ == "__main__":
	
	# Tests
	"""
	print(counter_up(12)) # answer 2
	print(counter_up(14)) # answer 2
	print(counter_up(1969)) # answer 654
	print(counter_up(100756)) # answer 33583
	"""

	# Part 1 Solution
	with open("day01_input", 'r') as infile:
		print(sum(counter_up(f) for f in infile.readlines()))

	# Tests
	"""	
	print(counter_up_fuel(100756))
	"""
	# Part 2 Solution
	with open("day01_input", 'r') as infile:
		print(sum(counter_up_fuel(f) for f in infile.readlines()))

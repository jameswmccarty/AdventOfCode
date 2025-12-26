#!/usr/bin/python

# Advent of Code 2024 Day 02

def safe(line):
	deltas = [ line[i+1]-line[i] for i in range(0,len(line)-1) ]
	if 0 in deltas or any(abs(x) > 3 for x in deltas):
		return False
	if all( x > 0 for x in deltas) or all( x < 0 for x in deltas): 
		return True
	return False

if __name__ == "__main__":

	# Part 1 Solution
	count = 0
	with open("day02_input", "r") as infile:
		for line in infile:
			line = [ int(x) for x in line.split() ]
			if safe(line):
				count += 1
	print(count)

	# Part 2 Solution
	count = 0
	with open("day02_input", "r") as infile:
		for line in infile:
			is_safe = False
			line = [ int(x) for x in line.split() ]
			for i in range(len(line)):
				new_line = line[:]
				new_line.pop(i)
				if safe(new_line):
					is_safe = True
			if is_safe:
				count += 1
	print(count)

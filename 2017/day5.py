#!/usr/bin/python

if __name__ == "__main__":

	#Part 1 Solution

	steps = 0
	idx = 0
	input = []
	with open("day5_input", "r") as infile:
		for line in infile.readlines():
			input.append(int(line.strip()))
	while idx > -1 and idx < len(input):
		offset = input[idx]
		input[idx] += 1
		steps += 1
		idx += offset
	print steps

	#Part 2 Solution

	steps = 0
	idx = 0
	input = []
	with open("day5_input", "r") as infile:
		for line in infile.readlines():
			input.append(int(line.strip()))
	while idx > -1 and idx < len(input):
		offset = input[idx]
		if offset >= 3:
			input[idx] -= 1
		else:
			input[idx] += 1
		steps += 1
		idx += offset
	print steps
		
	

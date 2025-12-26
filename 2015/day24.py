#!/usr/bin/python

import itertools

def smallest_fill(packages, target_weight):
	i = 2
	found = False
	short_len = float('inf')
	small_QE  = float('inf')
	while not found:
		if i > len(packages):
			break
		for combo in itertools.combinations(packages, i):
			if sum(combo) == target_weight:
				short_len = i
				small_QE = min(small_QE, reduce(lambda x, y: x*y, combo))
				found = True
		i += 1
	return small_QE
		

if __name__ == "__main__":

	# Part 1 Solution
	
	packages = []
	#packages = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
	
	with open("day24_input", "r") as infile:
		for line in infile.readlines():
			packages.append(int(line.strip()))
	
	target_weight = sum(packages) / 3
	packages.sort(reverse = True)
	
	print smallest_fill(packages, target_weight)

	# Part 2 Solution
	target_weight = sum(packages) / 4	
	print smallest_fill(packages, target_weight)
	
	

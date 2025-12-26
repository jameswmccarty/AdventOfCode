#!/usr/bin/python

# Advent of Code 2024 Day 19

patterns = []

def possible(design, avail_patterns = []):
	if len(design) == 0:
		return True
	for pattern in avail_patterns:
		if design.endswith(pattern):
			if possible(design[:-len(pattern)], [ x for x in  avail_patterns if x in design ]):
				return True
	return False

way_counts = dict()

def ways(design, avail_patterns = []):
	global way_counts
	if design in way_counts:
		return way_counts[design]
	if len(design) == 0:
		return 1
	sub_count = 0
	for pattern in avail_patterns:
		if design.startswith(pattern):
			sub_count += ways(design[len(pattern):], [ x for x in  avail_patterns if x in design ])
	way_counts[design] = sub_count
	return sub_count

if __name__ == "__main__":

	# Part 1 Solution
	found = 0
	with open("day19_input", "r") as infile:
		for line in infile:
			if "," in line:
				patterns = {*line.strip().split(", ")}
				patterns = sorted(patterns, key = lambda x:len(x), reverse=True)
			elif len(line.strip()) > 0:
				if possible(line.strip(), [ x for x in patterns if x in line ]):
					found += 1
	print(found)

	# Part 2 Solution
	found_ways = 0
	with open("day19_input", "r") as infile:
		for line in infile:
			if len(line.strip()) > 0 and "," not in line:
				if possible(line.strip(), [ x for x in patterns if x in line ]):
					found_ways += ways(line.strip(), [ x for x in patterns if x in line ])
	print(found_ways)

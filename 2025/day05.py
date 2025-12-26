#!/usr/bin/python

# Advent of Code 2025 Day 05

def consolidate_ranges(ranges):
	next_ranges = sorted(ranges)
	for i in range(len(next_ranges)):
		for j in range(len(next_ranges)):
			if i != j:
				lo, hi = next_ranges[i]
				a, b = next_ranges[j]
				if hi >= a and hi <= b:
					comb = (min(lo, a), b)
					ranges.discard(next_ranges[j])
					ranges.discard(next_ranges[i])
					ranges.add(comb)
					return True, set(ranges)
	return False, set(ranges)

if __name__ == "__main__":

	ranges = set()
	ids = []
	with open("day05_input", "r") as infile:
		for line in infile:
			if '-' in line:
				lo, hi = line.strip().split('-')
				ranges.add((int(lo), int(hi)))
			elif len(line.strip()) > 0:
				ids.append(int(line.strip()))

	count = 0
	for x in ids:
		if any(x >= lo and x <= hi for lo,hi in ranges):
			count += 1
	print(count)

	changed = True
	while changed:
		changed, ranges = consolidate_ranges(ranges)

	print(sum(hi+1-lo for lo, hi in ranges))


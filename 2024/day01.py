#!/usr/bin/python

# Advent of Code 2024 Day 01

if __name__ == "__main__":

	# Part 1 Solution
	l,r = [],[]
	with open("day01_input", "r") as infile:
		for line in infile:
			a,b = line.strip().split("   ")
			l.append(int(a))
			r.append(int(b))
	l.sort()
	r.sort()
	print(sum(abs(l[i]-r[i]) for i in range(len(l))))

	# Part 2 Solution
	print(sum(entry*r.count(entry) for entry in l))

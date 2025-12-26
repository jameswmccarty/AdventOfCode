#!/usr/bin/python


if __name__ == "__main__":

	def fully_contains(line):
		a,b = line.strip().split(',')
		a = a.split('-')
		b = b.split('-')
		if int(a[0]) <= int(b[0]) and int(b[1]) <= int(a[1]):
			return True
		if int(b[0]) <= int(a[0]) and int(a[1]) <= int(b[1]):
			return True
		return False

	def partly_contains(line): # use built-in set intersection
		a,b = line.strip().split(',')
		a = a.split('-')
		b = b.split('-')
		a = set([_ for _ in range(int(a[0]),int(a[1])+1)])
		b = set([_ for _ in range(int(b[0]),int(b[1])+1)])
		if len(a.intersection(b)) > 0:
			return True
		return False
	
	def partly_contains2(line): # check only by end points
		a,b = line.strip().split(',')
		a = a.split('-')
		b = b.split('-')
		if int(a[0]) >= int(b[0]) and int(a[0]) <= int(b[1]):
			return True
		if int(a[1]) >= int(b[0]) and int(a[1]) <= int(b[1]):
			return True
		if int(b[0]) >= int(a[0]) and int(b[0]) <= int(a[1]):
			return True
		if int(b[1]) >= int(a[0]) and int(b[1]) <= int(a[1]):
			return True
		return False		

	# Part 1 Solution
	with open("day04_input", "r") as infile:
		print(sum([fully_contains(line) for line in infile.readlines()]))

	# Part 2 Solution
	with open("day04_input", "r") as infile:
		print(sum([partly_contains2(line) for line in infile.readlines()]))

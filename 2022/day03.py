#!/usr/bin/python

if __name__ == "__main__":

	# return priority value of one or more groups
	def pri(groups):
		shared = set(groups.pop())
		while len(groups) > 0:
			shared = shared.intersection(set(groups.pop())) # find intersection of all groups
		shared = shared.pop()
		if shared.islower():
			return ord(shared)-96
		return ord(shared)-38

	# Part 1 Solution
	with open("day03_input", "r") as infile:
		print(sum( [ pri([line.strip()[0:len(line.strip())//2], line.strip()[len(line.strip())//2:]]) for line in infile.readlines() ] ))

	# Part 2 Solution
	with open("day03_input", "r") as infile:
		rucks = infile.read().split('\n')
	print(sum( [ pri(rucks[i:i+3]) for i in range(0,len(rucks)-1,3) ] ))


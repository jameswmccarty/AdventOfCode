#!/usr/bin/python


def reallocate(array, idx):
	blocks = array[idx]
	array[idx] = 0
	while blocks > 0:
		idx += 1
		array[idx%len(array)] += 1
		blocks -= 1
	return array

if __name__ == "__main__":

	#Part 1 Solution

	steps = 0
	memory = []
	seen = []
	with open("day6_input", "r") as infile:
		memory = infile.read().strip()
	
	memory = memory.split("\t")
	memory = [ int(x) for x in memory ]
	
	while ''.join(str(x) for x in memory) not in seen:
		seen.append(''.join(str(x) for x in memory))
		steps += 1
		memory = reallocate(memory, memory.index(max(memory)))
	
	print steps

	#Part 2 Solution

	print steps - seen.index(''.join(str(x) for x in memory))


#!/usr/bin/python


if __name__ == "__main__":

	# Part 1 Solution

	rules = dict()
	with open("day14_input","r") as infile:
		starting_chain = infile.readline().strip()
		for line in infile.readlines():
			if line.strip() == '':
				continue
			elif " -> " in line:
				rule,insert = line.strip().split(" -> ")
				rules[rule] = rule[0]+insert

	steps = 0
	while steps < 10:
		new_chain = ''
		for idx in range(len(starting_chain)-1):
			new_chain += rules[starting_chain[idx:idx+2]]
		starting_chain = new_chain+starting_chain[-1]
		steps += 1

	elements = { x for x in starting_chain }
	most = max([ starting_chain.count(x) for x in elements ] )
	least = min([ starting_chain.count(x) for x in elements ] )
	print(most-least)

	# Part 2 Solution

	change_list = dict()
	pair_counts = dict()
	histogram = dict()

	with open("day14_input","r") as infile:
		starting_chain = infile.readline().strip()
		for line in infile.readlines():
			if line.strip() == '':
				continue
			elif " -> " in line:
				rule,insert = line.strip().split(" -> ")
				pair_counts[rule] = 0
				change_list[rule] = (rule[0]+insert,insert+rule[1],insert)
				histogram[insert] = 0

	for idx in range(len(starting_chain)-1):
		pair_counts[starting_chain[idx:idx+2]] += 1
	for idx in range(len(starting_chain)):
		histogram[starting_chain[idx]] += 1

	steps = 0
	while steps < 40:
		new_pair_counts = dict()
		for entry in pair_counts:
			new_pair_counts[entry] = 0
		for entry in pair_counts:
			d1,d2,h = change_list[entry]
			new_pair_counts[d1] += pair_counts[entry]
			new_pair_counts[d2] += pair_counts[entry]
			histogram[h] += pair_counts[entry]
		pair_counts = new_pair_counts
		steps += 1
	most = max([ x for x in histogram.values() ] )
	least = min([ x for x in histogram.values() ] )
	print(most-least)



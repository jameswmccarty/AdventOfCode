#!/usr/bin/python

import functools

def hand_compare(a,b):
	a,b = a[0],b[0]
	strength = 'AKQJT98765432'
	a_counts = [ a.count(x) for x in set(a) ]
	b_counts = [ b.count(x) for x in set(b) ]
	max_a = max(a_counts)
	max_b = max(b_counts)
	# 5,4 or 3 of a kind beating a lower type
	if max_a > max_b and max_a >= 2:
		return 1
	if max_b > max_a and max_b >= 2:
		return -1
	# Full houses or 3 of a kind
	if max_a == max_b and max_a == 3:
		if len(a_counts) == 2 and len(b_counts) > 2:
			return 1
		if len(b_counts) == 2 and len(a_counts) > 2:
			return -1
	# Pairs
	if max_a == max_b and max_a == 2:
		if a_counts.count(2) > b_counts.count(2):
			return 1
		if b_counts.count(2) > a_counts.count(2):
			return -1
	# Check high card
	for i in range(len(a)):
		if strength.index(a[i]) < strength.index(b[i]):
			return 1
		if strength.index(b[i]) < strength.index(a[i]):
			return -1
	return 0

def hand_compare2(a,b):
	a,b = a[0],b[0]
	strength = 'AKQT98765432J'
	if 'J' in a:
		best_a_counts = []
		best_max_a = 0
		for char in 'AKQT98765432':
			new_a = a.replace('J',char)
			a_counts = [ new_a.count(x) for x in set(new_a) ]
			max_a = max(a_counts)
			if max_a > best_max_a:
				best_max_a = max_a
				best_a_counts = a_counts[:]
		a_counts = best_a_counts[:]
		max_a    = best_max_a
	elif 'J' not in a:
		a_counts = [ a.count(x) for x in set(a) ]
		max_a = max(a_counts)
	if 'J' in b:
		best_b_counts = []
		best_max_b = 0
		for char in 'AKQT98765432':
			new_b = b.replace('J',char)
			b_counts = [ new_b.count(x) for x in set(new_b) ]
			max_b = max(b_counts)
			if max_b > best_max_b:
				best_max_b = max_b
				best_b_counts = b_counts[:]
		b_counts = best_b_counts[:]
		max_b    = best_max_b
	elif 'J' not in b:
		b_counts = [ b.count(x) for x in set(b) ]
		max_b = max(b_counts)
	# 5,4 or 3 of a kind beating a lower type
	if max_a > max_b and max_a >= 2:
		return 1
	if max_b > max_a and max_b >= 2:
		return -1
	# Full houses or 3 of a kind
	if max_a == max_b and max_a == 3:
		if len(a_counts) == 2 and len(b_counts) > 2:
			return 1
		if len(b_counts) == 2 and len(a_counts) > 2:
			return -1
	# Pairs
	if max_a == max_b and max_a == 2:
		if a_counts.count(2) > b_counts.count(2):
			return 1
		if b_counts.count(2) > a_counts.count(2):
			return -1
	# Check high card
	for i in range(len(a)):
		if strength.index(a[i]) < strength.index(b[i]):
			return 1
		if strength.index(b[i]) < strength.index(a[i]):
			return -1
	return 0

if __name__ == "__main__":

	# Part 1 Solution
	with open("day07_input", "r") as infile:
		cards = [ tuple(line.strip().split()) for line in infile ]
	cards = sorted(cards, key=functools.cmp_to_key(hand_compare))
	print(sum( (i+1)*int(x[1]) for i,x in enumerate(cards) ))

	# Part 2 Solution
	cards = sorted(cards, key=functools.cmp_to_key(hand_compare2))
	print(sum( (i+1)*int(x[1]) for i,x in enumerate(cards) ))

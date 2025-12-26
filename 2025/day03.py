#!/usr/bin/python

# Advent of Code 2025 Day 03

memo = dict()

def max_of_size_at_idx(idx, size, digits):
	global memo
	if (idx, size) in memo:
		return memo[(idx, size)]
	if idx >= len(digits) or (idx + size) > len(digits):
		return ''
	if size == 1:
		memo[(idx, size)] = max(digits[idx], max_of_size_at_idx(idx+1, size, digits))
		return memo[(idx, size)]
	memo[(idx, size)] = max(max_of_size_at_idx(idx+1, size, digits), digits[idx] + max_of_size_at_idx(idx+1, size-1, digits))
	return memo[(idx, size)]

def p1_linemax(digits):
	m = 0
	for i in range(len(digits)-1):
		for j in range(i+1,len(digits)):
			m = max(m, int(digits[i]+digits[j]))
	return m

if __name__ == "__main__":

	p1_total = 0
	p2_total = 0
	with open("day03_input", "r") as infile:
		for line in infile:
			p1_total += p1_linemax(line.strip())
			memo = dict()
			p2_total += int(max_of_size_at_idx(0, 12, line.strip()))
	print(p1_total)
	print(p2_total)



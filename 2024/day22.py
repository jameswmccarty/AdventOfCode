#!/usr/bin/python

# Advent of Code 2024 Day 22

matrix = []
deltas = []

delta_avail_amount = dict()

def rng(seed):
	while True:
		seed = ((seed * 64) ^ seed) % 16777216
		seed = ((seed//32) ^ seed) % 16777216
		seed = ((seed * 2048) ^ seed) % 16777216
		yield seed

if __name__ == "__main__":

	# Part 1 Solution
	total = 0
	with open("day22_input", "r") as infile:
		for line in infile:
			a = rng(int(line.strip()))
			m = [ int(line.strip()) % 10 ]
			for _ in range(2000):
				b = next(a)
				m.append(b%10)
			total += b
			matrix.append(m)
	print(total)


	# Part 2 Solution
	for line in matrix:
		d = [ line[i] - line[i-1] for i in range(1,len(line)) ]
		deltas.append(d)
	y = 0
	for row in deltas:
		seen = set()
		for i in range(len(row)-3):
			delta_run = tuple(row[i:i+4])
			if delta_run not in seen:
				seen.add(delta_run)
				banannas = matrix[y][i+4]
				if delta_run not in delta_avail_amount:
					delta_avail_amount[delta_run] = 0
				delta_avail_amount[delta_run] += banannas
		y += 1
	print(max(v for v in delta_avail_amount.values()))

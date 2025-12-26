#!/usr/bin/python

# Advent of Code 2024 Day 07

def dfs(target, params, acc):
	if acc == target and not params:
		return True
	if acc <= target and params:
		return dfs(target, params[1:], acc+params[0]) | dfs(target, params[1:], acc*params[0])
	return False

def concat_dfs(target, params, acc):
	if acc == target and not params:
		return True
	if acc <= target and params:
		l = str(acc)
		r = str(params[0])
		return concat_dfs(target, params[1:], acc+params[0]) | \
		concat_dfs(target, params[1:], acc*params[0]) | \
		concat_dfs(target, params[1:], int(l+r))
	return False

if __name__ == "__main__":

	# Part 1 Solution
	total = 0
	part2_total = 0
	with open("day07_input", "r") as infile:
		for line in infile:
			target, params = line.strip().split(':')
			params = [*map(int, params.split())]
			target = int(target)
			if dfs(target, params[1:], params[0]):
				total += target
			elif concat_dfs(target, params[1:], params[0]):
				part2_total += target
	print(total)

	# Part 2 Solution
	print(total+part2_total)

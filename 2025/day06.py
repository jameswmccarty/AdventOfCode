#!/usr/bin/python

# Advent of Code 2025 Day 06

import math

if __name__ == "__main__":

	problems = []
	with open("day06_input", "r") as infile:
		for line in infile:
			problems.append(line.strip().split())

	total = 0
	for i in range(len(problems[0])):
		if problems[-1][i] == '+':
			total += sum(int(problems[j][i]) for j in range(len(problems)-1))
		else:
			total += math.prod(int(problems[j][i]) for j in range(len(problems)-1))

	print(total)

	total = 0
	problems = []
	with open("day06_input", "r") as infile:
		problems = infile.read().strip('\n').split('\n')
	i = len(problems[0]) - 1
	nums = []
	op = None
	while i >= 0:
		num = ''
		for j in range(len(problems)):
			num += problems[j][i]
		if num[-1] in "+*":
			op = num[-1]
			num = num[0:-1]
		if num.strip():
			nums.append(int(num))
		if op:
			if op == '+':
				total += sum(nums)
			else:
				total += math.prod(nums)
			op = None
			nums = []
		i -= 1
	print(total)

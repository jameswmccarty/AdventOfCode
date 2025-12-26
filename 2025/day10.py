#!/usr/bin/python

# Advent of Code 2025 Day 10

from collections import deque
from scipy.optimize import linprog
import numpy as np

def press_dfs(goal, buttons):
	lights = (False,) * len(goal)
	seen = { lights }
	q = deque()
	q.append((0, lights))
	while q:
		steps, status = q.popleft()
		if status == goal:
			return steps
		for press in buttons:
			new_state = list(status)
			for pos in press:
				new_state[pos] ^= True
			new_state = tuple(new_state)
			if new_state not in seen:
				seen.add(new_state)
				q.append((steps+1, new_state))
	return float('inf')

def p1_min(line):
	line = line.strip().split()
	lights = []
	for idx, char in enumerate(line[0]):
		if char == '#':
			lights.append(True)
		else:
			lights.append(False)
	lights = tuple(lights[1:-1]) # strip brackets
	line.pop(0)
	line.pop(-1)
	buttons = [ eval(x[0:-1]+",)") for x in line ]
	return press_dfs(lights, buttons)

def p2_opt(joltages, buttons):
	a = []
	for i in range(len(joltages)):
		a.append([i in button for button in buttons])
	a = np.array(a)
	b = np.array(joltages)
	c = [1] * len(buttons)
	return linprog(c=c, A_eq=a, b_eq=b, integrality=1).fun

def p2_min(line):
	line = line.strip().split()[1:] # discard lights
	joltages = list(map(int, line[-1][1:-1].split(',')))
	line = line[:-1]
	buttons = [ eval(x[0:-1]+",)") for x in line ]
	return int(p2_opt(joltages, buttons))

if __name__ == "__main__":

	p1 = 0
	p2 = 0
	with open("day10_input", "r") as infile:
		for line in infile:
			p1 += p1_min(line)
			p2 += p2_min(line)
	print(p1)
	print(p2)

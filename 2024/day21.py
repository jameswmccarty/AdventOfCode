#!/usr/bin/python

# Advent of Code 2024 Day 21

import heapq

alpha_pad = ['789','456','123',' 0A']
dir_pad = [' ^A','<v>']
delta = {(0,1):'v',(0,-1):'^',(1,0):'>',(-1,0):'<'}

dir_routes = dict()

memo = dict()

def routes(start_char, end_char, pad):
	for y in range(len(pad)):
		for x in range(len(pad[0])):
			if pad[y][x] == start_char:
				start = (x,y)
			if pad[y][x] == end_char:
				end = (x,y)
	routes = set()
	shortest = float('inf')
	q = [(0,start,{},'')]
	while q:
		steps, loc, seen, path = q.pop(0)
		if loc == end:
			if steps <= shortest:
				shortest = steps
				routes.add(path+'A')
		x, y = loc
		for dx,dy in delta.keys():
			nx, ny = x+dx, y+dy
			if nx >= 0 and nx < len(pad[0]) and ny >= 0 and ny < len(pad):
				if pad[ny][nx] not in seen and pad[ny][nx] != ' ':
					q.append((steps+1,(nx,ny),{*seen,pad[ny][nx]},path+delta[(dx,dy)]))
	return routes

def route_len(seq, depth):
	global memo
	if (seq, depth) in memo:
		return memo[(seq, depth)]
	if depth == 0:
		memo[(seq, depth)] = len(seq)
		return memo[(seq, depth)]
	sub_seqs = [ x+'A' for x in seq.split('A') ][:-1]
	total = 0
	for sub in sub_seqs:
		best = float('inf')
		for trial in next_level('A'+sub):
			best = min(best, route_len(trial, depth - 1))
		total += best 
	memo[(seq, depth)] = total
	return total

for a in '0123456789A':
	for b in '0123456789A':
		dir_routes[a+b] = routes(a,b,alpha_pad)

for a in '<v>^A':
	for b in '<v>^A':
		dir_routes[a+b] = routes(a,b,dir_pad)

def next_level(line):
	routes = {''}
	while len(line) > 1:
		routes = { r+e for e in dir_routes[line[0]+line[1]] for r in routes}
		line = line[1:]
	return routes

if __name__ == "__main__":

	score = 0
	# Part 1 Solution
	with open("day21_input", "r") as infile:
		for line in infile:
			start = 'A'+line.strip()
			routes = {''}
			while len(start) > 1:
				routes = { r+e for e in dir_routes[start[0]+start[1]] for r in routes }
				start = start[1:]
			best = float('inf')
			for entry in routes:
				factor = route_len(entry, 2)
				best = min(best, factor)
			score += int(''.join(x for x in line if x in '0123456789')) * best
	print(score)
	# Part 2 Solution
	with open("day21_input", "r") as infile:
		for line in infile:
			start = 'A'+line.strip()
			routes = {''}
			while len(start) > 1:
				routes = { r+e for e in dir_routes[start[0]+start[1]] for r in routes }
				start = start[1:]
			best = float('inf')
			for entry in routes:
				factor = route_len(entry, 25)
				best = min(best, factor)
			score += int(''.join(x for x in line if x in '0123456789')) * best
	print(score)


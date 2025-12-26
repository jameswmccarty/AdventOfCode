#!/usr/bin/python

from collections import deque
from math import lcm

nodes = dict()
path  = ''

def bfs(start,finish):
	q    = deque()
	q.append((start,0))
	while q:
		pos,step = q.popleft()
		if pos in finish:
			return step
		next_idx  = 1 if path[step%len(path)] == 'R' else 0
		q.append((nodes[pos][next_idx],step+1))

if __name__ == "__main__":

	# Part 1 Solution
	with open("day08_input", "r") as infile:
		path = infile.readline().strip()
		throw = infile.readline()
		for line in infile:
			node,branches = line.split('=')
			l,r = branches.strip().lstrip('( ').rstrip(')').split(',')
			nodes[node.strip()] = (l.strip(),r.strip())
	print(bfs('AAA','ZZZ'))

	# Part 2 Solution
	ends     = [ x for x in nodes.keys() if x[-1] == 'Z' ]
	starts   = [ x for x in nodes.keys() if x[-1] == 'A' ]
	cycles   = [ bfs(s,ends) for s in starts ]
	print(lcm(*cycles))

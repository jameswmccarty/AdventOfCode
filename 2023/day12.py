#!/usr/bin/python

from collections import deque

def ways(s,n):
	sols = set()
	q = deque()
	q.append((s,n,''))
	while q:
		s,n,b = q.popleft()
		if len(n) == 0 and (len(s) == 0 or '#' not in set(s)):
			b += '.'*len(s)
			sols.add(b)
		if len(n) > 0 and len(s) >= n[0]:
			if '.' not in s[0:n[0]]:
				if len(s) == n[0]:
					q.append((s[n[0]:],n[1:],b+'#'*n[0]))
				elif s[n[0]] != '#':
					q.append((s[n[0]+1:],n[1:],b+'#'*n[0]+'.'))
			if len(s) > 0 and s[0] != '#':
				q.append((s[1:],n[:],b+'.'))
	return sols				

seen = dict()

def ways2(s,n):
	if (s,tuple(n)) in seen:
		return seen[(s,tuple(n))]
	if len(n) == 0 and (len(s) == 0 or '#' not in set(s)):
		return 1
	if len(n) > 0 and len(s) >= n[0]:
			total = 0
			if '.' not in s[0:n[0]]:
				if len(s) == n[0]:
					total += ways2(s[n[0]:],n[1:])
				elif s[n[0]] != '#':
					total += ways2(s[n[0]+1:],n[1:])
			if len(s) > 0 and s[0] != '#':
				total += ways2(s[1:],n[:])
			seen[(s,tuple(n))] = total
			return total
	return 0

def unfold(s,n):
	out_s = s[:]
	out_n = n[:]
	for _ in range(4):
		out_s += '?' + s
		out_n += n[:]
	return out_s,out_n

if __name__ == "__main__":

	# Part 1 Solution
	total = 0
	with open("day12_input", "r") as infile:
		for line in infile:
			s,n = line.strip().split(' ')
			n = [ int(x) for x in n.split(',') ]
			total += len(ways(s,n))
	print(total)

	total = 0
	# Part 2 Solution
	with open("day12_input", "r") as infile:
		for line in infile:
			s,n = line.strip().split(' ')
			n = [ int(x) for x in n.split(',') ]
			ns,nn = unfold(s,n)
			total += ways2(ns,nn)
	print(total)

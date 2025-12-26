#!/usr/bin/python

import itertools


guests = {}

def add_guest(line):
	global guests
	line = line.split(" ")
	a = line[0] # First Person
	b = line[-1].strip(".") # Second Person
	delta = int(line[3]) # Value
	if line[2] == "lose":
		delta *= -1
	if a in guests:
		guests[a].update( { b : delta } )
	else:
		guests[a] = { b : delta }
		guests[a].update( { 'me' : 0 } )
		
def score(arr):
	s = 0
	for i in range(len(arr)):
		s += guests[arr[i]][arr[i-1]]
		s += guests[arr[i]][arr[(i+1)%len(arr)]]
	return s

if __name__ == "__main__":

	# Part 1 Solution
	
	with open("day13_input", "r") as infile:
		for line in infile.readlines():
			add_guest(line.strip())

	print max(score(x) for x in itertools.permutations([ y for y in guests ]))
	
	# Part 2 Solution
	guests['me'] = {}
	for guest in guests:
		guests['me'].update( { guest : 0 } )	
	print max(score(x) for x in itertools.permutations([ y for y in guests ]))

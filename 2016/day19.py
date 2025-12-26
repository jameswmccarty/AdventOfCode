#!/usr/bin/python

from collections import deque

def gift_round_1(elves):
	while len(elves) > 1:
		elves.append(elves.popleft())
		elves.popleft()
	return elves

def gift_round_2(elves):
	while len(elves) > 1:
		del elves[len(elves)/2]
		elves.rotate(-1)
	return elves		
	
if __name__ == "__main__":

	# Part 1 Solution
	elves = deque()
	for x in range(3012210):
		elves.append(x+1)
	gift_round_1(elves)
	print elves.popleft()
	
	# Part 2 Solution
	
	# correct but slow
	
	elves = deque()
	for x in range(3012210):
		elves.append(x+1)
	gift_round_2(elves)
	print elves.popleft()

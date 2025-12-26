#!/usr/bin/python

import math


def house_presents(house_num):
	factors = set()
	for i in range(1,int(math.ceil(math.sqrt(house_num)))+1):
		if house_num % i == 0:
			factors.add(i)
			factors.add(house_num/i)
	return 10 * sum(factors)	

def house_presents2(house_num):
	factors = set()
	for i in range(1,int(math.ceil(math.sqrt(house_num)))+1):
		if house_num % i == 0:
			factors.add(i)
			factors.add(house_num/i)
	factors = [ x for x in factors if 50*x >= house_num ]
	return 11 * sum(factors)
	
def min_house(goal):
	goal /= 10
	goal *= 2
	n = 1
	while n*(n-1) < goal:
		n+=1
	return n

# invalid approach...
def bin_search(target, L, R):
	while L <= R:
		M = int(math.floor((L+R)/2))
		if house_presents(M) < target:
			L = M + 1
		elif house_presents(M) > target:
			R = M - 1
		else:
			return M
	return M
	
if __name__ == "__main__":

	# Part 1 Solution
	goal = 33100000
	house_num = min_house(goal)
	while house_presents(house_num) < goal:
		house_num += 1
	print house_num
	
	# Part 2 Solution

	house_num = min_house(goal)
	while house_presents2(house_num) < goal:
		house_num += 1
	print house_num

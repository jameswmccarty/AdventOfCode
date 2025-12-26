#!/usr/bin/python



if __name__ == "__main__":


	# Part 1 Solution

	fish = dict()
	days = 80
	with open("day06_input","r") as infile:
		counters = [ int(x) for x in infile.read().strip().split(',') ]
	for i in range(9):
		fish[i] = counters.count(i)
	for i in range(days):
		fish[(i+7)%9] += fish[i%9]
	print(sum(fish.values()))

	# Part 2 Solution

	days = 256
	for i in range(80,days):
		fish[(i+7)%9] += fish[i%9]
	print(sum(fish.values()))

#!/usr/bin/python


min_ways = 0

def count_ways(volume, avail):
	if volume == 0:
		return 1
	if volume < 0:
		return 0
	if len(avail) == 0:
		return 0
	for i in range(len(avail)):
		return count_ways(volume-avail[i], avail[i+1:]) + count_ways(volume, avail[i+1:])
		
def count_ways_min(volume, avail, used):
	if volume < 0:
		return float('inf')
	if len(avail) == 0:
		return float('inf')
	if volume == 0:
		return used
	for i in range(len(avail)):
		return min(count_ways_min(volume-avail[i], avail[i+1:], used+1), count_ways_min(volume, avail[i+1:], used))
		
def size_n_ways(volume, avail, limit, used):
	if volume < 0:
		return 0
	if used > limit:
		return 0
	if volume == 0 and used == limit:
		return 1
	if volume == 0 and used != limit:
		return 0
	if len(avail) == 0:
		return 0
	for i in range(len(avail)):
		return size_n_ways(volume-avail[i], avail[i+1:], limit, used+1) + size_n_ways(volume, avail[i+1:], limit, used)
		

if __name__ == "__main__":

	# Part 1 Solution

	bins = []
	
	volume = 150
	
	with open("day17_input", "r") as infile:
		for line in infile.readlines():
			bins.append(int(line.strip()))
	
	print count_ways(volume, bins)
	
	# Part 2 Solution

	print size_n_ways(volume, bins, count_ways_min(volume, bins, 0), 0)


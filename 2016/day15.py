#!/usr/bin/python


def time_test(disks, time):
	if len(disks) == 0:
		return True		
	# Disk is a tuple of (num positions, start position)
	# If start position + time % num_positions == 0
	# the ball passes through		
	if (disks[0][1]+time+1) % disks[0][0] != 0:
		return False
	return time_test(disks[1:], time+1)

if __name__ == "__main__":

	# Part 1 Solution
	
	disks = []
	time = 0
	
	with open("day15_input", "r") as infile:
		for line in infile.readlines():
			line = line.split(" ")
			disks.append((int(line[3]),int(line[-1].replace(".",'').strip())))
			
	while not time_test(disks, time):
		time += 1
	print time
	
	# Part 2 Solution
	
	disks.append((11,0))
	time = 0
	while not time_test(disks, time):
		time += 1
	print time
	

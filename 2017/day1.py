#!/usr/bin/python


if __name__ == "__main__":

	#Part 1 Solution	
	
	with open("day1_input", "r") as infile:
		line = infile.read().strip()
	
	sum = 0	
	for i in range(len(line)):
		if line[i] == line[(i+1)%len(line)]:
			sum += int(line[i])	
	print sum
	
	#Part 2 Solution

	sum = 0	
	for i in range(len(line)):
		if line[i] == line[(i+(len(line)/2))%len(line)]:
			sum += int(line[i])	
	print sum
	
		
	
	

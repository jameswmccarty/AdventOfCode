#!/usr/bin/python


class Range:

	def __init__(self, low, high):
		self.low = low
		self.high = high
		
	def includes(self, low_val, high_val):
		if self.low <= low_val <= self.high or self.low <= high_val <= self.high:
			return True
		return False
		
	def grow(self, low_val, high_val):
		self.low = min(self.low, low_val)
		self.high = max(self.high, high_val)


if __name__ == "__main__":

	# Part 1 Solution
	
	ranges = []
	
	with open("day20_input", "r") as infile:
		for line in infile.readlines():
			line = line.strip().split("-")
			low = int(line[0])
			high = int(line[1])
			contained = False
			for range in ranges:
				if range.includes(low, high):
					range.grow(low, high)
					contained = True
			if not contained:
				ranges.append(Range(low, high))			
			
	low_addr = 0
	
	while True:
		valid = True
		for range in ranges:
			if range.includes(low_addr, low_addr):
				low_addr = range.high + 1
				valid = False
				break
		if valid:
			break
	print low_addr
			
	# Part 2 Solution

	valid_count = 0
	current_addr = 0
	while current_addr < 4294967295:
		valid = True
		for range in ranges:
			if range.includes(current_addr,current_addr):
				current_addr = range.high + 1
				valid = False
				break
		if valid:
			valid_count += 1
			current_addr += 1
			
	print valid_count
	

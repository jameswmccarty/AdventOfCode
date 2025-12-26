#!/usr/bin/python


digits = { "one" : '1',
	   "two" : '2',
	   "three" : '3',
	   "four" : '4',
	   "five" : '5',
	   "six" : '6',
	   "seven" : '7',
	   "eight" : '8',
	   "nine" : '9' }

def line_int(line):
	nums = ''.join(x for x in line if x in '123456789')
	return int(nums[0]+nums[-1])

def first_int(line,reverse):
	buf = ''
	if reverse:
		line = line[::-1]
	for char in line:
		for k,v in digits.items():
			if k in buf:
				return v
		if char in '123456789':
			return char
		if reverse:
			buf = char + buf
		else:
			buf = buf + char
		
if __name__ == "__main__":

	# Part 1 Solution
	with open("day01_input", "r") as infile:
		print(sum(line_int(line) for line in infile))

	# Part 2 Solution
	with open("day01_input", "r") as infile:
		print(sum(int(first_int(line,False)+first_int(line,True)) for line in infile))

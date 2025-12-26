#!/usr/bin/python


def is_trap(window):
    # Its left and center tiles are traps, but its right tile is not.
	if window[0] == '^' and window[1] == '^' and window[2] == '.':
		return True
    # Its center and right tiles are traps, but its left tile is not.
	if window[0] == '.' and window[1] == '^' and window[2] == '^':
		return True
    # Only its left tile is a trap.
	if window[0] == '^' and window[1] == '.' and window[2] == '.':
		return True
    # Only its right tile is a trap.
	if window[0] == '.' and window[1] == '.' and window[2] == '^':
		return True
	return False

def next_row(i):
	n = ['.'] * len(i)
	window = '.' + i[0:2]
	if is_trap(window):
		n[0] = '^'
	for j in range(1,len(i)-1):
		if is_trap(i[j-1:j+2]):
			n[j] = '^'
	window = i[-2:] + '.'
	if is_trap(window):
		n[len(i)-1] = '^'
	return ''.join(n)	

if __name__ == "__main__":

	# Part 1 Solution
	
	with open("day18_input", "r") as infile:
		line = infile.read().strip()
		
	#line = '.^^.^.^^^^'
	trap_count = 0
	for i in range(40):
		#print line
		trap_count += line.count(".")
		line = next_row(line)
	print trap_count
	
	# Part 2 Solution

	with open("day18_input", "r") as infile:
		line = infile.read().strip()
		
	trap_count = 0
	for i in range(400000):
		trap_count += line.count(".")
		line = next_row(line)
	print trap_count

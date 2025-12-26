#!/usr/bin/python

def reflect(lines):
	for i in range(1,len(lines)):
		match = True
		l = i-1
		r = i
		while l >= 0 and r < len(lines):
			if lines[l] != lines[r]:
				match = False
				break
			l -= 1
			r += 1
		if match:
			return i
	return 0

def diff(a,b):
	count = 0
	for i,c in enumerate(a):
		if b[i] != c:
			count += 1
	return count

def reflect2(lines):
	for i in range(1,len(lines)):
		count = 0
		l = i-1
		r = i
		while l >= 0 and r < len(lines):
			count += diff(lines[l],lines[r])
			l -= 1
			r += 1
		if count == 1:
			return i
	return 0

def score(block):
	total = 0
	h_lines = block.split('\n')
	total += 100*reflect(h_lines)
	v_lines = list()
	for i in range(len(h_lines[0].strip())):
		v_line = ''.join( x[i] for x in h_lines )
		v_lines.append(v_line)
	return total + reflect(v_lines)

def score2(block):
	h_lines = block.split('\n')
	v_lines = list()
	for i in range(len(h_lines[0].strip())):
		v_line = ''.join( x[i] for x in h_lines )
		v_lines.append(v_line)
	v_total = reflect2(v_lines)
	if v_total > 0:
		return v_total
	total = 100*reflect2(h_lines)
	if total > 0:
		return total
	return 0

if __name__ == "__main__":

	# Part 1 Solution
	with open("day13_input", "r") as infile:
		blocks = infile.read().strip().split('\n\n')
	print(sum(score(b) for b in blocks))
	
	# Part 2 Solution
	print(sum(score2(b) for b in blocks))



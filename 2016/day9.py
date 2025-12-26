#!/usr/bin/python


def version_2(line):
	length = 0
	idx = 0
	while idx < len(line):
		if line[idx] == '(':
			substr = ''
			idx += 1
			while line[idx] != ')':
				substr += line[idx]
				idx += 1
			skip, repeat = substr.split("x")
			segment = line[idx+1:idx+1+int(skip)]
			length += int(repeat) * version_2(segment)
			idx += int(skip) +1
		else:
			length += 1
			idx += 1
	return length

def decompress(line):
	out = ''
	idx = 0
	while idx < len(line):
		if line[idx] == '(':
			substr = ''
			idx += 1
			while line[idx] != ')':
				substr += line[idx]
				idx += 1
			skip, repeat = substr.split("x")
			segment = ''
			for j in range(idx+1, idx+1+int(skip)):
				segment += line[j]
			out += int(repeat) * segment
			idx += int(skip)+1
		else:
			out += line[idx]
			idx += 1			
	return out
	
if __name__ == "__main__":

	lines = ''
	# Part 1 Solution
	with open("day9_input", "r") as infile:
		for line in infile.readlines():
			lines += line.strip()
	
	print len(decompress(lines))
	
	# Part 2 Solution
	
	print version_2(lines)
	
	

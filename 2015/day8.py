#!/usr/bin/python


hex_chars = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' ]

if __name__ == "__main__":

	char_count = 0
	lit_count  = 0

	# Part 1 Solution
	with open("day8_input", "r") as infile:
		for line in infile.readlines():
			line = line.strip()
			char_count += len(line)
			i = 1
			while i < len(line)-1:
				if line[i] == '\\':
					if line[i+1] == r'"':
						i += 1
					elif line[i+1] == '\\':
						i += 1
					elif line[i+1] == 'x' and line[i+2] in hex_chars and line[i+3] in hex_chars:
						i += 3
				lit_count += 1
				i += 1
	print char_count - lit_count
	
	# Part 2 Solution
	char_count = 0
	lit_count  = 0
	with open("day8_input", "r") as infile:
		for line in infile.readlines():
			line = line.strip()
			lit_count += len(line)
			char_count += 2 # trailing and leading quote
			i = 0
			while i < len(line):
				if line[i] == r'"':
					char_count += 1
				elif line[i] == '\\':
					char_count += 1
				char_count += 1
				i += 1
	print char_count - lit_count
					
	

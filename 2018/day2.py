#!/usr/bin/python


def editDist(str1, str2):
	if len(str1) != len(str2):
		print "Error: Input size must match."
		exit()
	dist = 0
	for i in range(0, len(str1)):
		if str1[i] != str2[i]:
			dist += 1
	return dist
	
def min_str(str1, str2):
	out = ''
	for i in range(0, len(str1)):
		if str1[i] == str2[i]:
			out += str1[i]
	return out	

if __name__ == "__main__":

	#Part 1 solution
	twos = 0
	threes = 0
	with open("day2_input", "r") as infile:
		for line in infile.readlines():
			freq_gram = [0] * 26
			for char in line.strip():
				freq_gram[ord(char)-97] += 1
			if 2 in freq_gram:
				twos += 1
			if 3 in freq_gram:
				threes += 1
	print "Part 1 solution: " + str(twos * threes)
	
	#Part 2 solution
	all_lines = []
	with open("day2_input", "r") as infile:
		for line in infile.readlines():
			all_lines.append(line.strip())
	row_idx = 0
	found = False
	while row_idx < len(all_lines) and not found:
		for line in all_lines:
			if editDist(all_lines[row_idx], line) == 1:
				#print line
				#print all_lines[row_idx]
				print min_str(line, all_lines[row_idx])
				found = True
		row_idx += 1

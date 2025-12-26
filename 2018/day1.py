#/usr/bin/python


if __name__ == "__main__":

	#Part 1 solution
	freq = 0
	with open("day1_input", "r") as infile:
		for line in infile.readlines():
			freq += int(line.strip())
	print "Part 1 solution: " + str(freq)

	#Part 2 solution
	freq = 0
	inputs = []
	seen_set = set()
	found = False
	with open("day1_input", "r") as infile:
		for line in infile.readlines():
			inputs.append(int(line.strip()))
	#loop inputs as ring buffer
	while not found:
		for item in inputs:
			freq += item
			if freq in seen_set:
				print "Part 2 solution " + str(freq)
				found = True
				break;
			else:
				seen_set.add(freq)

		

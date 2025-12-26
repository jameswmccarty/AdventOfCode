#!/usr/bin/python


def react(string):
	# reaction between 'Aa' or 'aA' forms for a-z/A-Z
	for i in range(65,91): # upper ascii
		string = string.replace(chr(i).lower()+chr(i), '')
		string = string.replace(chr(i)+chr(i).lower(), '')
	return string

if __name__ == "__main__":
	# Part 1 Solution

	orig_input = ''
	polystring = ''
	with open("day5_input", "r") as infile:
		polystring = infile.read().strip()
	orig_input = polystring # save for Part #2
	
	last_ver = ''
	while last_ver != polystring:
		last_ver = polystring
		polystring = react(polystring)

	print "Remaining units: " + str(len(polystring))

	#Part 2 Solution
	
	lengths = [len(orig_input)] * 26
	for i in range(65,91): # upper ascii
		trialstr = orig_input.replace(chr(i), '')
		trialstr = trialstr.replace(chr(i).lower(), '')
		last_ver = ''
		while last_ver != trialstr:
			last_ver = trialstr
			trialstr = react(trialstr)
		lengths[i-65] = len(trialstr)
	
	print "Remove polymer " + str(chr(65+lengths.index(min(lengths))))
	print "Min length is " + str(min(lengths))

	

#!/usr/bin/python


def build_seq(seq):
	out = ''
	count = 0
	last = seq[0]
	for i in range(len(seq)):
		if last == seq[i]:
			count += 1
		else:
			out += str(count) + last
			count = 1
			last = seq[i]
	out += str(count) + last
	return out

if __name__ == "__main__":

	# Part 1 Solution

	#seq = "1"
	seq = "1321131112"
	
	for i in range(40):
		seq = build_seq(seq)
	print len(seq)

	# Part 2 Solution
	seq = "1321131112"	
	for i in range(50):
		seq = build_seq(seq)
	print len(seq)
	

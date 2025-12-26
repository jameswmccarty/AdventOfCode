#!/usr/bin/python


if __name__ == "__main__":

	# Part 1 Solution
	
	list = []
	for i in range(256):
		list.append(i)
	pos = 0
	skip = 0
	
	lengths = [197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63]
	
	for length in lengths:
		sublist = []
		for i in range(length):
			sublist.append(list[(pos+i)%len(list)])
		sublist.reverse()
		for i in range(length):
			list[(pos+i)%len(list)] = sublist[i]		
		pos += length + skip
		pos %= len(list)
		skip += 1
	
	print list[0]*list[1]
	
	# Part 2 Solution
	
	list = []
	for i in range(256):
		list.append(i)
	pos = 0
	skip = 0
	
	lengths = []
	input = "197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63"
	#input = "1,2,3"
	suffix = [17, 31, 73, 47, 23]
	for char in input:
		lengths.append(ord(char))
	for val in suffix:
		lengths.append(val)
	
	for round in range(64):
		for length in lengths:
			sublist = []
			for i in range(length):
				sublist.append(list[(pos+i)%len(list)])
			sublist.reverse()
			for i in range(length):
				list[(pos+i)%len(list)] = sublist[i]		
			pos += length + skip
			pos %= len(list)
			skip += 1
	hash = ''
	for i in range(16):
		char = 0
		for z in range(16):
			char ^= list[i*16 + z]
		hash += '%02x' % char
	
	print hash
		

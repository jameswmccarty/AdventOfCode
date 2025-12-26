#!/usr/bin/python


def validate(room, checksum):
	letters = dict()
	for segment in room:
		for char in segment:
			if char in letters:
				letters[char] += 1
			else:
				letters[char] = 1
	comp = [ x[0] for x in sorted(sorted(letters.items(), key=lambda a:a[0]), key=lambda b:b[1], reverse=True) ][0:5]
	if ''.join(comp) == checksum:
		return True
	return False

def decode(room, shift):
	out = ''
	for segment in room:
		for char in segment:
			val = ord(char)-97
			val += (shift % 26)
			val %= 26
			out += chr(val+97)
		out += ' '
	#print out
	return out
	
	
if __name__ == "__main__":

	# Part 1 Solution
	
	total = 0
	
	with open("day4_input", "r") as infile:
		for line in infile.readlines():
			room, checksum = line.split("[")
			checksum = checksum.replace("]", '').strip()
			segments = room.split("-")
			sector_ID = int(segments[-1])
			segments = segments[:-1]
			if validate(segments, checksum):
				total += sector_ID
				
	print total
	
	# Part 2 Solution
	with open("day4_input", "r") as infile:
		for line in infile.readlines():
			room, checksum = line.split("[")
			checksum = checksum.replace("]", '').strip()
			segments = room.split("-")
			sector_ID = int(segments[-1])
			segments = segments[:-1]
			if validate(segments, checksum):
				soln = decode(segments, sector_ID)
				if "north" in soln and "pole" in soln:
					print soln, sector_ID
	

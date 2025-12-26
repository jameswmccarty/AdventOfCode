#!/usr/bin/python

def find_key(subj_number):
	value = 1
	while True:
		value *= subj_number
		value %= 20201227
		yield value

if __name__ == "__main__":

	# Part 1 Solution
	with open("day25_input", 'r') as infile:
		door_pub = int(infile.readline().strip())
		card_pub = int(infile.readline().strip())
	
	#door_pub = 5764801
	#card_pub = 17807724
	
	loop_finder = find_key(7)
	count = 1
	found_door = False
	found_card = False
	while not (found_door or found_card):
		trial = next(loop_finder)
		if trial == door_pub:
			found_door = True
			break
		elif trial == card_pub:
			found_card = True
			break
		count += 1
	
	q = find_key(card_pub)
	p = find_key(door_pub)
	i = 0
	if found_door:
		while i < count:
			out = next(q)
			i += 1
	else:
		while i < count:
			out = next(p)
			i += 1
	print(out)

#!/usr/bin/python



deck = None
decksize = None

def cut(N):
	global deck
	deck = deck[N:] + deck[:N]

def deal(N):
	global deck
	new = [ None ] * len(deck)
	idx = 0
	while len(deck) > 0:
		new[idx%len(new)] = deck.pop(0)
		idx += N
	deck = new

def new_stack():
	global deck
	deck.reverse()

def parse_line(line):
	line = line.split(' ')
	if line[0] == 'cut':
		cut(int(line[-1]))
	elif line[0] == 'deal' and line[-1] == 'stack':
		new_stack()
	elif line[0] == 'deal':
		deal(int(line[-1]))
	else:
		print("Error:", line)
		exit()

def cut_2(i, N):
	global decksize
	return ((decksize-N)+i) % decksize

def deal_2(i, N):
	global decksize
	return (i*N) % decksize

def new_stack_2(i):
	global decksize
	return (decksize - i - 1) % decksize

def parse_line_2(line, i):
	line = line.split(' ')
	if line[0] == 'cut':
		i = cut_2(i, int(line[-1]))
	elif line[0] == 'deal' and line[-1] == 'stack':
		i = new_stack_2(i)
	elif line[0] == 'deal':
		i = deal_2(i, int(line[-1]))
	else:
		print("Error:", line)
		exit()
	return i

def unshuffle(n):
	return ((n - 140568611385) / 6871724559536) + 2

if __name__ == "__main__":

	# Part 1 Solution

	deck = [ i for i in range(10007) ]
	with open("day22_input", 'r') as infile:
		for line in infile.readlines():
			parse_line(line.strip())
	print(deck.index(2019))

	"""
	place = 2019
	decksize = 10007
	with open("day22_input", 'r') as infile:
		for line in infile.readlines():
			place = parse_line_2(line.strip(), place)
	print(place)
	"""

	# Part 2 Solution

	"""
	big_size = 119315717514047
	num_shuffle = 101741582076661
	shuff_seq = []
	place = 0
	decksize = big_size
	with open("day22_input", 'r') as infile:
		for line in infile.readlines():
			shuff_seq.append(line.strip())
	shuff_seq.reverse()
	for z in range(250):
		place = z
		for step in shuff_seq:
			place = parse_line_2(step, place)
		print(z, place)


	# Place				Delta		Difference
	# 0	105712837006360		
	# 1	112584561565896		
	# 2	140568611385		
	# 3	7012293170921	6871724559536	140568611385
	# 4	13884017730457	6871724559536	

	# Linear sequence: P1 = ((P0 - 2) * 6871724559536 + 140568611385) % 119315717514047
	"""

#!/usr/bin/python


gens = dict()
board = dict()
seen = set()

def spawn_board():
	new = dict()
	for j in range(5):
		for i in range(5):
			new[(i,j)] = '.'
	return new

def parse_line(idx, line):
	global board
	for row, char in enumerate(line.strip()):
		board[(row,idx)] = char

def get_count(x, y):
	global board
	count = 0
	if (x-1,y) in board and board[(x-1,y)] == '#':
		count += 1
	if (x+1,y) in board and board[(x+1,y)] == '#':
		count += 1
	if (x,y-1) in board and board[(x,y-1)] == '#':
		count += 1
	if (x,y+1) in board and board[(x,y+1)] == '#':
		count += 1
	return count

def survives(x, y):
	count = get_count(x,y)
	if board[(x,y)] == '#' and count == 1:
		return True
	elif board[(x,y)] == '.' and (count == 1 or count == 2):
		return True
	return False	

def next_gen():
	global board
	next = spawn_board()
	for i in range(5):
		for j in range(5):
			if survives(j, i):
				next[(j,i)] = '#'
	board = next

def score_board():
	global board
	total = 0
	power = 1
	for j in range(5):
		for i in range(5):
			if board[(i,j)] == '#':
				total += power
			power *= 2
	return total

def score_board2():
	global gens
	total = 0
	for key in gens.keys():
		for j in range(5):
			for i in range(5):
				if gens[key][(i,j)] == '#':
					total += 1
	return total

def parse2_line(idx, line, board):
	for row, char in enumerate(line.strip()):
		board[(row,idx)] = char
	return board

def survives2(key, x, y, low, high):
	count = get_count2(key, x, y, low, high)
	if gens[key][(x,y)] == '#' and count == 1:
		return True
	elif gens[key][(x,y)] == '.' and (count == 1 or count == 2):
		return True
	return False

def next_gen2():
	global gens
	low = min(gens.keys())
	high = max(gens.keys())
	gens[low-1] = spawn_board()
	gens[high+1] = spawn_board()
	next = dict()
	for key in gens.keys():
		next[key] = spawn_board()
	for key in gens.keys():
		for j in range(5):
			for i in range(5):
				if (i,j) != (2,2) and survives2(key, i, j, low, high):
					next[key][(i,j)] = '#'
	gens = next


"""
     |     |         |     |     
 0,0 | 1,0 |  2,0    | 3,0 | 4,0 
     |     |         |     |     
-----+-----+---------+-----+-----
     |     |         |     |     
 0,1 | 1,1 |  2,1    | 3,1 | 4,1
     |     |         |     |     
-----+-----+---------+-----+-----
     |     | | | | | |     |     
     |     |-+-+-+-+-|     |     
     |     | | | | | |     |     
 0,2 | 1,2 |-+-+-+-+-|     |     
     |     | | |?| | | 3,2 | 4,2 
     |     |-+-+-+-+-|     |     
     |     | | | | | |     |     
     |     |-+-+-+-+-|     |     
     |     | | | | | |     |     
-----+-----+---------+-----+-----
     |     |         |     |     
 0,3 | 1,3 |  2,3    | 3,3 | 4,3 
     |     |         |     |     
-----+-----+---------+-----+-----
     |     |         |     |     
 0,4 | 1,4 |  2,4    | 3,4 | 4,4 
     |     |         |     |     
"""	

def get_count2(key, x, y, low, high):
	count = 0
	pos = (x,y)
	if pos == (0,0):
		count += 1 if key > low and gens[key-1][(2,1)] == '#' else 0
		count += 1 if key > low and gens[key-1][(1,2)] == '#' else 0
		count += 1 if gens[key][(1,0)] == '#' else 0
		count += 1 if gens[key][(0,1)] == '#' else 0
	elif pos == (0,1):
		count += 1 if gens[key][(0,0)] == '#' else 0
		count += 1 if gens[key][(1,1)] == '#' else 0
		count += 1 if gens[key][(0,2)] == '#' else 0
		count += 1 if key > low and gens[key-1][(1,2)] == '#' else 0
	elif pos == (0,2):
		count += 1 if gens[key][(0,1)] == '#' else 0
		count += 1 if gens[key][(0,3)] == '#' else 0
		count += 1 if gens[key][(1,2)] == '#' else 0
		count += 1 if key > low and gens[key-1][(1,2)] == '#' else 0
	elif pos == (0,3):
		count += 1 if gens[key][(0,2)] == '#' else 0
		count += 1 if gens[key][(1,3)] == '#' else 0
		count += 1 if gens[key][(0,4)] == '#' else 0
		count += 1 if key > low and gens[key-1][(1,2)] == '#' else 0
	elif pos == (0,4):
		count += 1 if gens[key][(0,3)] == '#' else 0
		count += 1 if gens[key][(1,4)] == '#' else 0
		count += 1 if key > low and gens[key-1][(1,2)] == '#' else 0
		count += 1 if key > low and gens[key-1][(2,3)] == '#' else 0

	elif pos == (1,0):
		count += 1 if key > low and gens[key-1][(2,1)] == '#' else 0
		count += 1 if gens[key][(0,0)] == '#' else 0
		count += 1 if gens[key][(2,0)] == '#' else 0
		count += 1 if gens[key][(1,1)] == '#' else 0
	elif pos == (1,1):
		count += 1 if gens[key][(1,0)] == '#' else 0
		count += 1 if gens[key][(0,1)] == '#' else 0
		count += 1 if gens[key][(1,2)] == '#' else 0
		count += 1 if gens[key][(2,1)] == '#' else 0
	elif pos == (1,2):
		count += 1 if gens[key][(1,1)] == '#' else 0
		count += 1 if gens[key][(0,2)] == '#' else 0
		count += 1 if gens[key][(1,3)] == '#' else 0
		for i in range(5):
			count += 1 if key < high and gens[key+1][(0,i)] == '#' else 0
	elif pos == (1,3):
		count += 1 if gens[key][(1,2)] == '#' else 0
		count += 1 if gens[key][(0,3)] == '#' else 0
		count += 1 if gens[key][(2,3)] == '#' else 0
		count += 1 if gens[key][(1,4)] == '#' else 0
	elif pos == (1,4):
		count += 1 if gens[key][(1,3)] == '#' else 0
		count += 1 if gens[key][(0,4)] == '#' else 0
		count += 1 if gens[key][(2,4)] == '#' else 0
		count += 1 if key > low and gens[key-1][(2,3)] == '#' else 0

	elif pos == (2,0):
		count += 1 if key > low and gens[key-1][(2,1)] == '#' else 0
		count += 1 if gens[key][(1,0)] == '#' else 0
		count += 1 if gens[key][(3,0)] == '#' else 0
		count += 1 if gens[key][(2,1)] == '#' else 0
	elif pos == (2,1):
		count += 1 if gens[key][(2,0)] == '#' else 0
		count += 1 if gens[key][(1,1)] == '#' else 0
		count += 1 if gens[key][(3,1)] == '#' else 0
		for i in range(5):
			count += 1 if key < high and gens[key+1][(i,0)] == '#' else 0
	elif pos == (2,3):
		count += 1 if gens[key][(1,3)] == '#' else 0
		count += 1 if gens[key][(2,4)] == '#' else 0
		count += 1 if gens[key][(3,3)] == '#' else 0
		for i in range(5):
			count += 1 if key < high and gens[key+1][(i,4)] == '#' else 0
	elif pos == (2,4):
		count += 1 if gens[key][(2,3)] == '#' else 0
		count += 1 if gens[key][(1,4)] == '#' else 0
		count += 1 if gens[key][(3,4)] == '#' else 0
		count += 1 if key > low and gens[key-1][(2,3)] == '#' else 0

	elif pos == (3,0):
		count += 1 if gens[key][(2,0)] == '#' else 0
		count += 1 if gens[key][(4,0)] == '#' else 0
		count += 1 if gens[key][(3,1)] == '#' else 0
		count += 1 if key > low and gens[key-1][(2,1)] == '#' else 0
	elif pos == (3,1):
		count += 1 if gens[key][(3,0)] == '#' else 0
		count += 1 if gens[key][(2,1)] == '#' else 0
		count += 1 if gens[key][(4,1)] == '#' else 0
		count += 1 if gens[key][(3,2)] == '#' else 0
	elif pos == (3,2):
		count += 1 if gens[key][(3,1)] == '#' else 0
		count += 1 if gens[key][(4,2)] == '#' else 0
		count += 1 if gens[key][(3,3)] == '#' else 0
		for i in range(5):
			count += 1 if key < high and gens[key+1][(4,i)] == '#' else 0
	elif pos == (3,3):
		count += 1 if gens[key][(3,2)] == '#' else 0
		count += 1 if gens[key][(2,3)] == '#' else 0
		count += 1 if gens[key][(4,3)] == '#' else 0
		count += 1 if gens[key][(3,4)] == '#' else 0
	elif pos == (3,4):
		count += 1 if gens[key][(3,3)] == '#' else 0
		count += 1 if gens[key][(2,4)] == '#' else 0
		count += 1 if gens[key][(4,4)] == '#' else 0
		count += 1 if key > low and gens[key-1][(2,3)] == '#' else 0

	elif pos == (4,0):
		count += 1 if key > low and gens[key-1][(2,1)] == '#' else 0
		count += 1 if key > low and gens[key-1][(3,2)] == '#' else 0
		count += 1 if gens[key][(4,1)] == '#' else 0
		count += 1 if gens[key][(3,0)] == '#' else 0
	elif pos == (4,1):
		count += 1 if gens[key][(4,0)] == '#' else 0
		count += 1 if gens[key][(3,1)] == '#' else 0
		count += 1 if gens[key][(4,2)] == '#' else 0
		count += 1 if key > low and gens[key-1][(3,2)] == '#' else 0
	elif pos == (4,2):
		count += 1 if gens[key][(4,1)] == '#' else 0
		count += 1 if gens[key][(3,2)] == '#' else 0
		count += 1 if gens[key][(4,3)] == '#' else 0
		count += 1 if key > low and gens[key-1][(3,2)] == '#' else 0
	elif pos == (4,3):
		count += 1 if gens[key][(4,2)] == '#' else 0
		count += 1 if gens[key][(3,3)] == '#' else 0
		count += 1 if gens[key][(4,4)] == '#' else 0
		count += 1 if key > low and gens[key-1][(3,2)] == '#' else 0
	elif pos == (4,4):
		count += 1 if gens[key][(4,3)] == '#' else 0
		count += 1 if gens[key][(3,4)] == '#' else 0
		count += 1 if key > low and gens[key-1][(2,3)] == '#' else 0
		count += 1 if key > low and gens[key-1][(3,2)] == '#' else 0

	return count


if __name__ == "__main__":

	# Part 1 Solution

	with open("day24_input", 'r') as infile:
		idx = 0
		for line in infile.readlines():
			parse_line(idx, line.strip())
			idx += 1

	while hash(frozenset(board.items())) not in seen:
		seen.add(hash(frozenset(board.items())))
		next_gen()
	print(score_board())

	# Part 2 Solution
	gen0 = dict()
	with open("day24_input", 'r') as infile:
		idx = 0
		for line in infile.readlines():
			parse2_line(idx, line.strip(), gen0)
			idx += 1
	gens[0] = gen0

	for x in range(200):
		next_gen2()
	print(score_board2())


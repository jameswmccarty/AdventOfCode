#!/usr/bin/python

valid_dirs = ('e', 'se', 'sw', 'w', 'nw', 'ne')

"""
  \ e  /
ne +--+ se
  /    \
-+      +-
  \    /
nw +--+ sw
  / w  \
"""

swaps = {"se, w" : "sw",
		 "w, se" : "sw",
		 "ne, se": "e",
		 "se, ne": "e",
		 "nw, sw": "w",
		 "sw, nw": "w",
		 "ne, w" : "nw",
		 "w, ne" : "nw",
		 "sw, e" : "se",
		 "e, sw" : "se",
		 "e, nw" : "ne",
		 "nw, e" : "ne"}

black_tiles = set()

def tokenize(line):
	tokens = []
	while len(line) > 0:
		if line[:2] in valid_dirs:
			tokens.append(line[:2])
			line = line[2:]
		else:
			tokens.append(line[0])
			line = line[1:]
	return tokens

def compress(tokens):
	compressed = []
	while len(tokens) > 0:
		trial = ', '.join(tokens[:2])
		if trial in swaps.keys():
			if swaps[trial] != '':
				compressed.append(swaps[trial])
			tokens = tokens[2:]
		else:
			compressed.append(tokens[0])
			tokens = tokens[1:]
	return compressed

def path_compress(path):
	# X = NE | SW
	# Y =  E | W
	# Z = SE | NW
	last_sum = 0
	while last_sum != sum(path.values()):
		last_sum = sum(path.values())
		# Cancel E and W
		m = min(path['e'],path['w'])
		path['e'] -= m
		path['w'] -= m
		# Cancel NE and SW
		m = min(path['ne'],path['sw'])
		path['ne'] -= m
		path['sw'] -= m
		# Cancel NW and SE
		m = min(path['nw'],path['se'])
		path['nw'] -= m
		path['se'] -= m
		# Compress NE + SE = E
		m = min(path['ne'],path['se'])
		path['e'] += m
		path['ne'] -= m
		path['se'] -= m
		# Compress NW + SW = W
		m = min(path['nw'],path['sw'])
		path['w'] += m
		path['nw'] -= m
		path['sw'] -= m
		# Compress SE + W = SW
		m = min(path['se'],path['w'])
		path['sw'] += m
		path['se'] -= m
		path['w'] -= m
		# Compress NE + W = NW
		m = min(path['ne'],path['w'])
		path['nw'] += m
		path['ne'] -= m
		path['w'] -= m
		# Compress SW + E = SE
		m = min(path['sw'],path['e'])
		path['se'] += m
		path['sw'] -= m
		path['e'] -= m
		# Compress NW + E = NE
		m = min(path['nw'],path['e'])
		path['ne'] += m
		path['nw'] -= m
		path['e'] -= m
	
	return path
	
def parse(line):
	tokens = tokenize(line)
	#tokens = compress(tokens)
	#last = float('inf')
	#while last != len(tokens):
	#	last = len(tokens)
	#	tokens = compress(tokens)
	path = {"e" : 0, "se": 0, "ne": 0, "w": 0, "nw": 0, "sw": 0}
	for t in tokens:
		path[t] += 1
	path = path_compress(path)
	path = ','.join(str(x) for x in path.values())
	if path in black_tiles:
		black_tiles.remove(path)
	else:
		black_tiles.add(path)

def count_adjacent(path):
	count = 0
	start_loc = {"e" : 0, "se": 0, "ne": 0, "w": 0, "nw": 0, "sw": 0}
	path = [ int(x) for x in path.split(",") ]
	start_loc['e']  = path[0]
	start_loc['se'] = path[1]
	start_loc['ne'] = path[2]
	start_loc['w']  = path[3]
	start_loc['nw'] = path[4]
	start_loc['sw'] = path[5]

	for step in valid_dirs:
		trial = start_loc.copy()
		trial[step] += 1
		trial = path_compress(trial)
		trial = ','.join(str(x) for x in trial.values())
		if trial in black_tiles:
			count += 1

	return count

def new_day():
	global black_tiles
	next = set()
	evaluated = set()
	for tile in list(black_tiles):
		count = count_adjacent(tile)
		if not (count == 0 or count > 2):
			next.add(tile)
		for i in range(6):
			trial = [ int(x) for x in tile.split(",") ]
			trial[i] += 1
			start_loc = {"e" : 0, "se": 0, "ne": 0, "w": 0, "nw": 0, "sw": 0}
			start_loc['e']  = trial[0]
			start_loc['se'] = trial[1]
			start_loc['ne'] = trial[2]
			start_loc['w']  = trial[3]
			start_loc['nw'] = trial[4]
			start_loc['sw'] = trial[5]
			start_loc = path_compress(start_loc)
			trial = ','.join(str(x) for x in start_loc.values())
			if trial not in evaluated:
				evaluated.add(trial)
				if count_adjacent(trial) == 2:
					next.add(trial)
	black_tiles = next

if __name__ == "__main__":

	# Part 1 Solution
	with open("day24_input", 'r') as infile:
		for line in infile.readlines():
			parse(line.strip())
	print(len(black_tiles))

	# Part 2 Solution
	for _ in range(100):
		new_day()
	print(len(black_tiles))

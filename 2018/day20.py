#!/usr/bin/python


rooms = set()
doors1 = set()
doors2 = set()
final_map = dict()
map_dims = None
struct_map = []

def explore(start, re):

	#print start, re

	root_pos = start
	pos = start
	steps = 0
	most_steps = 0

	while len(re) > 0:
		x, y = pos
		char = re[0]
		if char == ')':
			most_steps = max(most_steps, steps)
			return most_steps, pos
		if char == 'N':
			doors1.add((x,y-1))
			rooms.add((x,y-2))
			pos = (x,y-2)
			re = re[1:]
			steps += 1
		if char == 'S':
			doors1.add((x,y+1))
			rooms.add((x,y+2))
			pos = (x,y+2)
			re = re[1:]
			steps += 1
		if char == 'E':
			doors2.add((x+1,y))
			rooms.add((x+2,y))
			pos = (x+2,y)
			re = re[1:]
			steps += 1		
		if char == 'W':
			doors2.add((x-1,y))
			rooms.add((x-2,y))
			pos = (x-2,y)
			re = re[1:]
			steps += 1
		if char == '|':
			pos = root_pos
			re = re[1:]
			most_steps = max(most_steps, steps)
			steps = 0
		if char == '(':
			ctr = 1
			idx = 1
			sub_str = ''
			while ctr != 0:
				sub_str += re[idx]
				if re[idx] == '(':
					ctr += 1
				if re[idx] == ')':
					ctr -= 1
				idx += 1
			t_steps, t_pos = explore(pos, sub_str)
			if t_pos != pos:
				steps += t_steps
			re = re[idx:]
		if char == '^':
			re = re[1:]
		if char == '$':
			most_steps = max(most_steps, steps)
			return most_steps, pos

def index_map():
	global map_dims
	minx = float('inf')
	miny = float('inf')
	maxx = 0
	maxy = 0

	for entry in rooms:
		minx = min(minx, entry[0])
		miny = min(miny, entry[1])

	for entry in doors1:
		minx = min(minx, entry[0])
		miny = min(miny, entry[1])

	for entry in doors2:
		minx = min(minx, entry[0])
		miny = min(miny, entry[1])

	minx = abs(minx) + 1
	miny = abs(miny) + 1

	for entry in rooms:
		final_map[(entry[0]+minx,entry[1]+miny)] = '.'
	for entry in doors1:
		final_map[(entry[0]+minx,entry[1]+miny)] = '-'
	for entry in doors2:
		final_map[(entry[0]+minx,entry[1]+miny)] = '|'
	final_map[(minx, miny)] = 'X'

	for entry in final_map.keys():
		maxx = max(entry[0], maxx) 
		maxy = max(entry[1], maxy) 

	map_dims = (maxx, maxy)

def print_map():
	maxx, maxy = map_dims
	maxx += 2
	maxy += 2
	for i in range(maxy):
		out = ['#'] * maxx
		for j in range(maxx):
			if (j,i) in final_map:
				out[j] = final_map[(j,i)]
		print ''.join(out)

def structure_map():
	maxx, maxy = map_dims
	maxx += 2
	maxy += 2
	for i in range(maxy):
		out = ['#'] * maxx
		for j in range(maxx):
			if (j,i) in final_map:
				out[j] = final_map[(j,i)]
		struct_map.append(out)

def exclude_rooms(radius):

	queue = []
	seen = set()
	for i, row in enumerate(struct_map):
		for j, col in enumerate(row):
			if col == 'X':
				center = (i,j)
	queue.append((center, 0))
	
	while len(queue) != 0:
		pos, steps = queue.pop(0)
		x, y = pos
		seen.add(pos)
		if steps < 1000:
			struct_map[x][y] = 'X'
		if struct_map[x-1][y] == '-' and struct_map[x-2][y] == '.' and (x-2,y) not in seen:
			queue.append(((x-2,y), steps+1))
		if struct_map[x+1][y] == '-' and struct_map[x+2][y] == '.' and (x+2,y) not in seen: 
			queue.append(((x+2,y), steps+1))
		if struct_map[x][y+1] == '|' and struct_map[x][y+2] == '.' and (x,y+2) not in seen:
			queue.append(((x,y+2), steps+1))		
		if struct_map[x][y-1] == '|' and struct_map[x][y-2] == '.'and (x,y-2) not in seen:
			queue.append(((x,y-2), steps+1))			
		

def score_map():
	rooms = 0
	for row in struct_map:
		rooms += row.count('.')
	return rooms

if __name__ == "__main__":

	# Part 1 Solution

	#print explore((0,0), '^ENWWW(NEEE|SSE(EE|N))$') # 10 doors
	#print explore((0,0), '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$') # 18 doors
	#print explore((0,0), '^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$') # 23 doors
	#print explore((0,0), '^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$') # 31 doors

	with open("day20_input", 'r') as infile:
		route = infile.read().strip()

	print explore((0,0), route) # 3721 per input
	index_map()
	print_map()
	
	# Part 2 Solution

	structure_map()
	exclude_rooms(1000)
	print score_map()

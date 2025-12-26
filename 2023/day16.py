#!/usr/bin/python


from collections import deque

layout = dict()

def show_map(s,x_dim,y_dim):
	for y in range(y_dim):
		for x in range(x_dim):
			if (x,y) in s:
				print('#',end='')
			else:
				print('.',end='')
		print()

def beam_walk(x_dim,y_dim,p,d):
	seen = set()
	q = deque()
	seen.add((p,d))
	q.append((p,d))
	while q:
		p,d = q.popleft()
		x,y   = p
		dx,dy = d
		if p not in layout and ((x+dx,y+dy),d) not in seen and x+dx >= 0 and x+dx < x_dim and y+dy >= 0 and y+dy < y_dim:
			seen.add(((x+dx,y+dy),d))
			q.append(((x+dx,y+dy),d))
		elif p in layout:
			m = layout[p]
			if m == '-' and d in ((1,0),(-1,0)): # horizontal travel,no split
				if ((x+dx,y+dy),d) not in seen and x+dx >= 0 and x+dx < x_dim and y+dy >= 0 and y+dy < y_dim:
					seen.add(((x+dx,y+dy),d))
					q.append(((x+dx,y+dy),d))
			elif m == '-' and d in ((0,1),(0,-1)): # vertical travel, split
				for dx,dy in ((1,0),(-1,0)):
					if ((x+dx,y+dy),(dx,dy)) not in seen and x+dx >= 0 and x+dx < x_dim and y+dy >= 0 and y+dy < y_dim:
						seen.add(((x+dx,y+dy),(dx,dy)))
						q.append(((x+dx,y+dy),(dx,dy)))
			elif m == '|' and d in ((0,1),(0,-1)): # vertical travel,no split
				if ((x+dx,y+dy),d) not in seen and x+dx >= 0 and x+dx < x_dim and y+dy >= 0 and y+dy < y_dim:
					seen.add(((x+dx,y+dy),d))
					q.append(((x+dx,y+dy),d))
			elif m == '|' and d in ((1,0),(-1,0)): # horizontal travel, split
				for dx,dy in ((0,1),(0,-1)):
					if ((x+dx,y+dy),(dx,dy)) not in seen and x+dx >= 0 and x+dx < x_dim and y+dy >= 0 and y+dy < y_dim:
						seen.add(((x+dx,y+dy),(dx,dy)))
						q.append(((x+dx,y+dy),(dx,dy)))
			elif m == '/': # 90 degree turn
				if d == (1,0):
					dx,dy = (0,-1) # right to up
				if d == (-1,0):
					dx,dy = (0,1) # left to down
				if d == (0,1):
					dx,dy = (-1,0) # down to left
				if d == (0,-1):
					dx,dy = (1,0) # up to right
				if ((x+dx,y+dy),(dx,dy)) not in seen and x+dx >= 0 and x+dx < x_dim and y+dy >= 0 and y+dy < y_dim:
					seen.add(((x+dx,y+dy),(dx,dy)))
					q.append(((x+dx,y+dy),(dx,dy)))
			elif m == chr(92): # 90 degree turn \
				if d == (1,0):
					dx,dy = (0,1) # right to down
				if d == (-1,0):
					dx,dy = (0,-1) # left to up
				if d == (0,1):
					dx,dy = (1,0) # down to right
				if d == (0,-1):
					dx,dy = (-1,0) # up to left
				if ((x+dx,y+dy),(dx,dy)) not in seen and x+dx >= 0 and x+dx < x_dim and y+dy >= 0 and y+dy < y_dim:
					seen.add(((x+dx,y+dy),(dx,dy)))
					q.append(((x+dx,y+dy),(dx,dy)))
	return { x[0] for x in seen }

if __name__ == "__main__":

	# Part 1 Solution
	with open("day16_input", "r") as infile:
		y = 0
		for line in infile:
			x_dim = len(line.strip())
			for x,c in enumerate(line.strip()):
				if c != '.':
					layout[(x,y)] = c
			y += 1

	energized = beam_walk(x_dim,y,(0,0),(1,0))
	print(len((energized)))

	# Part 2 Solution
	most = 0
	for x in range(x_dim):
		most = max(most,len(beam_walk(x_dim,y,(x,0),(0,1)))) # top row
		most = max(most,len(beam_walk(x_dim,y,(x,y-1),(0,-1)))) # bottom row
	for y in range(y):
		most = max(most,len(beam_walk(x_dim,y,(0,y),(1,0)))) # left
		most = max(most,len(beam_walk(x_dim,y,(x_dim-1,y),(-1,0)))) # right
	# corners
	#most = max(most,len(beam_walk(x_dim,y,(0,0),(0,1))))
	most = max(most,len(beam_walk(x_dim,y,(0,0),(1,0))))
	
	#most = max(most,len(beam_walk(x_dim,y,(x_dim-1,0),(-1,0))))
	most = max(most,len(beam_walk(x_dim,y,(x_dim-1,0),(0,1))))
	
	#most = max(most,len(beam_walk(x_dim,y,(0,y-1),(1,0))))
	most = max(most,len(beam_walk(x_dim,y,(0,y-1),(0,-1))))

	#most = max(most,len(beam_walk(x_dim,y,(x_dim-1,y-1),(-1,0))))
	most = max(most,len(beam_walk(x_dim,y,(x_dim-1,y-1),(0,-1))))
	print(most)

#!/usr/bin/python


if __name__ == "__main__":

	# Part 1 Solution

	adj_points = [(1,0),(-1,0),(0,1),(0,-1)]
	map_points = dict()
	low_points = []
	with open("day09_input","r") as infile:
		cavemap = infile.read().strip()
	cavemap = cavemap.split('\n')
	for j,line in enumerate(cavemap):
		for i,point in enumerate(line):
			map_points[(i,j)] = int(point)
	low_total = 0
	for a,b in map_points:
		lowest = True
		for x,y in adj_points:
			if (a+x,b+y) in map_points and map_points[(a+x,b+y)] <= map_points[(a,b)]:
				lowest = False
		if lowest:
			low_total += (map_points[(a,b)]+1)
			low_points.append((a,b))
	print(low_total)


	# Part 2 Solution
	basins = []
	for x,y in low_points:
		basin = set()
		basin.add((x,y))
		q = [(x,y)]
		while len(q) > 0:
			x,y = q.pop(0)
			for dx,dy in adj_points:
				if (x+dx,y+dy) not in basin and (x+dx,y+dy) in map_points and map_points[(x+dx,y+dy)] != 9:
					q.append((x+dx,y+dy))
					basin.add((x+dx,y+dy))
		basins.append(basin)
	for j,b1 in enumerate(basins):
		for i in range(j+1,len(basins)):
			if len(b1.intersection(basins[i])) > 0:
				b1 += basins[i]
				basin[i] = set()
	sizes = sorted([ len(x) for x in basins if len(x) > 0 ], reverse = True)
	print(sizes[0]*sizes[1]*sizes[2])

		
	

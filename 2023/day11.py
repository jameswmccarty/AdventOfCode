#!/usr/bin/python

def mhd(a,b):
	return abs(a[0]-b[0])+abs(a[1]-b[1])

if __name__ == "__main__":

	# Part 1 Solution
	galaxies = set()
	with open("day11_input", "r") as infile:
		y = 0
		for line in infile.readlines():
			max_x = len(line.strip())
			for x,c in enumerate(line.strip()):
				if c == "#":
					galaxies.add((x,y))
			y += 1
	max_y = y

	xs =  { pt[0] for pt in galaxies }
	xs.add(0)
	xs.add(max_x-1)
	xs = sorted(xs)
	gx = []
	for i in range(len(xs)):
		gx.append( [p for p in galaxies if p[0] == xs[i]] )

	for i in range(1,len(xs)):
		dx = xs[i]-xs[i-1]
		if dx > 1:
			for j in range(i,len(xs)):
				gx[j] = [ (x+dx-1,y) for x,y in gx[j] ]
	galaxies = set()
	for e in gx:
		for x in e:
			galaxies.add(x)

	ys =  { pt[1] for pt in galaxies }
	ys.add(0)
	ys.add(max_y-1)
	ys = sorted(ys)
	gy = []
	for i in range(len(ys)):
		gy.append( [p for p in galaxies if p[1] == ys[i]] )

	for i in range(1,len(ys)):
		dy = ys[i]-ys[i-1]
		if dy > 1:
			for j in range(i,len(ys)):
				gy[j] = [ (x,y+dy-1) for x,y in gy[j] ]
	galaxies = set()
	for e in gy:
		for y in e:
			galaxies.add(y)

	total = 0
	galaxies = sorted(galaxies)
	for j in range(len(galaxies)):
		for i in range(j+1,len(galaxies)):
			total += mhd(galaxies[i],galaxies[j])
	print(total)

	# Part 2 Solution
	galaxies = set()
	with open("day11_input", "r") as infile:
		y = 0
		for line in infile.readlines():
			max_x = len(line.strip())
			for x,c in enumerate(line.strip()):
				if c == "#":
					galaxies.add((x,y))
			y += 1
	max_y = y

	xs =  { pt[0] for pt in galaxies }
	xs.add(0)
	xs.add(max_x-1)
	xs = sorted(xs)
	gx = []
	for i in range(len(xs)):
		gx.append( [p for p in galaxies if p[0] == xs[i]] )

	for i in range(1,len(xs)):
		dx = xs[i]-xs[i-1]
		if dx > 1:
			for j in range(i,len(xs)):
				gx[j] = [ (x+(dx-1)*(1000000-1),y) for x,y in gx[j] ]
	galaxies = set()
	for e in gx:
		for x in e:
			galaxies.add(x)

	ys =  { pt[1] for pt in galaxies }
	ys.add(0)
	ys.add(max_y-1)
	ys = sorted(ys)
	gy = []
	for i in range(len(ys)):
		gy.append( [p for p in galaxies if p[1] == ys[i]] )

	for i in range(1,len(ys)):
		dy = ys[i]-ys[i-1]
		if dy > 1:
			for j in range(i,len(ys)):
				gy[j] = [ (x,y+(dy-1)*(1000000-1)) for x,y in gy[j] ]
	galaxies = set()
	for e in gy:
		for y in e:
			galaxies.add(y)

	total = 0
	galaxies = sorted(galaxies)
	for j in range(len(galaxies)):
		for i in range(j+1,len(galaxies)):
			total += mhd(galaxies[i],galaxies[j])
	print(total) 


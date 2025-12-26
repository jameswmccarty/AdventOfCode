#!/usr/bin/python


if __name__ == "__main__":


	# Part 1 Solution

	points = []
	vent_points = dict()
	with open("day05_input","r") as infile:
		for line in infile.readlines():
			p1,p2 = line.strip().split(" -> ")
			x1,y1 = p1.strip().split(",")
			x2,y2 = p2.strip().split(",")
			points.append((int(x1),int(y1),int(x2),int(y2)))
	
	for point in points:
		x1,y1,x2,y2 = point
		if (x1==x2) ^ (y1==y2):
			x1,x2 = min(x1,x2),max(x1,x2)
			y1,y2 = min(y1,y2),max(y1,y2)
			for j in range(y1,y2+1):
				for i in range(x1,x2+1):
					if (i,j) in vent_points:
						vent_points[(i,j)] += 1
					else:
						vent_points[(i,j)] = 1
	print(sum([ x >= 2 for x in vent_points.values() ]))

	# Part 2 Solution
	for point in points:
			x1,y1,x2,y2 = point
			if (x1==x2) ^ (y1==y2):
				continue
			else:
				xspan = x2-x1
				dx = -1 if xspan < 0 else 1
				yspan = y2-y1
				dy = -1 if yspan < 0 else 1
				a, b = x1, y1
				for d in range(min(abs(xspan),abs(yspan))+1):
					if (a,b) in vent_points:
						vent_points[(a,b)] += 1
					else:
						vent_points[(a,b)] = 1
					a, b = a+dx,b+dy
	print(sum([ x >= 2 for x in vent_points.values() ]))


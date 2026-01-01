#!/usr/bin/python

#import matplotlib.pyplot as plt

# Advent of Code 2025 Day 09

def inside(i,j,k,l,x,y):
	return x > i[0] and x < k[0] and y > k[1] and y < j[1]

if __name__ == "__main__":

	pts = set()
	with open("day09_input", "r") as infile:
		for line in infile:
			x, y = map(int, line.strip().split(','))
			pts.add((x,y))
	largest = 0
	for a in pts:
		for b in pts:
			largest = max(largest, abs(a[0]-b[0]+1)*abs(a[1]-b[1]+1))
	print(largest)

	vert_cuts = set()
	horiz_cuts = set()
	pt_list = []
	xs = []
	ys = []
	with open("day09_input", "r") as infile:
		for line in infile:
			x, y = map(int, line.strip().split(','))
			pt_list.append((x,y))
			xs.append(x)
			ys.append(y)
	#plt.scatter(xs,ys)
	#plt.plot(xs,ys)
	#plt.show()
	pt_list.append(pt_list[0])
	for i in range(1, len(pt_list)):
		a = pt_list[i-1]
		b = pt_list[i]
		if a[0] == b[0]:
			vert_cuts.add(tuple(sorted((a,b))))
		else:
			horiz_cuts.add(tuple(sorted((a,b))))

	largest = 0
	seen = set()
	for a in pts:
		for b in pts:
			i = (min(a[0], b[0]), min(a[1], b[1]))
			j = (min(a[0], b[0]), max(a[1], b[1]))
			k = (max(a[0], b[0]), min(a[1], b[1]))
			l = (max(a[0], b[0]), max(a[1], b[1]))

			# cut-off boundary determined from observation of plotted polygon shape
			if not any(inside(i,j,k,l,x,y) for x,y in pts) and (i[1] >= 50147):
				largest = max(largest, (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1))
				if largest not in seen:
					x2s = [ u[0] for u in (i,j,k,l) ]
					y2s = [ u[1] for u in (i,j,k,l) ]
					#plt.plot(xs,ys)
					#plt.scatter(x2s, y2s)
					#plt.show()
					#print(largest, a, b, i, j, k, l)
					seen.add(largest)

	print(largest)

#!/usr/bin/python



class Point:

	def __init__(self, x, y, z, t):
		self.x = x
		self.y = y
		self.z = z
		self.t = t
		
	def dist(self, pt):
		return abs(self.x-pt.x)+abs(self.y-pt.y)+abs(self.z-pt.z)+abs(self.t-pt.t)
		
	def inrange(self, pt):
		if 3 >= self.dist(pt):
			return True
		return False
		
def parse_line(line):
	x,y,z,t = line.strip().split(",")
	return Point(int(x), int(y), int(z), int(t))	

if __name__ == "__main__":

	# Part 1 Solution
	
	points = []
	
	constellations = []
	
	with open("day25_input", "r") as infile:
		for line in infile.readlines():
			points.append(parse_line(line))
			
	for point in points:
		merge_idxs = set()
		for idx, constellation in enumerate(constellations):
			for sub_point in constellation:
				if sub_point.inrange(point):
					merge_idxs.add(idx)
					break
		if len(merge_idxs) == 0:
			constellations.append({point})
		else:
			merge_idxs = list(merge_idxs)
			merge_idxs.sort(reverse=True)
			new_set = { point }
			for idx in merge_idxs:
				new_set = new_set.union(constellations[idx])
			for idx in merge_idxs:
				constellations.pop(idx)
			constellations.append(new_set)
	
	print len(constellations)

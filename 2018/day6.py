#/usr/bin/python


class Point:
	
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)
		self.is_inf = False # is an outer boundry, and won't count
		self.score = 0 # for counting area
		
	def mh_dist(self, pt):
		return abs(self.x - pt.x) + abs(self.y - pt.y)


if __name__ == "__main__":

	#Part 1 Solution
	
	points = []
	with open("day6_input", "r") as infile:
		for line in infile.readlines():
			x, y = line.strip().split(", ")
			points.append(Point(x, y))
			
	# locate boundary points
	xcords = []
	ycords = []
	for point in points:
		xcords.append(point.x) # all x coordinates
		ycords.append(point.y) # all y coordinates
	minx = min(xcords)
	maxx = max(xcords)
	miny = min(ycords)
	maxy = max(ycords)
	for point in points:
		# exclude all that lie on boundary
		if point.x == minx or point.x == maxx or point.y == miny or point.y == maxy:
			point.is_inf = True

	# build a 2D grid to contain all available points
	grid = [[None] * maxx for i in range(maxy)]
		
	for i in range(minx, maxx):
		for j in range(miny, maxy):
			ranges = []
			for point in points:
				# find each grid point's distance from set of all points
				ranges.append((point.mh_dist(Point(i, j)), point))
			ranges.sort(key = lambda x : x[0]) # locate closest point
			if ranges[0][0] == ranges[1][0]: # equal distant to two points
				grid[j][i] = None
			else:
				grid[j][i] = ranges[0][1] # assign closest point
				

	# find point that owns the most grid area
	max_score = 0
	best_point = None
	for i in range(minx, maxx):
		for j in range(miny, maxy):
			if grid[j][i] is not None:
				if grid[j][i].is_inf == False:
					grid[j][i].score += 1
					if grid[j][i].score > max_score:
						max_score = grid[j][i].score
						best_point = grid[j][i]
	
	print best_point.score
	
	# Part 2 Solution
	
	# build a 2D grid to contain all available points
	grid = [[None] * maxx for i in range(maxy)]
		
	for i in range(minx, maxx):
		for j in range(miny, maxy):
			total_dist = 0
			for point in points:
				# sum each grid point's distance from set of all points
				total_dist += point.mh_dist(Point(i, j))
			if total_dist < 10000: # count as in range
				grid[j][i] = 1
			else:
				grid[j][i] = 0
	
	safe_area = 0
	for i in range(minx, maxx):
		for j in range(miny, maxy):
			safe_area += grid[j][i]
			
	print safe_area
	



		

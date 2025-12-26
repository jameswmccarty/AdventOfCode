#!/usr/bin/python



sensors = set()
beacons = set()
exclusion_area = set()
dist_measures = dict()

def dist(p1,p2):
	x1,y1 = p1
	x2,y2 = p2
	return abs(x2-x1)+abs(y2-y1)

# determine distance of a given point to nearest sensor
# return number of steps and beacon found
def bfs(pt):
	q = []
	q.append((0,pt))
	seen = set()
	while len(q) > 0:
		steps,pt = q.pop(0)
		if pt in sensors:
			return (steps,pt)
		else:
			x,y = pt
			for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
				next = (x+dx,y+dy)
				if next not in seen:
					seen.add(next)
					q.append((steps+1,next))
	return (float('inf'),None)

def in_range_of_any_sensor(pt):
	for s in sensors:
		if dist(pt,s) <= dist_measures[s]:
			return True
	return False

# Given a sensors, provide an x min and max for a given y
# where a beacon cannot be present, or None if no overlap
# of range
def overlap_range(scan_y,sensor):
	x,y   = sensor
	reach = dist_measures[sensor]
	dy = dist(sensor,(x,scan_y))
	if abs(dy) >= reach:
		return None
	else:
		dy -= reach
		return [x-abs(dy),x+abs(dy)]

# with assistance from https://www.geeksforgeeks.org/merging-intervals/
def mergeIntervals(intervals):
	# Sort the array on the basis of start values of intervals.
	intervals.sort()
	stack = []
	# insert first interval into stack
	stack.append(intervals[0])
	for i in intervals[1:]:
		# Check for overlapping interval,
		# if interval overlap
		if stack[-1][0] <= i[0] <= stack[-1][-1]:
			stack[-1][-1] = max(stack[-1][-1], i[-1])
		else:
			stack.append(i)
	return stack

def parse_line(line):
	s,b = line.split(':')
	s,b = s.split(' at ')[1],b.split(' at ')[1]
	sx,sy = s.split(', ')
	bx,by = b.split(', ')
	s = (int(sx.replace('x=','')),int(sy.replace('y=','')))
	b = (int(bx.replace('x=','')),int(by.replace('y=','')))
	dist_measures[s] = dist(s,b)
	sensors.add(s)
	beacons.add(b)

if __name__ == "__main__":

	# Part 1 Solution
	with open('day15_input','r') as infile:
		for line in infile.readlines():
			parse_line(line.strip())
	scan_y = 2000000
	"""
	error_bars = max(dist_measures.values())
	min_x = min(min([ x[0] for x in beacons ]),min([ x[0] for x in sensors])) - error_bars
	max_x = max(max([ x[0] for x in beacons ]),max([ x[0] for x in sensors])) + error_bars
	cannot_contain = 0
	for x in range(min_x,max_x):
		if in_range_of_any_sensor((x,scan_y)):# and (x,scan_y) not in beacons:
			cannot_contain += 1
	print(cannot_contain)
	"""
	ranges = [ overlap_range(scan_y,sensor) for sensor in sensors ]
	ranges = [ x for x in ranges if x != None ]
	compressed_ranges = mergeIntervals(ranges)
	total = 0
	for r in compressed_ranges:
		total += r[1]+1 - r[0]
	print(total-len( [ b for b in beacons if b[1] == scan_y ] ))

	# Part 2 Solution
	for y in range(4000000,-1,-1):
		ranges = [ overlap_range(y,sensor) for sensor in sensors ]
		ranges = [ x for x in ranges if x != None ]
		compressed_ranges = mergeIntervals(ranges)
		if len(compressed_ranges) > 1:
			print((compressed_ranges[1][0]-1)*4000000+y)
			break


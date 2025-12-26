#!/usr/bin/python

from collections import deque

class MapRange:

	def __init__(self,title):
		title = title.replace("map:",'')
		takes,goes_to = title.split("-to-")
		self.takes = takes.strip()
		self.goes_to = goes_to.strip()
		self.ranges = []

	def add_range(self,line):
		self.ranges.append(tuple(int(x) for x in line.strip().split()))
		self.ranges = sorted(self.ranges,key=lambda x:x[1])

	def in_range(self,num):
		for dest,source,ran in self.ranges:
			if num >= source and num <= source+ran:
				return (num-source)+dest
		return num

	def transform_range(self,start,delta):
		new_ranges = []
		pos  = start
		high_bound = start+delta
		# interval is low,high,new base
		intervals = [ (x[1],x[1]+x[2],x[0]) for x in self.ranges ]
		while intervals and pos < high_bound:
			base,ceil,new_base = intervals.pop(0)
			if pos < base:
				dx = min(base,high_bound)-pos
				new_ranges.append((pos,dx))
				pos += dx
			if pos >= base and pos < ceil:
				sx = pos - base
				dx = min(ceil,high_bound)-pos
				new_ranges.append((sx+new_base,dx))
				pos += dx
		if pos < high_bound:
			new_ranges.append((pos,high_bound-pos+1))
		return new_ranges

if __name__ == "__main__":

	# Part 1 Solution
	maps = dict()
	with open("day05_input", "r") as infile:
		current_map = None
		for line in infile:
			if line.strip() == '':
				if current_map != None:
					maps[current_map.takes] = current_map
			elif "seeds:" in line:
				seeds = [ int(x) for x in line.lstrip("seeds:").split() ]
			elif "map:" in line:
				current_map = MapRange(line)
			else:
				current_map.add_range(line)
		if current_map != None:
			maps[current_map.takes] = current_map

	min_loc = float("inf")
	q = deque()
	for entry in seeds:
		q.append((entry,'seed'))
	while q:
		value,location = q.popleft()
		if location == "location":
			min_loc = min(min_loc,value)
		else:
			q.append((maps[location].in_range(value),maps[location].goes_to))
	print(min_loc)

	# Part 2 Solution
	min_loc = float("inf")
	q = deque()
	while seeds:
		start = seeds.pop(0)
		delta = seeds.pop(0)
		q.append(((start,delta),'seed'))
	while q:
		value,location = q.popleft()
		if location == "location":
			min_loc = min(min_loc,value[0])
		else:
			for entry in maps[location].transform_range(value[0],value[1]):
				q.append((entry,maps[location].goes_to))
	print(min_loc)

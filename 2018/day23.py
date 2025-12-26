#!/usr/bin/python

import heapq
import random


class Bot:

	def __init__(self, x, y, z, r):
		self.x = x
		self.y = y
		self.z = z
		self.r = r
		
	def dist(self, bot):
		return abs(self.x-bot.x)+abs(self.y-bot.y)+abs(self.z-bot.z)
		
	def inrange(self, bot):
		if self.r >= self.dist(bot):
			return True
		return False

	def r_dist(self, x, y, z):
		if self.r >= (abs(self.x-x)+abs(self.y-y)+abs(self.z-z)):
			return True
		return False
		
def parse_line(line):
	# pos=<0,0,0>, r=4
	pos, r = line.strip().split(">, ")
	r = r.replace("r=",'')
	x,y,z = pos.split(",")
	x = x.replace("pos=<",'')
	return Bot(int(x), int(y), int(z), int(r))

def pt_score(bots, x, y, z):
	score = 0
	for bot in bots:
		if bot.r_dist(x,y,z):
			score += 1
	return -1*score	

if __name__ == "__main__":

	# Part 1 Solution
	
	bots = []
	
	with open("day23_input", "r") as infile:
		for line in infile.readlines():
			bots.append(parse_line(line))
			
	bots.sort(key=lambda x: x.r, reverse=True)
	
	count = 1
	for i in range(1,len(bots)):
		if bots[0].inrange(bots[i]):
			count += 1
	print count
	

	# Part 2 Solution

	x_min = float('inf')
	x_max = 0
	y_min = float('inf')
	y_max = 0
	z_min = float('inf')
	z_max = 0

	most_bots = 0
	min_dist = float('inf')

	for bot in bots:
		x_min = min(x_min, bot.x)
		x_max = max(x_max, bot.x)
		y_min = min(y_min, bot.y)
		y_max = max(y_max, bot.y)
		z_min = min(z_min, bot.z)
		z_max = max(z_max, bot.z)

	ranx = x_max - x_min
	rany = y_max - y_min
	ranz = z_max - z_min
	bran = min(ranx,rany,ranz)
	bran *= 0.2
	bran = int(bran)	

	best = float('inf')
	best_mh = float('inf')
	h = []

	# Binary search the cubic space
	
	heapq.heappush(h, (pt_score(bots, (x_min+x_max)/2, (y_min+y_max)/2, (z_min+z_max)/2), x_min, x_max, y_min, y_max, z_min, z_max))

	for i in xrange(2000): # shotgun many random starting points, with limited search boxes
		b_x = int(random.uniform(x_min*1.2, x_max*1.2))
		b_y = int(random.uniform(y_min*1.2, y_max*1.2))
		b_z = int(random.uniform(z_min*1.2, z_max*1.2))
		heapq.heappush(h, (pt_score(bots, b_x, b_y, b_z), b_x-bran, b_x+bran,b_y-bran, b_y+bran,b_z-bran, b_z+bran))
	for bot in bots: # also start at bot centers, seaching in range
		b_x = bot.x
		b_y = bot.y
		b_z = bot.z
		bran = int(bot.r)
		heapq.heappush(h, (pt_score(bots, b_x, b_y, b_z), b_x-bran, b_x+bran,b_y-bran, b_y+bran,b_z-bran, b_z+bran))
	while len(h) > 0 and h[0][0] <= best:
		current_score, x_min, x_max, y_min, y_max, z_min, z_max = heapq.heappop(h)
		x = (x_min + x_max) / 2
		y = (y_min + y_max) / 2
		z = (z_min + z_max) / 2
		if current_score <= best:
			if current_score < best:
				best = current_score
				best_mh = abs(x)+abs(y)+abs(z)
			best_mh = min(best_mh,abs(x)+abs(y)+abs(z)) 
			heapq.heappush(h, (pt_score(bots, (x+x_max) / 2, (y+y_max) / 2, (z+z_max) / 2), x, x_max, y, y_max, z, z_max)) #111
			heapq.heappush(h, (pt_score(bots, (x+x_max) / 2, (y+y_max) / 2, (z+z_min) / 2), x, x_max, y, y_max, z_min, z)) #110
			heapq.heappush(h, (pt_score(bots, (x+x_max) / 2, (y+y_min) / 2, (z+z_max) / 2), x, x_max, y_min, y, z, z_max)) #101
			heapq.heappush(h, (pt_score(bots, (x+x_max) / 2, (y+y_min) / 2, (z+z_min) / 2), x, x_max, y_min, y, z_min, z)) #100
			heapq.heappush(h, (pt_score(bots, (x+x_min) / 2, (y+y_max) / 2, (z+z_max) / 2), x_min, x, y, y_max, z, z_max)) #011
			heapq.heappush(h, (pt_score(bots, (x+x_min) / 2, (y+y_max) / 2, (z+z_min) / 2), x_min, x, y, y_max, z_min, z)) #010
			heapq.heappush(h, (pt_score(bots, (x+x_min) / 2, (y+y_min) / 2, (z+z_max) / 2), x_min, x, y_min, y, z, z_max)) #001
			heapq.heappush(h, (pt_score(bots, (x+x_min) / 2, (y+y_min) / 2, (z+z_min) / 2), x_min, x, y_min, y, z_min, z)) #000

	#print best, best_mh, x, y, z

	# Simulated annealing technique to escape local maxima

	delta = 2**23
	cooling = 0.95
	seen = set()

	while delta > 0:
		seen = set()
		h = []
		seen.add((x,y,z))
		heapq.heappush(h, (pt_score(bots, x, y, z), x, y, z))
		heapq.heappush(h, (pt_score(bots, x+delta, y, z), x+delta, y, z))
		heapq.heappush(h, (pt_score(bots, x-delta, y, z), x-delta, y, z))
		heapq.heappush(h, (pt_score(bots, x, y+delta, z), x, y+delta, z))
		heapq.heappush(h, (pt_score(bots, x, y-delta, z), x, y-delta, z))
		heapq.heappush(h, (pt_score(bots, x, y, z+delta), x, y, z+delta))
		heapq.heappush(h, (pt_score(bots, x, y, z-delta), x, y, z-delta))
		heapq.heappush(h, (pt_score(bots, x+delta, y+delta, z+delta), x+delta, y+delta, z+delta))
		heapq.heappush(h, (pt_score(bots, x+delta, y+delta, z-delta), x+delta, y+delta, z-delta))
		heapq.heappush(h, (pt_score(bots, x+delta, y-delta, z+delta), x+delta, y-delta, z+delta))
		heapq.heappush(h, (pt_score(bots, x+delta, y-delta, z-delta), x+delta, y-delta, z-delta))
		heapq.heappush(h, (pt_score(bots, x-delta, y+delta, z+delta), x-delta, y+delta, z+delta))
		heapq.heappush(h, (pt_score(bots, x-delta, y+delta, z-delta), x-delta, y+delta, z-delta))
		heapq.heappush(h, (pt_score(bots, x-delta, y-delta, z+delta), x-delta, y-delta, z+delta))
		heapq.heappush(h, (pt_score(bots, x-delta, y-delta, z-delta), x-delta, y-delta, z-delta))
		while len(h) > 0 and h[0][0] <= best:
			current_score, x, y, z = heapq.heappop(h)
			if (x,y,z) not in seen:
				seen.add((x,y,z))
				#print current_score, x, y, z
				if current_score <= best:
					if current_score < best:
						best = current_score
						best_mh = abs(x)+abs(y)+abs(z)
						delta = 2**23 #int(delta/cooling)
						break
					best_mh = min(best_mh,abs(x)+abs(y)+abs(z))
				heapq.heappush(h, (pt_score(bots, x+delta, y, z), x+delta, y, z))
				heapq.heappush(h, (pt_score(bots, x-delta, y, z), x-delta, y, z))
				heapq.heappush(h, (pt_score(bots, x, y+delta, z), x, y+delta, z))
				heapq.heappush(h, (pt_score(bots, x, y-delta, z), x, y-delta, z))
				heapq.heappush(h, (pt_score(bots, x, y, z+delta), x, y, z+delta))
				heapq.heappush(h, (pt_score(bots, x, y, z-delta), x, y, z-delta))
				heapq.heappush(h, (pt_score(bots, x+delta, y+delta, z+delta), x+delta, y+delta, z+delta))
				heapq.heappush(h, (pt_score(bots, x+delta, y+delta, z-delta), x+delta, y+delta, z-delta))
				heapq.heappush(h, (pt_score(bots, x+delta, y-delta, z+delta), x+delta, y-delta, z+delta))
				heapq.heappush(h, (pt_score(bots, x+delta, y-delta, z-delta), x+delta, y-delta, z-delta))
				heapq.heappush(h, (pt_score(bots, x-delta, y+delta, z+delta), x-delta, y+delta, z+delta))
				heapq.heappush(h, (pt_score(bots, x-delta, y+delta, z-delta), x-delta, y+delta, z-delta))
				heapq.heappush(h, (pt_score(bots, x-delta, y-delta, z+delta), x-delta, y-delta, z+delta))
				heapq.heappush(h, (pt_score(bots, x-delta, y-delta, z-delta), x-delta, y-delta, z-delta))
		#print best, best_mh, x, y, z, delta
		delta = min(int(delta * cooling), delta-1)

	# Final exhaustive search of local region

	x_min = x - 10
	x_max = x + 10
	y_min = y - 10
	y_max = y + 10
	z_min = z - 10
	z_max = z + 10

	for x in xrange(x_min, x_max):
		for y in xrange(y_min, y_max):
			for z in xrange(z_min, z_max):
				l_count = 0				
				for bot in bots:
					if bot.r_dist(x,y,z):
						l_count += 1
				if l_count == most_bots and abs(x)+abs(y)+abs(z) < min_dist:
					min_dist = abs(x)+abs(y)+abs(z)
				elif l_count > most_bots:
					most_bots = l_count
					min_dist = abs(x)+abs(y)+abs(z)
	print min_dist
				

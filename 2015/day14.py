#!/usr/bin/python



class Reindeer:

	def __init__(self, fly, rest, speed):
		self.fly = int(fly)
		self.rest = int(rest)
		self.speed = int(speed)
		self.interval = self.fly + self.rest
		self.int_dist = self.speed * self.fly
		self.points = 0
		
	def dist_t(self, t):
		return (t/self.interval)*self.int_dist + min(self.fly, t%self.interval)*self.speed

if __name__ == "__main__":

	deers = []

	# Part 1 Solution
	with open("day14_input", "r") as infile:
		for line in infile.readlines():
			line = line.split(" ")
			deers.append(Reindeer(line[6], line[-2], line[3]))
			
	print max(x.dist_t(2503) for x in deers)
	
	# Part 2 Solution
	for i in range(1,2503):
		lead_pos = max(x.dist_t(i) for x in deers)
		for x in deers:
			if lead_pos == x.dist_t(i):
				x.points += 1
	print max(x.points for x in deers)
		

#!/usr/bin/python


class Vect:

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	# Manhattan distance
	def dist(self, pos):
		return abs(self.x-pos.x)+abs(self.y-pos.y)+abs(self.z-pos.z)
		
	# Simple vector addition
	def sum(self, pos):
		self.x += pos.x
		self.y += pos.y
		self.z += pos.z
		
	def coord(self):
		return str(self.x) + "," + str(self.y) + "," + str(self.z)
		
class Particle:


	# take a line from the input file, parse and create particle
	def __init__(self, line, line_num):
		line = line.split(">, ")
		pos_line = line[0].replace("p=<", '')
		pos_line = pos_line.split(",")
		self.pos = Vect(int(pos_line[0]),int(pos_line[1]), int(pos_line[2]))
		vel_line = line[1].replace("v=<", '')
		vel_line = vel_line.split(",")
		self.vel = Vect(int(vel_line[0]),int(vel_line[1]), int(vel_line[2]))
		acc_line = line[2].replace("a=<", '')
		acc_line = acc_line.replace(">", '')
		acc_line = acc_line.split(",")
		self.acc = Vect(int(acc_line[0]),int(acc_line[1]), int(acc_line[2]))
		self.id_num = line_num
		self.collided = False
	
	# distance from the origin <0,0,0>
	def dist(self):
		return self.pos.dist(Vect(0,0,0))
		
	def tick(self):
		self.vel.sum(self.acc)
		self.pos.sum(self.vel)
		
	def collide(self, p):
		if p != self and self.pos.x == p.pos.x and self.pos.y == p.pos.y and self.pos.z == p.pos.z:
			self.collided = True
			p.collided = True		

if __name__ == "__main__":

	# Part 1 Solution

	particles = []

	with open("day20_input", "r") as infile:
		row_idx = 0
		for line in infile.readlines():
			particles.append(Particle(line, row_idx))
			row_idx += 1
	
	for i in range(1000):
		for particle in particles:
			particle.tick()
	
	particles.sort(key=lambda x : x.dist())
	
	print particles[0].id_num
	
	# Part 2 Solution

	particles = [] # Reset

	with open("day20_input", "r") as infile:
		row_idx = 0
		for line in infile.readlines():
			particles.append(Particle(line, row_idx))
			row_idx += 1
			

	
	for i in range(50):
		occupied = {}
		for particle in particles:
			particle.tick()
			if particle.pos.coord() in occupied:
				occupied[particle.pos.coord()].add(particle)
			else:
				occupied[particle.pos.coord()] = {particle}
		if len(occupied) < len(particles):
			rmv = [ occupied[x] for x in occupied if len(occupied[x]) > 1 ]
			rmv = [ x for y in rmv for x in y ]
			for item in rmv:
				particles.remove(item)
				
	print len(particles)
	
		

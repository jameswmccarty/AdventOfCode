#!/usr/bin/python

from functools import reduce
from math import gcd

def lcm(a, b):
	return int(a * b / gcd(a, b))

def lcms(*numbers):
	return reduce(lcm, numbers)

class Body:

	def __init__(self, x, y, z):
		self.pos = [int(x),int(y),int(z)]
		self.vel = [0,0,0]
		self.delta = [0,0,0]

	def comp(self, moon):
		for i in range(3):
			if self.pos[i] < moon.pos[i]:
				self.delta[i] += 1
				moon.delta[i] -= 1
			elif self.pos[i] > moon.pos[i]:
				self.delta[i] -= 1
				moon.delta[i] += 1

	def delta_v(self):
		for i in range(3):
			self.vel[i] += self.delta[i]
		self.delta = [0, 0, 0]
		for i in range(3):
			self.pos[i] += self.vel[i]

	def PE(self):
		return sum( abs(x) for x in self.pos )

	def KE(self):
		return sum( abs(x) for x in self.vel )

	def energy(self):
		return self.PE() * self.KE()

	def state(self):
		return hash(tuple(self.pos + self.vel))

	def i_state(self, i):
		return tuple([self.pos[i],self.vel[i]])

def parse(l):
	l = l.replace('<x=','').replace('>','')
	l = l.split(', ')
	return Body(l[0], l[1].replace('y=',''),l[2].replace('z=',''))

def M_state(bodies, i):
	state = tuple( x.i_state(i) for x in bodies )
	return hash(state)

if __name__ == "__main__":

	moons = []

	# Part 1 Solution
	with open("day12_input", 'r') as infile:
		for line in infile.readlines():
			moons.append(parse(line.strip()))

	for idx in range(1000):
		#for i in range(len(moons)):
		#	print(moons[i].pos, moons[i].vel)
		#print("------")
		for i in range(len(moons)):
			for j in range(i,len(moons)):
					moons[i].comp(moons[j])
		for i in range(len(moons)):
			moons[i].delta_v()	

	print(sum( x.energy() for x in moons ))

	# Part 2 Solution
	moons = []
	x_seen = set()
	y_seen = set()
	z_seen = set()
	x_0 = None
	y_0 = None
	z_0 = None
	x_cycle = None
	y_cycle = None
	z_cycle = None
	with open("day12_input", 'r') as infile:
		for line in infile.readlines():
			moons.append(parse(line.strip()))

	x_seen.add(M_state(moons,0))
	y_seen.add(M_state(moons,1))
	z_seen.add(M_state(moons,2))

	for i in range(len(moons)):
		for j in range(i,len(moons)):
			moons[i].comp(moons[j])
	for i in range(len(moons)):
		moons[i].delta_v()	

	gen = 1
	while x_cycle == None or y_cycle == None or z_cycle == None:
		x_seen.add(M_state(moons,0))
		y_seen.add(M_state(moons,1))
		z_seen.add(M_state(moons,2))
		for i in range(len(moons)):
			for j in range(i,len(moons)):
				moons[i].comp(moons[j])
		for i in range(len(moons)):
			moons[i].delta_v()
		if M_state(moons,0) in x_seen and x_cycle == None and x_0 != None:
			x_cycle = gen - x_0
		if M_state(moons,1) in y_seen and y_cycle == None and y_0 != None:
			y_cycle = gen - y_0
		if M_state(moons,2) in z_seen and z_cycle == None and z_0 != None:
			z_cycle = gen - z_0
		if M_state(moons,0) in x_seen and x_0 == None:
			x_0 = gen
			x_seen = set()
		if M_state(moons,1) in y_seen and y_0 == None:
			y_0 = gen
			y_seen = set()
		if M_state(moons,2) in z_seen and z_0 == None:
			z_0 = gen
			z_seen = set()
		gen += 1
	print(lcms(x_cycle, y_cycle, z_cycle))


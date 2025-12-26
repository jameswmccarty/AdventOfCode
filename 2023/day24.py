#!/usr/bin/python

from z3 import *

class Hailstone:

	def __init__(self,line):
		pos,vel = line.split(' @ ')
		self.x,self.y,self.z    = [ int(x) for x in pos.split(', ') ]
		self.dx,self.dy,self.dz = [ int(x) for x in vel.split(', ') ]
		self.m = self.dy / self.dx
		self.b = self.y - self.m*self.x
		self.M = self.m ** -1
		self.A = self.m * self.M
		self.B = -self.M
		self.C = self.b * self.M
		self.A /= self.B
		self.C /= self.B
		self.B /= self.B
	
	def intersects_2d(self,b):
		x_num = self.B*b.C-b.B*self.C
		x_den = self.A*b.B-b.A*self.B
		
		y_num = b.A*self.C-self.A-b.C
		y_den = self.A*b.B-b.A*self.B
		
		if x_den == 0 or y_den == 0:
			return None
		
		return (x_num/x_den,y_num/y_den)
	
	def line_at_x(self,x):
		return x*self.m+self.b
	
	def t_at_pt(self,pt):
		x,y = pt
		return (x - self.x) / self.dx, (y - self.y) / self.dy


if __name__ == "__main__":

	stones = []

	# Part 1 Solution
	with open("day24_input", "r") as infile:
		for line in infile:
			stones.append(Hailstone(line.strip()))

	low_bound  = 200000000000000
	high_bound = 400000000000000

	crossings = 0
	for i in range(0,len(stones)):
		for j in range(i,len(stones)):
			result = stones[i].intersects_2d(stones[j])
			if result != None:
				cross_pt = (result[0],stones[i].line_at_x(result[0]))
				a_times  = stones[i].t_at_pt(cross_pt)
				b_times  = stones[j].t_at_pt(cross_pt)
				if a_times[0] > 0 and a_times[1] > 0 and b_times[0] > 0 and b_times[1] > 0:
					if cross_pt[0] >= low_bound and cross_pt[0] <= high_bound and cross_pt[1] >= low_bound and cross_pt[1] <= high_bound:
						crossings += 1
	print(crossings)			


	# Part 2 Solution
	x,y,z,dx,dy,dz,t1,t2,t3,t4 = Reals('x y z dx dy dz t1 t2 t3 t4')
	s = Solver()
	
	s.add(x>0)
	s.add(y>0)
	s.add(z>0)
	
	ts = [t1,t2,t3]
	for i in range(len(ts)):
		s.add(x+(dx*ts[i]) == stones[i].x+ts[i]*stones[i].dx)
		s.add(y+(dy*ts[i]) == stones[i].y+ts[i]*stones[i].dy)
		s.add(z+(dz*ts[i]) == stones[i].z+ts[i]*stones[i].dz)

	# Check for satisfiability
	if s.check() == sat:
	    model = s.model()
	    print(sum([model[x].as_long(),model[y].as_long(),model[z].as_long()]))
	else:
	    print('No solution found.')
	
	



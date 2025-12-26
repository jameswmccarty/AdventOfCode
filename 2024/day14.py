#!/usr/bin/python

# Advent of Code 2024 Day 14

x_dim=101
y_dim=103

def pt_at_t_and_q(bot,t):
	x,y,dx,dy = bot
	nx,ny = (x+dx*t)%x_dim, (y+dy*t)%y_dim
	if nx < x_dim//2 and ny < y_dim//2:
		return nx, ny, 1
	if nx > x_dim//2 and ny < y_dim//2:
		return nx, ny, 2
	if nx < x_dim//2 and ny > y_dim//2:
		return nx, ny, 3
	if nx > x_dim//2 and ny > y_dim//2:
		return nx, ny, 4
	return nx, ny, 0

def pretty_print(pos_list):
	pos_set = { (x,y) for x,y,q in pos_list }
	for j in range(y_dim):
		for i in range(x_dim):
			if (i,j) in pos_set:
				print('X',end='')
			else:
				print('.',end='')
		print()

if __name__ == "__main__":

	# Part 1 Solution
	bots = []
	with open("day14_input", "r") as infile:
		for line in infile:
			p,v = line.strip().split()
			x,y = p.split(',')
			dx,dy = v.split(',')
			bots.append((int(x.lstrip('p=')),int(y),int(dx.lstrip('v=')),int(dy)))

	t100_pos = [ pt_at_t_and_q(b,100) for b in bots ]

	q1 = len([pt for pt in t100_pos if pt[2] == 1])
	q2 = len([pt for pt in t100_pos if pt[2] == 2])
	q3 = len([pt for pt in t100_pos if pt[2] == 3])
	q4 = len([pt for pt in t100_pos if pt[2] == 4])

	print(q1*q2*q3*q4)
	# Part 2 Solution

	#seen = set()
	#i = 0
	#while True:
	#	pos = repr([ pt_at_t_and_q(b,i) for b in bots ])
	#	print(pos)
	#	i += 1
	#	if hash(pos) in seen:
	#		print(i)
	#		exit()
	#	seen.add(hash(pos))

	# half-split cycle size

	for i in range(7803,10404):
		pos = [ pt_at_t_and_q(b,i) for b in bots ]
		print(i)
		print(pretty_print(pos))

#!/usr/bin/python

rope = [ (0,0) for _ in range(10) ] # 10 element rope
p1_visited   = set() # 2nd knot in rope (or rope of length 2)
p2_visited   = set() # 10th knot

def exec_move(move):
	global rope
	move_dir, steps = move.split(' ')
	for _ in range(int(steps)):
		if move_dir == 'R':
			rope[0] = (rope[0][0]+1,rope[0][1])
		elif move_dir == 'L':
			rope[0] = (rope[0][0]-1,rope[0][1])
		elif move_dir == 'U':
			rope[0] = (rope[0][0],rope[0][1]-1)
		elif move_dir == 'D':
			rope[0] = (rope[0][0],rope[0][1]+1)
		for i in range(1,len(rope)):
			x1,y1 = rope[i-1] # lead knot
			x2,y2 = rope[i]   # next knot
			delta = (x2-x1,y2-y1)
			#If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction
			# Direction of motion for the next knot remains the same
			if (abs(delta[0]) == 2 and delta[1] == 0) or (abs(delta[1]) == 2 and delta[0] == 0):
				dx,dy = delta[0]//2,delta[1]//2
				rope[i] = (x2-dx,y2-dy)
			elif abs(delta[0]) >= 2 or abs(delta[1]) >= 2:
			#Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up
			# This may change the direction of motion for the next knot
				dx,dy = delta[0]//abs(delta[0]),delta[1]//abs(delta[1])
				rope[i] = (x2-dx,y2-dy)
			else:
				#No movement down the rest of the rope
				break
		p1_visited.add(rope[1])
		p2_visited.add(rope[-1])

if __name__ == "__main__":

	# Part 1 Solution
	p1_visited.add(rope[1])
	p2_visited.add(rope[-1])
	with open("day09_input","r") as infile:
		for line in infile.readlines():
			exec_move(line.strip())
	print(len(p1_visited))

	# Part 2 Solution
	print(len(p2_visited))

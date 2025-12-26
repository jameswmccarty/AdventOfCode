#!/usr/bin/python

pad = [	[1,2,3],
		[4,5,6],
		[7,8,9]]

pad2 = [[0  ,0  ,'1',0  ,0  ],
		[0  ,'2','3','4',0  ],
		['5','6','7','8','9'],
		[0  ,'A','B','C',0  ],
		[0  ,0  ,'D',0  ,0  ]]

		
pos = (1,1) # the '5'

pos2 = (2,0) # the '5'

def move(char):
	global pos
	if char == 'U':
		pos = (max(0,pos[0]-1),pos[1])
	elif char == 'D':
		pos = (min(2,pos[0]+1),pos[1])
	elif char == 'L':
		pos = (pos[0],max(0,pos[1]-1))
	elif char == 'R':
		pos = (pos[0],min(2,pos[1]+1))

def move2(char):
	global pos2
	if char == 'U':
		n_pos = (max(0,pos2[0]-1),pos2[1])
	elif char == 'D':
		n_pos = (min(4,pos2[0]+1),pos2[1])
	elif char == 'L':
		n_pos = (pos2[0],max(0,pos2[1]-1))
	elif char == 'R':
		n_pos = (pos2[0],min(4,pos2[1]+1))
	if pad2[n_pos[0]][n_pos[1]] != 0:
		pos2 = n_pos
		
if __name__ == "__main__":

	# Part 1 Solution
	
	code = ''
	
	with open("day2_input", "r") as infile:
		for line in infile.readlines():
			for char in line.strip():
				move(char)
			code += str(pad[pos[0]][pos[1]])
	print code
	
	# Part 2 Solution
	
	code = ''
	
	with open("day2_input", "r") as infile:
		for line in infile.readlines():
			for char in line.strip():
				move2(char)
			code += str(pad2[pos2[0]][pos2[1]])
	print code
	

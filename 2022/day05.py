#!/usr/bin/python

if __name__ == "__main__":

	stacks = []
	
	def enque(line):
		global stacks
		if len(stacks) == 0:
			stacks = [ list() for _ in range(len(line)//4+1) ]
		for i in range(1,len(line)-1,4):
			if line[i] != ' ':
				stacks[i//4].append(line[i])
	
	def execute_single_move(line):
		line = line.split(' ')
		src = int(line[3])-1
		dst = int(line[5])-1
		for i in range(int(line[1])):
			stacks[dst].append(stacks[src].pop())

	def execute_multi_move(line):
		global stacks
		line = line.split(' ')
		src = int(line[3])-1
		dst = int(line[5])-1
		sub_stack = stacks[src][-int(line[1]):]
		stacks[src] = stacks[src][0:len(stacks[src])-int(line[1])]
		stacks[dst] += sub_stack

	# general method -- use slices vice calls to push/pop
	# not used
	def stack_move(line,retainOrder=False):
		global stacks
		line = line.split(' ')
		src = int(line[3])-1
		dst = int(line[5])-1
		sub_stack = stacks[src][-int(line[1]):]
		if not retainOrder:
			sub_stack = sub_stack[::-1]
		stacks[src] = stacks[src][0:len(stacks[src])-int(line[1])]
		stacks[dst] += sub_stack		


	# Part 1 Solution
	with open("day05_input", "r") as infile:
		for line in infile.readlines():
			if '[' in line:
				enque(line.strip('\n'))
			elif line.strip() == '':
				for stack in stacks:
					stack.reverse()
			elif 'move' in line:
				execute_single_move(line.strip())
			else:
				continue
	print(''.join( [ x[-1] for x in stacks ] ))

	# Part 2 Solution
	stacks = []
	with open("day05_input", "r") as infile:
		for line in infile.readlines():
			if '[' in line:
				enque(line.strip('\n'))
			elif line.strip() == '':
				for stack in stacks:
					stack.reverse()
			elif 'move' in line:
				execute_multi_move(line.strip())
			else:
				continue
	print(''.join( [ x[-1] for x in stacks ] ))

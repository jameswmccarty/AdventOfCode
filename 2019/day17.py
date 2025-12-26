#!/usr/bin/python


class IntPuterVM:
	
	def __init__(self, memory):
		self.mem = memory
		self.mem += [0] * 5000
		self.last_out = None
		self.prog_in = []
		self.halted = False
		self.blocked = True
		self.ip_state = 0
		self.base = 0

	def buffer_read(self, i):
		self.prog_in.append(i)
		self.blocked = False

	def ascii_readln(self, cmd):
		for char in cmd:
			vm.buffer_read(ord(char))
		vm.buffer_read(10)

	def run(self):
		ip = self.ip_state
		while True:
			A = None
			B = None
			C = None
			d_ip = None
			ip_updated = False
			op = self.mem[ip]
			modes, opcode = str(op)[:-2], int(str(op)[-2:])
			if opcode == 99: # Halt
				self.halted = True
				return
			if opcode == 1: # res = C + B
				d_ip = 4
				if modes == '':
					self.mem[self.mem[ip+3]] = self.mem[self.mem[ip+1]] + self.mem[self.mem[ip+2]]
				else:
					if modes[-1] == '1':
						C = self.mem[ip+1]
					elif modes[-1] == '2':
						C = self.mem[self.base+self.mem[ip+1]]
					elif modes[-1] == '0':
						C = self.mem[self.mem[ip+1]]
					modes = modes[:-1]
					if modes == '':
						modes = '0'
					if modes[-1] == '1':
						B = self.mem[ip+2]
					elif modes[-1] == '2':
						B = self.mem[self.base+self.mem[ip+2]]
					elif modes[-1] == '0':
						B = self.mem[self.mem[ip+2]]
					modes = modes[:-1]
					if modes == '' or modes[-1] == '0':
						self.mem[self.mem[ip+3]] = C + B
					elif modes == '2':
						self.mem[self.base+self.mem[ip+3]] = C + B
			elif opcode == 2: # res = C * B
				d_ip = 4
				if modes == '':
					self.mem[self.mem[ip+3]] = self.mem[self.mem[ip+1]] * self.mem[self.mem[ip+2]]
				else:
					if modes[-1] == '1':
						C = self.mem[ip+1]
					elif modes[-1] == '2':
						C = self.mem[self.base+self.mem[ip+1]]
					elif modes[-1] == '0':
						C = self.mem[self.mem[ip+1]]
					modes = modes[:-1]
					if modes == '':
						modes = '0'
					if modes[-1] == '1':
						B = self.mem[ip+2]
					elif modes[-1] == '2':
						B = self.mem[self.base+self.mem[ip+2]]
					elif modes[-1] == '0':
						B = self.mem[self.mem[ip+2]]
					modes = modes[:-1]
					if modes == '' or modes[-1] == '0':
						self.mem[self.mem[ip+3]] = C * B
					elif modes[-1] == '2':
						self.mem[self.base+self.mem[ip+3]] = C * B
			elif opcode == 3: # Store input at param 1
				d_ip = 2
				if len(self.prog_in) == 0:
					self.blocked = True
					self.ip_state = ip
					return
				if modes == '' or modes == '0':
					self.mem[self.mem[ip+1]] = self.prog_in.pop(0)
				elif modes == '1':
					self.mem[ip+1] = self.prog_in.pop(0)
				elif modes == '2':
					self.mem[self.base+self.mem[ip+1]] = self.prog_in.pop(0)
			elif opcode == 4: # Output value at param 1
				d_ip = 2
				if modes == '' or modes == '0':
					self.last_out = self.mem[self.mem[ip+1]]
				elif modes == '1':
					self.last_out = self.mem[ip+1]
				elif modes == '2':
					self.last_out = self.mem[self.base+self.mem[ip+1]]
				yield self.last_out
			elif opcode == 5: # Jump if True (non-zero)
				d_ip = 3
				if modes == '':
					if self.mem[self.mem[ip+1]] != 0:
						ip = self.mem[self.mem[ip+2]]
						ip_updated = True
				else:
					if modes[-1] == '1':
						C = self.mem[ip+1]
					elif modes[-1] == '0':
						C = self.mem[self.mem[ip+1]]
					elif modes[-1] == '2':
						C = self.mem[self.base+self.mem[ip+1]]
					modes = modes[:-1]
					if modes == '':
						modes = '0'
					if modes[-1] == '1':
						B = self.mem[ip+2]
					elif modes[-1] == '0':
						B = self.mem[self.mem[ip+2]]
					elif modes[-1] == '2':
						B = self.mem[self.base+self.mem[ip+2]]
					modes = modes[:-1]
					if C != 0:
						ip = B
						ip_updated = True
			elif opcode == 6: # Jump if False (zero)
				d_ip = 3
				if modes == '':
					if self.mem[self.mem[ip+1]] == 0:
						ip = self.mem[self.mem[ip+2]]
						ip_updated = True
				else:
					if modes[-1] == '1':
						C = self.mem[ip+1]
					elif modes[-1] == '0':
						C = self.mem[self.mem[ip+1]]
					elif modes[-1] == '2':
						C = self.mem[self.base+self.mem[ip+1]]
					modes = modes[:-1]
					if modes == '':
						modes = '0'
					if modes[-1] == '1':
						B = self.mem[ip+2]
					elif modes[-1] == '0':
						B = self.mem[self.mem[ip+2]]
					elif modes[-1] == '2':
						B = self.mem[self.base+self.mem[ip+2]]
					modes = modes[:-1]
					if C == 0:
						ip = B
						ip_updated = True
			elif opcode == 7: # res = C < B
				d_ip = 4
				if modes == '':
					if self.mem[self.mem[ip+1]] < self.mem[self.mem[ip+2]]:
						self.mem[self.mem[ip+3]] = 1
					else:
						self.mem[self.mem[ip+3]] = 0
				else:
					if modes[-1] == '1':
						C = self.mem[ip+1]
					elif modes[-1] == '0':
						C = self.mem[self.mem[ip+1]]
					elif modes[-1] == '2':
						C = self.mem[self.base+self.mem[ip+1]]
					modes = modes[:-1]
					if modes == '':
						modes = '0'
					if modes[-1] == '1':
						B = self.mem[ip+2]
					elif modes[-1] == '0':
						B = self.mem[self.mem[ip+2]]
					elif modes[-1] == '2':
						B = self.mem[self.base+self.mem[ip+2]]
					modes = modes[:-1]
					if C < B:
						if modes == '' or modes[-1] == '0':
							self.mem[self.mem[ip+3]] = 1
						elif modes[-1] == '2':
							self.mem[self.base+self.mem[ip+3]] = 1
					else:
						if modes == '' or modes[-1] == '0':
							self.mem[self.mem[ip+3]] = 0
						elif modes[-1] == '2':
							self.mem[self.base+self.mem[ip+3]] = 0
			elif opcode == 8: # res = C == B
				d_ip = 4
				if modes == '':
					if self.mem[self.mem[ip+1]] == self.mem[self.mem[ip+2]]:
						self.mem[self.mem[ip+3]] = 1
					else:
						self.mem[self.mem[ip+3]] = 0
				else:
					if modes[-1] == '1':
						C = self.mem[ip+1]
					elif modes[-1] == '0':
						C = self.mem[self.mem[ip+1]]
					elif modes[-1] == '2':
						C = self.mem[self.base+self.mem[ip+1]]
					modes = modes[:-1]
					if modes == '':
						modes = '0'
					if modes[-1] == '1':
						B = self.mem[ip+2]
					elif modes[-1] == '0':
						B = self.mem[self.mem[ip+2]]
					elif modes[-1] == '2':
						B = self.mem[self.base+self.mem[ip+2]]
					modes = modes[:-1]
					if C == B:
						if modes == '' or modes[-1] == '0':
							self.mem[self.mem[ip+3]] = 1
						elif modes[-1] == '2':
							self.mem[self.base+self.mem[ip+3]] = 1
					else:
						if modes == '' or modes[-1] == '0':
							self.mem[self.mem[ip+3]] = 0
						elif modes[-1] == '2':
							self.mem[self.base+self.mem[ip+3]] = 0
			elif opcode == 9: # adjust base pointer by param
				d_ip = 2
				if modes == '':
					self.base += self.mem[self.mem[ip+1]]
				else:
					if modes[-1] == '1':
						self.base += self.mem[ip+1]
					elif modes[-1] == '0':
						self.base += self.mem[self.mem[ip+1]]
					elif modes[-1] == '2':
						self.base += self.mem[self.base+self.mem[ip+1]]
			if not ip_updated:
				ip += d_ip

def get_world_view(vm):
	camera_view = dict()
	x = 0
	y = 0
	for char in vm.run():
		if char == 10:
			y += 1
			x = -1
		else:
			camera_view[(x,y)] = chr(char)
		x += 1
	return camera_view

def intersection_count(w):
	count = 0
	v = ['^','<','>','v','#']
	max_x = 0
	max_y = 0
	for key in w.keys():
		x, y = key
		max_x = max(x, max_x)
		max_y = max(y, max_y)
	for x in range(1,max_x-1):
		for y in range(1,max_y-1):
			if w[(x,y)] in v and w[(x+1,y)] in v and w[(x-1,y)] and w[(x,y+1)] in v and w[(x,y-1)] in v:
				count += (x * y)
	return count			

if __name__ == "__main__":

	# Part 1 Solution
	with open("day17_input", 'r') as infile:
		prog = [ int(x) for x in infile.readline().strip().split(',') ]
	vm = IntPuterVM(prog[:])
	print(intersection_count(get_world_view(vm)))

# Part 2 Solution

	with open("day17_input", 'r') as infile:
		prog = [ int(x) for x in infile.readline().strip().split(',') ]
	vm = IntPuterVM(prog[:])
	vm.mem[0] = 2 # for setting mode
	for char in vm.run():
		print(chr(char), end='')
	vm.ascii_readln("A,A,B,C,B,C,B,C,C,A")
	for char in vm.run():
		print(chr(char), end='')
	vm.ascii_readln("R,8,L,4,R,4,R,10,R,8")
	for char in vm.run():
		print(chr(char), end='')
	vm.ascii_readln("L,12,L,12,R,8,R,8")
	for char in vm.run():
		print(chr(char), end='')
	vm.ascii_readln("R,10,R,4,R,4")
	for char in vm.run():
		print(chr(char), end='')
	vm.ascii_readln("n")
	for char in vm.run():
		if char < 255:
			print(chr(char),end='')
		else:
			print(char)
	#print(intersection_count(get_world_view(vm)))

	"""
	..................#########..........
	..................#.......#..........
	#########.........#.......#..........
	#.................#.......#..........
	#.......#####.....#.......#..........
	#.......#...#.....#.......#..........
	#.......#.#############...#..........
	#.......#.#.#.....#...#...#..........
	#...#########.....#############......
	#...#...#.#...........#...#...#......
	#.###########.........#####...#......
	#.#.#...#.#.#.................#......
	#####...#.#.#.................#......
	..#.....#.#.#.................#......
	..#.....#####.................#......
	..#.......#...................#......
	..#.......#.................#########
	..#.......#.................#.#.....#
	..#########.................#.#.....#
	............................#.#.....#
	......###########.........#####.....#
	......#.........#.........#.#.......#
	......#.......#####.......#.#.......#
	......#.......#.#.#.......#.#.......#
	......#####...#.#.#.......###########
	..........#...#.#.#.........#........
	......^########.#.#.........#........
	..........#.....#.#.........#........
	..........#.....#############........
	..........#.......#..................
	..........#.......#..................
	..........#.......#..................
	..........#########..................
	"""

	"""
	# Whole Path
	
    R,8,L,4,R,4,R,10,R,8,R,8,L,4,R,4,R,10,R,8,L,12,L,12,R,8,R,8,R,10,R,4,R,4,L,12,L,12,R,8,R,8,R,10,R,4,R,4,L,12,L,12,R,8,R,8,R,10,R,4,R,4,R,10,R,4,R,4,R,8,L,4,R,4,R,10,R,8

	A = R,8,L,4,R,4,R,10,R,8
	B = L,12,L,12,R,8,R,8
	C = R,10,R,4,R,4
	COMPRESSED = A,A,B,C,B,C,B,C,C,A
	"""

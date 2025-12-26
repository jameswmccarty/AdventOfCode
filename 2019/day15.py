#!/usr/bin/python

from copy import deepcopy


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

o_gen_loc = None
world_map = dict()
search_buffer = list()
def discover_world():
	global world_map
	global search_buffer
	global o_gen_loc
	while len(search_buffer) > 0:
		vm, pos, steps = search_buffer.pop(0)
		x, y = pos
		n_vm = deepcopy(vm)
		n_vm.buffer_read(1)
		s_vm = deepcopy(vm)
		s_vm.buffer_read(2)
		e_vm = deepcopy(vm)
		e_vm.buffer_read(3)
		w_vm = deepcopy(vm)
		w_vm.buffer_read(4)
		if (x, y+1) not in world_map:
			for reply in n_vm.run():
				world_map[(x,y+1)] = reply
				if reply == 1:
					search_buffer.append((n_vm, (x,y+1), steps+1))
				elif reply == 2:
					o_gen_loc = (x,y+1)
					return steps+1
		if (x, y-1) not in world_map:
			for reply in s_vm.run():
				world_map[(x,y-1)] = reply
				if reply == 1:
					search_buffer.append((s_vm, (x,y-1), steps+1))
				elif reply == 2:
					o_gen_loc = (x,y-1)
					return steps+1
		if (x+1, y) not in world_map:
			for reply in e_vm.run():
				world_map[(x+1,y)] = reply
				if reply == 1:
					search_buffer.append((e_vm, (x+1,y), steps+1))
				elif reply == 2:
					o_gen_loc = (x+1,y)
					return steps+1
		if (x-1, y) not in world_map:
			for reply in w_vm.run():
				world_map[(x-1,y)] = reply
				if reply == 1:
					search_buffer.append((w_vm, (x-1,y), steps+1))
				elif reply == 2:
					o_gen_loc = (x-1,y)
					return steps+1

def discover_world_full():
	global world_map
	global search_buffer
	while len(search_buffer) > 0:
		vm, pos = search_buffer.pop(0)
		x, y = pos
		n_vm = deepcopy(vm)
		n_vm.buffer_read(1)
		s_vm = deepcopy(vm)
		s_vm.buffer_read(2)
		e_vm = deepcopy(vm)
		e_vm.buffer_read(3)
		w_vm = deepcopy(vm)
		w_vm.buffer_read(4)
		if (x, y+1) not in world_map:
			for reply in n_vm.run():
				world_map[(x,y+1)] = reply
				if reply == 1 or reply == 2:
					search_buffer.append((n_vm, (x,y+1)))
		if (x, y-1) not in world_map:
			for reply in s_vm.run():
				world_map[(x,y-1)] = reply
				if reply == 1 or reply == 2:
					search_buffer.append((s_vm, (x,y-1)))
		if (x+1, y) not in world_map:
			for reply in e_vm.run():
				world_map[(x+1,y)] = reply
				if reply == 1 or reply == 2:
					search_buffer.append((e_vm, (x+1,y)))
		if (x-1, y) not in world_map:
			for reply in w_vm.run():
				world_map[(x-1,y)] = reply
				if reply == 1 or reply == 2:
					search_buffer.append((w_vm, (x-1,y)))

def time_o2():
	global search_buffer
	global world_map
	seen = set()
	max_steps = 0
	while len(search_buffer) > 0:
		pos, steps = search_buffer.pop(0)
		x, y = pos
		max_steps = max(max_steps, steps)
		seen.add(pos)
		if (x+1,y) not in seen and (x+1,y) in world_map and world_map[(x+1,y)] != 0:
			search_buffer.append(((x+1,y),steps+1))
		if (x-1,y) not in seen and (x-1,y) in world_map and world_map[(x-1,y)] != 0:
			search_buffer.append(((x-1,y),steps+1))
		if (x,y+1) not in seen and (x,y+1) in world_map and world_map[(x,y+1)] != 0:
			search_buffer.append(((x,y+1),steps+1))
		if (x,y-1) not in seen and (x,y-1) in world_map and world_map[(x,y-1)] != 0:
			search_buffer.append(((x,y-1),steps+1))
	return max_steps	

if __name__ == "__main__":

	# Part 1 Solution
	with open("day15_input", 'r') as infile:
		prog = [ int(x) for x in infile.readline().strip().split(',') ]
	vm = IntPuterVM(prog[:])
	world_map[(0,0)] = 1
	search_buffer.append((vm, (0,0), 0))
	print(discover_world())

	# Part 2 Solution
	with open("day15_input", 'r') as infile:
		prog = [ int(x) for x in infile.readline().strip().split(',') ]
	vm = IntPuterVM(prog[:])
	world_map = dict()
	world_map[(0,0)] = 1
	search_buffer = list()
	search_buffer.append((vm, (0,0)))
	discover_world_full()
	search_buffer = list()
	search_buffer.append((o_gen_loc, 0))
	print(time_o2())


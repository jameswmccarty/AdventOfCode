#!/usr/bin/python

from itertools import permutations


class IntPuterVM:
	
	def __init__(self, memory):
		self.mem = memory
		self.last_out = None
		self.prog_in = []
		self.halted = False
		self.blocked = True
		self.ip_state = 0

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
					elif modes[-1] == '0':
						C = self.mem[self.mem[ip+1]]
					modes = modes[:-1]
					if modes == '':
						modes = '0'
					if modes[-1] == '1':
						B = self.mem[ip+2]
					elif modes[-1] == '0':
						B = self.mem[self.mem[ip+2]]
					modes = modes[:-1]
					self.mem[self.mem[ip+3]] = C + B
			elif opcode == 2: # res = C * B
				d_ip = 4
				if modes == '':
					self.mem[self.mem[ip+3]] = self.mem[self.mem[ip+1]] * self.mem[self.mem[ip+2]]
				else:
					if modes[-1] == '1':
						C = self.mem[ip+1]
					elif modes[-1] == '0':
						C = self.mem[self.mem[ip+1]]
					modes = modes[:-1]
					if modes == '':
						modes = '0'
					if modes[-1] == '1':
						B = self.mem[ip+2]
					elif modes[-1] == '0':
						B = self.mem[self.mem[ip+2]]
					modes = modes[:-1]
					self.mem[self.mem[ip+3]] = C * B
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
			elif opcode == 4: # Output value at param 1
				d_ip = 2
				if modes == '' or modes == '0':
					self.last_out = self.mem[self.mem[ip+1]]
				elif modes == '1':
					self.last_out = self.mem[ip+1]
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
					modes = modes[:-1]
					if modes == '':
						modes = '0'
					if modes[-1] == '1':
						B = self.mem[ip+2]
					elif modes[-1] == '0':
						B = self.mem[self.mem[ip+2]]
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
					modes = modes[:-1]
					if modes == '':
						modes = '0'
					if modes[-1] == '1':
						B = self.mem[ip+2]
					elif modes[-1] == '0':
						B = self.mem[self.mem[ip+2]]
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
					modes = modes[:-1]
					if modes == '':
						modes = '0'
					if modes[-1] == '1':
						B = self.mem[ip+2]
					elif modes[-1] == '0':
						B = self.mem[self.mem[ip+2]]
					modes = modes[:-1]
					if C < B:
						self.mem[self.mem[ip+3]] = 1
					else:
						self.mem[self.mem[ip+3]] = 0
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
					modes = modes[:-1]
					if modes == '':
						modes = '0'
					if modes[-1] == '1':
						B = self.mem[ip+2]
					elif modes[-1] == '0':
						B = self.mem[self.mem[ip+2]]
					modes = modes[:-1]
					if C == B:
						self.mem[self.mem[ip+3]] = 1
					else:
						self.mem[self.mem[ip+3]] = 0
			if not ip_updated:
				ip += d_ip	

if __name__ == "__main__":

	# Part 1 Solution
	with open("day07_input", 'r') as infile:
		prog = [ int(x) for x in infile.readline().strip().split(',') ]
	max_out = 0
	for combo in permutations(range(5),5):
		VMs = [ IntPuterVM(prog[:]) for i in range(5) ]
		combo = list(combo)
		for idx in range(5):
			VMs[idx].buffer_read(combo.pop(0))
		VMs[0].buffer_read(0)
		for idx in range(5):
			for prog_out in VMs[idx].run():
				break
			if idx < 4:
				VMs[idx+1].buffer_read(prog_out)
			else:
				max_out = max(max_out, prog_out)
	print(max_out)

	# Part 2 Solution
	with open("day07_input", 'r') as infile:
		prog = [ int(x) for x in infile.readline().strip().split(',') ]
	max_out = 0
	for combo in permutations(range(5,10),5):
		VMs = [ IntPuterVM(prog[:]) for i in range(5) ]
		combo = list(combo)
		for idx in range(5):
			VMs[idx].buffer_read(combo.pop(0))
		VMs[0].buffer_read(0)
		idx = 0		
		while True:
			if sum( [x.halted for x in VMs] ) == 5:
				break
			for prog_out in VMs[idx].run():
				if VMs[idx].blocked:
					break
				VMs[(idx+1)%5].buffer_read(prog_out)
			idx += 1
			if idx > 4:
				idx = 0			
		max_out = max(max_out, VMs[4].last_out)
	print(max_out)

	

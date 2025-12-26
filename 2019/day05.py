#!/usr/bin/python


prog_in = None
prog_out = None

def run(p):
	global prog_out
	global prog_in
	ip = 0
	while True:
		A = None
		B = None
		C = None
		d_ip = None
		ip_updated = False
		op = p[ip]
		modes, opcode = str(op)[:-2], int(str(op)[-2:])
		if opcode == 99: # Halt
			return True
		if opcode == 1: # res = C + B
			d_ip = 4
			if modes == '':
				p[p[ip+3]] = p[p[ip+1]] + p[p[ip+2]]
			else:
				if modes[-1] == '1':
					C = p[ip+1]
				elif modes[-1] == '0':
					C = p[p[ip+1]]
				modes = modes[:-1]
				if modes == '':
					modes = '0'
				if modes[-1] == '1':
					B = p[ip+2]
				elif modes[-1] == '0':
					B = p[p[ip+2]]
				modes = modes[:-1]
				p[p[ip+3]] = C + B
		elif opcode == 2: # res = C * B
			d_ip = 4
			if modes == '':
				p[p[ip+3]] = p[p[ip+1]] * p[p[ip+2]]
			else:
				if modes[-1] == '1':
					C = p[ip+1]
				elif modes[-1] == '0':
					C = p[p[ip+1]]
				modes = modes[:-1]
				if modes == '':
					modes = '0'
				if modes[-1] == '1':
					B = p[ip+2]
				elif modes[-1] == '0':
					B = p[p[ip+2]]
				modes = modes[:-1]
				p[p[ip+3]] = C * B
		elif opcode == 3: # Store input at param 1
			d_ip = 2
			if modes == '' or modes == '0':
				p[p[ip+1]] = prog_in
			elif modes == '1':
				p[ip+1] = prog_in
		elif opcode == 4: # Output value at param 1
			d_ip = 2
			if modes == '' or modes == '0':
				prog_out = p[p[ip+1]]
			elif modes == '1':
				prog_out = p[ip+1]
		elif opcode == 5: # Jump if True (non-zero)
			d_ip = 3
			if modes == '':
				if p[p[ip+1]] != 0:
					ip = p[p[ip+2]]
					ip_updated = True
			else:
				if modes[-1] == '1':
					C = p[ip+1]
				elif modes[-1] == '0':
					C = p[p[ip+1]]
				modes = modes[:-1]
				if modes == '':
					modes = '0'
				if modes[-1] == '1':
					B = p[ip+2]
				elif modes[-1] == '0':
					B = p[p[ip+2]]
				modes = modes[:-1]
				if C != 0:
					ip = B
					ip_updated = True
		elif opcode == 6: # Jump if False (zero)
			d_ip = 3
			if modes == '':
				if p[p[ip+1]] == 0:
					ip = p[p[ip+2]]
					ip_updated = True
			else:
				if modes[-1] == '1':
					C = p[ip+1]
				elif modes[-1] == '0':
					C = p[p[ip+1]]
				modes = modes[:-1]
				if modes == '':
					modes = '0'
				if modes[-1] == '1':
					B = p[ip+2]
				elif modes[-1] == '0':
					B = p[p[ip+2]]
				modes = modes[:-1]
				if C == 0:
					ip = B
					ip_updated = True
		elif opcode == 7: # res = C < B
			d_ip = 4
			if modes == '':
				if p[p[ip+1]] < p[p[ip+2]]:
					p[p[ip+3]] = 1
				else:
					p[p[ip+3]] = 0
			else:
				if modes[-1] == '1':
					C = p[ip+1]
				elif modes[-1] == '0':
					C = p[p[ip+1]]
				modes = modes[:-1]
				if modes == '':
					modes = '0'
				if modes[-1] == '1':
					B = p[ip+2]
				elif modes[-1] == '0':
					B = p[p[ip+2]]
				modes = modes[:-1]
				if C < B:
					p[p[ip+3]] = 1
				else:
					p[p[ip+3]] = 0
		elif opcode == 8: # res = C == B
			d_ip = 4
			if modes == '':
				if p[p[ip+1]] == p[p[ip+2]]:
					p[p[ip+3]] = 1
				else:
					p[p[ip+3]] = 0
			else:
				if modes[-1] == '1':
					C = p[ip+1]
				elif modes[-1] == '0':
					C = p[p[ip+1]]
				modes = modes[:-1]
				if modes == '':
					modes = '0'
				if modes[-1] == '1':
					B = p[ip+2]
				elif modes[-1] == '0':
					B = p[p[ip+2]]
				modes = modes[:-1]
				if C == B:
					p[p[ip+3]] = 1
				else:
					p[p[ip+3]] = 0
		if not ip_updated:
			ip += d_ip

if __name__ == "__main__":
	
	# Tests

	"""
	program = [1002,4,3,4,33]
	run(program)
	print(prog_out)
	"""

	# Part 1 Solution
	with open("day05_input", 'r') as infile:
		program = infile.readline().strip()
		program = program.split(',')
		program = [ int(x) for x in program ]
		prog_in = 1		
		run(program)
		print(prog_out)

	prog_in = None
	prog_out = None

	# Part 2 Solution
	with open("day05_input", 'r') as infile:
		program = infile.readline().strip()
		program = program.split(',')
		program = [ int(x) for x in program ]
		prog_in = 5		
		run(program)
		print(prog_out)


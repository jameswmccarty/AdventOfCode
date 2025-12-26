#!/usr/bin/python


regs = {} # register bank
mul_count = 0 # counter
ip = 0

def init(): # zero all registers a-z
	global regs
	for reg in range(97,106): #a-h
		regs[chr(reg)] = 0
		
# set X Y sets register X to the value of Y.
def set(x, y):
	if y in regs:
		regs[x] = regs[y]
	else:
		regs[x] = int(y)
		
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
def mul(x, y):
	global mul_count
	mul_count += 1
	if y in regs:
		regs[x] *= regs[y]
	else:
		regs[x] *= int(y)
		
# add X Y decreases register X by the value of Y.
def sub(x, y):
	if y in regs:
		regs[x] -= regs[y]
	else:
		regs[x] -= int(y)

# jnz X Y jumps with an offset of the value of Y, but only if the value of X is not equal to zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
def jnz(x, y):
	global ip
	if x in regs:
		if regs[x] != 0:
			if y in regs:
				ip += (regs[y]-1)
			else:
				ip += (int(y)-1)
	elif x != 0:
		if y in regs:
			ip += (regs[y]-1)
		else:
			ip += (int(y)-1)		
		
if __name__ == "__main__":
	
	# Part 1 Solution

	op = {"set" : set, "sub" : sub, "mul" : mul, "jnz" : jnz }
	
	program = []
	
	with open("day23_input", "r") as infile:
		for line in infile.readlines():
			program.append(line.strip().split(" "))
			
	init()
	while ip < len(program) and ip > -1:
		op[program[ip][0]](program[ip][1],program[ip][2])
		ip += 1
	print mul_count

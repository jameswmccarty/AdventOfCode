#!/usr/bin/python


regs = {} # register bank
last_snd = 0 # last sound played
ip = 0 # instruction pointer
first_run = True

def init(): # zero all registers a-z
	global regs
	for reg in range(97,123): #a-z
		regs[chr(reg)] = 0
		
# snd X plays a sound with a frequency equal to the value of X.
def snd(reg, jnk):
	global last_snd
	last_snd = regs[reg]

# set X Y sets register X to the value of Y.
def set(x, y):
	if y in regs:
		regs[x] = regs[y]
	else:
		regs[x] = int(y)

# add X Y increases register X by the value of Y.
def add(x, y):
	if y in regs:
		regs[x] += regs[y]
	else:
		regs[x] += int(y)
	
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
def mul(x, y):
	if y in regs:
		regs[x] *= regs[y]
	else:
		regs[x] *= int(y)
	
# mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
def mod(x, y):
	if y in regs:
		regs[x] %= regs[y]
	else:
		regs[x] %= int(y)

# rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
def rcv(x, jnk):
	global last_snd
	global first_run
	if regs[x] != 0:
		regs[x] = last_snd
		if first_run:
			print "Recovered last sound of ", last_snd
			first_run = False
	
# jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
def jgz(x, y):
	global ip
	if x in regs:
		if regs[x] > 0:
			if y in regs:
				ip += (regs[y]-1)
			else:
				ip += (int(y)-1)
	elif x > 0:
		if y in regs:
			ip += (regs[y]-1)
		else:
			ip += (int(y)-1)


if __name__ == "__main__":

	# Part 1 Solution

	op = {"snd" : snd, "set" : set, "add" : add, "mul" : mul, "mod" : mod, "rcv" : rcv, "jgz" : jgz }
	
	program = []
	
	with open("day18_input", "r") as infile:
		for line in infile.readlines():
			program.append(line.strip().split(" "))
			
	init()
	while ip < len(program) and ip > -1:
		if len(program[ip]) < 3: # some opcodes only have one argument
			program[ip].append(None) # avoid index OOB
		op[program[ip][0]](program[ip][1],program[ip][2])
		ip += 1

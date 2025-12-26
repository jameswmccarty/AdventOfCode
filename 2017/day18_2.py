#!/usr/bin/python


regs1 = {} # register bank
regs2 = {} # register bank

def init(): # zero all registers a-z, set program id in reg p
	global regs1
	global regs2
	for reg in range(97,123): #a-z
		regs1[chr(reg)] = 0
		regs2[chr(reg)] = 0
	regs2['p'] = 1
	regs1['sent'] = 0 # sent message counters
	regs2['sent'] = 0
	regs1['id'] = 0
	regs2['id'] = 1
	regs1['ip'] = 0 # instruction pointer
	regs2['ip'] = 0
	regs1['msg'] = [] # message queue
	regs2['msg'] = []
	regs1['lock'] = False # deadlocked
	regs2['lock'] = False
	regs1['run'] = True # ip in bounds
	regs2['run'] = True
		
# snd X pass a message to other copy of program
def snd(reg, jnk, regs):
	global regs1
	global regs2
	if regs['id'] == 0:
		if reg in regs:
			regs2['msg'].append(regs[reg])
		else:
			regs2['msg'].append(int(reg))
	else:
		if reg in regs:
			regs1['msg'].append(regs[reg])
		else:
			regs1['msg'].append(int(reg))
	regs['sent'] += 1

# set X Y sets register X to the value of Y.
def set(x, y, regs):
	if y in regs:
		regs[x] = regs[y]
	else:
		regs[x] = int(y)

# add X Y increases register X by the value of Y.
def add(x, y, regs):
	if y in regs:
		regs[x] += regs[y]
	else:
		regs[x] += int(y)
	
# mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
def mul(x, y, regs):
	if y in regs:
		regs[x] *= regs[y]
	else:
		regs[x] *= int(y)
	
# mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
def mod(x, y, regs):
	if y in regs:
		regs[x] %= regs[y]
	else:
		regs[x] %= int(y)

# rcv X get input from other program
def rcv(x, jnk, regs):
	global regs1
	global regs2
	if len(regs['msg']) > 0:
		regs[x] = regs['msg'].pop(0)
		regs['lock'] = False
	else:
		regs['lock'] = True
		
		if regs1['lock'] and regs2['lock']:
			print "Program Terminated."
			regs1['run'] = False
			regs2['run'] = False
		
		else:
			regs['ip'] -= 1 # 'spin wait' this inst
			print "Spin waiting on program", regs['id']
				
# jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
def jgz(x, y, regs):
	if x in regs:
		if regs[x] > 0:
			if y in regs:
				regs['ip'] += (regs[y]-1)
			else:
				regs['ip'] += (int(y)-1)
	elif x > 0:
		if y in regs:
			regs['ip'] += (regs[y]-1)
		else:
			regs['ip'] += (int(y)-1)


if __name__ == "__main__":

	# Part 2 Solution

	op = {"snd" : snd, "set" : set, "add" : add, "mul" : mul, "mod" : mod, "rcv" : rcv, "jgz" : jgz }
	
	program1 = []
	program2 = []
	
	with open("day18_input", "r") as infile:
		for line in infile.readlines():
			program1.append(line.strip().split(" "))
			program2.append(line.strip().split(" "))
			
	init()
	while regs1['run'] or regs2['run']:
		if regs1['ip'] < len(program1) and regs1['ip'] > -1:
			if len(program1[regs1['ip']]) < 3: # some opcodes only have one argument
				program1[regs1['ip']].append(None) # avoid index OOB
			op[program1[regs1['ip']][0]](program1[regs1['ip']][1],program1[regs1['ip']][2], regs1)
			regs1['ip'] += 1
		else:
			regs1['run'] = False
		if regs2['ip'] < len(program2) and regs2['ip'] > -1:
			if len(program2[regs2['ip']]) < 3: # some opcodes only have one argument
				program2[regs2['ip']].append(None) # avoid index OOB
			op[program2[regs2['ip']][0]](program2[regs2['ip']][1],program2[regs2['ip']][2], regs2)
			regs2['ip'] += 1
		else:
			regs2['run'] = False
			
	print "Program 0 sent", regs1['sent']
	print "Program 1 sent", regs2['sent']

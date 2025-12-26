#!/usr/bin/python


# 4 registers
regs = { "0" : 0,
	 "1" : 0,
	 "2" : 0,
	 "3" : 0}

opcode_poss = {	"0" : set(),	
	       "1" : set(),
		"2" : set(),
		"3" : set(),
		"4" : set(),
		"5" : set(),
		"6" : set(),
		"7" : set(),
		"8" : set(),
		"9" : set(),
		"10" : set(),
		"11" : set(),
		"12" : set(),
		"13" : set(),
		"14" : set(),
		"15" : set()}
				 
opcode_neg = {	"0" : set(),	
		"1" : set(),
		"2" : set(),
		"3" : set(),
		"4" : set(),
		"5" : set(),
		"6" : set(),
		"7" : set(),
		"8" : set(),
		"9" : set(),
		"10" : set(),
		"11" : set(),
		"12" : set(),
		"13" : set(),
		"14" : set(),
		"15" : set()}
				 
def regs_set(a, b, c, d):
	regs["0"] = a
	regs["1"] = b
	regs["2"] = c
	regs["3"] = d

def reset():
	global regs
	regs = { "0" : 0, "1" : 0, "2" : 0, "3" : 0}
	
def regs_dump():
	return [ regs["0"], regs["1"], regs["2"], regs["3"] ]

# addr (add register) 
# stores into register C the result of adding register A and register B.
def addr(a,b,c):
	regs[c] = int(regs[a]) + int(regs[b])

# addi (add immediate)
# stores into register C the result of adding register A and value B.	
def addi(a, b, c):
	regs[c] = int(regs[a]) + int(b)

# mulr (multiply register) stores into register C 
# the result of multiplying register A and register B.
def mulr(a, b, c):
	regs[c] = int(regs[a]) * int(regs[b])

# muli (multiply immediate) 
# stores into register C the result of multiplying register A and value B.
def muli(a, b, c):
	regs[c] = int(regs[a]) * int(b)
	
# banr (bitwise AND register) stores into register C the result of the 
# bitwise AND of register A and register B.
def banr(a, b, c):
	regs[c] = int(regs[a]) & int(regs[b])

# bani (bitwise AND immediate) stores into register C the result of the 
# bitwise AND of register A and value B.
def bani(a, b, c):
	regs[c] = int(regs[a]) & int(b)

# borr (bitwise OR register) stores into register C the result of the 
# bitwise OR of register A and register B.
def borr(a, b, c):
	regs[c] = int(regs[a]) | int(regs[b])

# bori (bitwise OR immediate) stores into register C the result of the 
# bitwise OR of register A and value B.
def bori(a, b, c):
	regs[c] = int(regs[a]) | int(b)

# setr (set register) copies the contents of register A into register C. 
# (Input B is ignored.)
def setr(a, b, c):
	regs[c] = int(regs[a])

# seti (set immediate) stores value A into register C. 
# (Input B is ignored.)
def seti(a, b, c):
	regs[c] = int(a)

# gtir (greater-than immediate/register) sets register C to 1 if value A is 
# greater than register B. Otherwise, register C is set to 0.
def gtir(a, b, c):
	if(int(a) > int(regs[b])):
		regs[c] = 1
	else:
		regs[c] = 0

# gtri (greater-than register/immediate) sets register C to 1 if register 
# A is greater than value B. Otherwise, register C is set to 0.
def gtri(a, b, c):
	if(int(regs[a]) > int(b)):
		regs[c] = 1
	else:
		regs[c] = 0
		
# gtrr (greater-than register/register) sets register C to 1 if register A 
# is greater than register B. Otherwise, register C is set to 0.
def gtrr(a, b, c):
	if(int(regs[a]) > int(regs[b])):
		regs[c] = 1
	else:
		regs[c] = 0

# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. 
# Otherwise, register C is set to 0.
def eqir(a, b, c):
	if(int(a) == int(regs[b])):
		regs[c] = 1
	else:
		regs[c] = 0

# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. 
# Otherwise, register C is set to 0.
def eqri(a, b, c):
	if(int(regs[a]) == int(b)):
		regs[c] = 1
	else:
		regs[c] = 0
		
# eqrr (equal register/register) sets register C to 1 if register A is equal to register B.
# Otherwise, register C is set to 0.
def eqrr(a, b, c):
	if(int(regs[a]) == int(regs[b])):
		regs[c] = 1
	else:
		regs[c] = 0

# If an instruction is valid for an opcode,
# then add the opcode to the set of possibilities
# for that opcode number
def evaluate(samples, opcodes):
	
	for sample in samples:
		for opcode in opcodes:
			if sample.test(opcode):
				opcode_poss[sample.op].add(opcode)
			else:
				opcode_neg[sample.op].add(opcode)	

# called once evaluate has been run
def assign():
	
	opcode_map = {}
	for i in range(16):
		opcode_map[str(i)] = None
	
	assigned = 0
	
	for op in opcode_poss:
		opcode_poss[op] = opcode_poss[op].difference(opcode_neg[op])
	
	while assigned < len(opcode_map):
		
		for op in opcode_poss:
			inst = None
			# only one option for a given opcode
			if len(opcode_poss[op]) == 1:
				inst = opcode_poss[op].pop()
				opcode_map[op] = inst
				assigned += 1
				# print "Assignment found for opcode : " + str(op)
				# remove assigned opcode from other sets
				for opc in opcode_poss:
					if inst in opcode_poss[opc]:
						opcode_poss[opc].remove(inst)
						
	return opcode_map		

def verify(mapping):
	
	for opcode in mapping:
		for sample in samples:
			if sample.op == opcode:
				if not sample.test(mapping[opcode]):
					return False
	return True
	
class Sample:

	# Before: [1, 0, 2, 1]
	# 2 3 2 0
	# After:  [1, 0, 2, 1]

	def __init__(self, before, cmd, after):
		before = before.replace("Before: [", '')
		before = before.replace("]", '')
		start = before.strip().split(",")
		self.start = [ int(x) for x in start ]
		cmds = cmd.split(" ")
		self.op = cmds[0].strip()
		self.a  = cmds[1].strip()
		self.b  = cmds[2].strip()
		self.c  = cmds[3].strip()
		after = after.replace("After:  [", '')
		after = after.replace("]", '')
		after = after.strip().split(",")
		self.end = [ int(x) for x in after ]
		
	def test(self, opcode):
	
		reset()		
		regs_set(self.start[0], self.start[1], self.start[2], self.start[3])		
		t_f = lambda x : x(self.a, self.b, self.c)
		t_f(opcode)		
		soln = regs_dump()
		for i, val in enumerate(soln):
			if self.end[i] != val:
				return False
		return True

if __name__ == "__main__":

	opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
	samples = []
	program = []
	
	with open("day16_input", "r") as infile:
		while True:
			line = infile.readline()
			if not line:
				break
			# Found a sample
			if "Before" in line:
				l2  = infile.readline()
				l3  = infile.readline()
				samples.append(Sample(line, l2, l3))
			# Reached program
			elif line.strip() != '':
				program.append(line.strip().split(" "))
	
	
	# Part 1 Solution
	valid_samples = 0	
	for sample in samples:
		sample_count = 0
		for code in opcodes:
			if sample.test(code):
				sample_count += 1
		if sample_count >= 3:
			valid_samples += 1	
	print valid_samples	
	
	# Part 2 Solution
	evaluate(samples, opcodes)
	op_map = assign()

	if not verify(op_map):
		print "!!! VALIDATION FAILURE!!!"
		exit()
	
	reset()
	for line in program:
		op_map[line[0]](line[1],line[2],line[3])
	print regs_dump()[0]

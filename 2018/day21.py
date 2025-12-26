#!/usr/bin/python


# 5 registers
regs = { "0" : 0,
		 "1" : 0,
		 "2" : 0,
		 "3" : 0,
		 "4" : 0,
		 "5" : 0}

def reset():
	global regs
	regs = { "0" : 0, "1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0}
	
def regs_dump():
	return [ regs["0"], regs["1"], regs["2"], regs["3"], regs["4"], regs["5"] ]

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

if __name__ == "__main__":

	# map string to function
	op = {"addr" : addr, "addi" : addi, "mulr" : mulr, "muli" : muli, "banr" : banr, "bani" : bani, "borr" : borr, "bori" :bori, "setr" : setr, "seti" : seti, "gtir" : gtir, "gtri" : gtri, "gtrr" : gtrr, "eqir" : eqir, "eqri" : eqri, "eqrr" : eqrr}

	program = []
	
	# Part 1 Solution
	
	with open("day21_input", "r") as infile:
		for line in infile.readlines():
			program.append(line.strip().split(" "))
			
	ip_line = ''.join(program.pop(0))
	ip_line = ip_line.replace("#ip", '').strip() # ip_line contains IP register number
	
	reset()
	ip = 0
	regs["0"] = 2985446
	while ip < len(program) and ip > -1:
		regs[ip_line] = ip
		op[program[ip][0]](program[ip][1],program[ip][2],program[ip][3])
		ip = regs[ip_line]
		ip += 1
		#print regs_dump()
	print regs_dump()[0]
	
	# Part 2 Solution
	
	seen = []

	reset()
	ip = 0
	looped = False
	while ip < len(program) and ip > -1 and not looped:
		regs[ip_line] = ip
		op[program[ip][0]](program[ip][1],program[ip][2],program[ip][3])
		ip = regs[ip_line]
		ip += 1
		if ip == 29:
			if regs["4"] in seen:
				print seen[-1]
				looped = True
			else:
				seen.append(regs["4"])
				#print regs["4"]

			
			
	

#!/usr/bin/python


program = []

regs = { "a" : 0, "b" : 0, "c" : 0, "d" : 0, "ip" : -1 }

# cpy x y copies x (either an integer or the value of a register) into register y
def cpy(r, o):
	if r in regs:
		regs[o] = regs[r]
	else:
		regs[o] = int(r)
# inc x increases the value of register x by one.
def inc(r, o):
	regs[r] += 1
	
# dec x decreases the value of register x by one.	
def dec(r, o):
	regs[r] -= 1

# jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.
def jnz(r, o):
	if r in regs:
		if regs[r] != 0:
			if o in regs:
				regs["ip"] += regs[o]-1
			else:
				regs["ip"] += int(o)-1
	elif int(r) != 0:
		if o in regs:
			regs["ip"] += regs[o]-1
		else:
			regs["ip"] += int(o)-1
		
# tgl x toggles the instruction x away (pointing at instructions like jnz does: positive means forward; negative means backward
def tgl(r, o):
	#If an attempt is made to toggle an instruction outside the program, nothing happens.
	if r in regs:
		dest = regs["ip"] + regs[r]
	else:
		dest = regs["ip"] + int(r)
	if dest >= 0 and dest < len(program):
		program[dest][3] ^= True	

def fac(n):
	if n == 1:
		return 1
	return n*fac(n-1)
		
if __name__ == "__main__":

	# Part 1 Solution
	
	op = { "cpy" : cpy, "inc" : inc, "dec" : dec, "jnz" : jnz, "tgl" : tgl}
	top= { "cpy" : jnz, "inc" : dec, "dec" : inc, "jnz" : cpy, "tgl" : inc}
	
	with open("day23_input", "r") as infile:
		for line in infile.readlines():
			line = line.split(" ")
			if len(line) < 3 and len(line) > 1:
				line.append(".")
			line = [ x.strip().strip(",") for x in line ]
			line.append(False) # line toggle status
			program.append(line)

	regs["a"] = 8 # problem setup
	
	while regs["ip"] < len(program)-1:
		regs["ip"] += 1
		#print regs["ip"], program[regs["ip"]], regs
		if program[regs["ip"]][3]: # Toggle flag set
			try:
				top[program[regs["ip"]][0]](program[regs["ip"]][1], program[regs["ip"]][2])
			except:
				print "Skipped instruction", program[regs["ip"]]
		else:
			op[program[regs["ip"]][0]](program[regs["ip"]][1], program[regs["ip"]][2])

	print regs["a"]
	
	# Part 2 Solution
	
	"""
	Program is computing the factorial of register 'a', plus 91*95=8645
	"""
	
	print fac(12)+8645

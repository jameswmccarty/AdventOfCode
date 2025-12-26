#!/usr/bin/python


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
			regs["ip"] += int(o)-1
	elif int(r) != 0:
		regs["ip"] += int(o)-1
	

if __name__ == "__main__":

	# Part 1 Solution

	program = []
	
	op = { "cpy" : cpy, "inc" : inc, "dec" : dec, "jnz" : jnz }
	
	with open("day12_input", "r") as infile:
		for line in infile.readlines():
			line = line.split(" ")
			if len(line) < 3 and len(line) > 1:
				line.append(".")
			line = [ x.strip().strip(",") for x in line ]
			program.append(line)

	while regs["ip"] < len(program)-1:
		regs["ip"] += 1
		op[program[regs["ip"]][0]](program[regs["ip"]][1], program[regs["ip"]][2])

	print regs["a"]
	
	# Part 2 Solution
	
	regs = { "a" : 0, "b" : 0, "c" : 1, "d" : 0, "ip" : -1 }
	
	while regs["ip"] < len(program)-1:
		regs["ip"] += 1
		op[program[regs["ip"]][0]](program[regs["ip"]][1], program[regs["ip"]][2])

	print regs["a"]

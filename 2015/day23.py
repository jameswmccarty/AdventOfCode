#!/usr/bin/python

regs = { "a" : 0, "b" : 0, "ip" : -1 }

def hlf(r, o):
	regs[r] = int(regs[r] / 2)
	
def tpl(r, o):
	regs[r] *= 3
	
def inc(r, o):
	regs[r] += 1

def jie(r, o):
	if regs[r] % 2 == 0:
		regs["ip"] += int(o)-1

def jio(r, o):
	if regs[r] == 1:
		regs["ip"] += int(o)-1

def jmp(r, o):
	regs["ip"] += int(r)-1

if __name__ == "__main__":

	# Part 1 Solution

	program = []
	op = { "hlf" : hlf, "tpl" : tpl, "inc" : inc, "jie" : jie, "jio" : jio, "jmp" : jmp }
	
	with open("day23_input", "r") as infile:
		for line in infile.readlines():
			line = line.split(" ")
			if len(line) < 3 and len(line) > 1:
				line.append(".")
			line = [ x.strip().strip(",") for x in line ]
			program.append(line)

	while regs["ip"] < len(program)-1:
		regs["ip"] += 1
		op[program[regs["ip"]][0]](program[regs["ip"]][1], program[regs["ip"]][2])

	print regs["b"]
	
	# Part 2 Solution
	
	regs = { "a" : 1, "b" : 0, "ip" : -1 }
	
	while regs["ip"] < len(program)-1:
		regs["ip"] += 1
		op[program[regs["ip"]][0]](program[regs["ip"]][1], program[regs["ip"]][2])

	print regs["b"]

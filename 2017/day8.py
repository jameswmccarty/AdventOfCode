#!/usr/bin/python


registers = {}

def rread(reg):
	if reg in registers:
		return registers[reg]
	else:
		registers[reg] = 0
		return 0

def accu(reg, value):
	registers[reg] = rread(reg) + value

def eq(reg, value):
	if rread(reg) == value:
		return True
	return False

def neq(reg, value):
	if rread(reg) != value:
		return True
	return False
	
def lte(reg, value):
	if rread(reg) <= value:
		return True
	return False

def lt(reg, value):
	if rread(reg) < value:
		return True
	return False
	
def gte(reg, value):
	if rread(reg) >= value:
		return True
	return False

def gt(reg, value):
	if rread(reg) > value:
		return True
	return False

def parse_inst(command):
	action, cond = command.strip().split(" if ")
	if "inc" in action:
		target, value = action.split(" inc ")
		value = int(value)
	else:
		target, value = action.split(" dec ")
		value = int(value) * -1
	valid = False
	if " > " in cond:
		r, v = cond.split(" > ")
		v = int(v)
		valid = gt(r,v)
	elif " >= " in cond:
		r, v = cond.split(" >= ")
		v = int(v)
		valid = gte(r,v)
	elif " < " in cond:
		r, v = cond.split(" < ")
		v = int(v)
		valid = lt(r,v)
	elif " <= " in cond:
		r, v = cond.split(" <= ")
		v = int(v)
		valid = lte(r,v)
	elif " == " in cond:
		r, v = cond.split(" == ")
		v = int(v)
		valid = eq(r,v)
	elif " != " in cond:
		r, v = cond.split(" != ")
		v = int(v)
		valid = neq(r,v)
	if valid:
		accu(target, value)
		
if __name__ == "__main__":

	# Part 1 Solution

	with open("day8_input", "r") as infile:
		for line in infile.readlines():
			parse_inst(line.strip())
	print max(registers.values())
	
	# Part 2 Solution
	registers.clear()
	m = 0
	with open("day8_input", "r") as infile:
		for line in infile.readlines():
			parse_inst(line.strip())
			m = max(m, max(registers.values()))
	print m

#!/usr/bin/python

# Advent of Code 2024 Day 17

# 4A, 5B, 6C
regs = {4:None,5:None,6:None}

ip = 0

mem = []

a_trial = [1,1,1,1,1,1,1,1,1,1,1,1,1,5,1]

def adv(operand):
	global regs
	if operand < 4:
		regs[4] = regs[4] // 2**operand
	else:
		regs[4] = regs[4] // 2**regs[operand]

def bxl(operand):
	global regs
	regs[5] ^= operand

def bst(operand):
	global regs
	if operand < 4:
		regs[5] = operand % 8
	else:
		regs[5] = regs[operand] % 8

def jnz(operand):
	global ip
	if regs[4] != 0:
		ip = operand - 2

def bxc(operand):
	global regs
	regs[5] = regs[5] ^ regs[6]

def out(operand):
	if operand < 4:
		print(operand % 8,end=',')
	else:
		print(regs[operand] % 8,end=',')

def bdv(operand):
	global regs
	if operand < 4:
		regs[5] = regs[4] // 2**operand
	else:
		regs[5] = regs[4] // 2**regs[operand]

def cdv(operand):
	global regs
	if operand < 4:
		regs[6] = regs[4] // 2**operand
	else:
		regs[6] = regs[4] // 2**regs[operand]

opcodes = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

def f(a):
	out = ''
	while a != 0:
		b = a % 8
		b ^= 4
		c = a // 2**b
		b = b ^ c
		b ^= 4
		out += str(b%8)
		a //= 8
	return out

if __name__ == "__main__":

	# Part 1 Solution
	with open("day17_input", "r") as infile:
		for line in infile:
			if "Register A:" in line:
				regs[4] = int(line.lstrip("Register A: ").strip())
			if "Register B:" in line:
				regs[5] = int(line.lstrip("Register B: ").strip())
			if "Register C:" in line:
				regs[6] = int(line.lstrip("Register C: ").strip())
			if "Program:" in line:
				mem = [*map(int,line.lstrip("Program: ").strip().split(','))]

	while ip < len(mem):
		opcode, operand = mem[ip], mem[ip+1]
		opcodes[opcode](operand)
		ip += 2
	print()
	# Part 2 Solution
	# 2,4,1,4,7,5,4,1,1,4,5,5,0,3,3,0
	# BST A | 2,4
	# XOR 4 | 1,4
	# CDV B | 7,5
	# BXC 1 | 4,1
	# XOR 4 | 1,4
	# OUT B | 5,5
	# ADV 3 | 0,3
	# JNZ 0 | 3,0


	#START
	#B = A % 8
	#B ^= 4
	#C = A // 2**B
	#B = B ^ C
	#B ^= 4
	#PRINT B%8
	#A //= 8
	#IF A != 0 GOTO START


	#for i in range(10):
	#	for j in range(10):
	#		for k in range(10):
	#			for l in range(10):
	#				print(i,j,k,l,f(((((((((((((((4*8+3)*8+5)*8+4)*8+3)*8+3)*8+7)*8+6)*8+7)*8+1)*8+2)*8+3)*8+7)*8+k)*8+i)*8+j))

	a= (((((((((((((((4*8+3)*8+5)*8+4)*8+3)*8+3)*8+7)*8+6)*8+7)*8+1)*8+2)*8+3)*8+7)*8+0)*8+0)*8+2)
	while True:
		if f(a) == '2414754114550330' : print(a); exit()
		a += 1

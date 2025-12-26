#!/usr/bin/python


ip = 0
regs = {'acc' : 0 }
mem = []

def nop(value):
	return

def jmp(value):
	global ip
	ip += value - 1

def acc(value):
	regs["acc"] += value

if __name__ == "__main__":

	ops = {"nop" : nop, "jmp" : jmp, "acc" : acc}
	seen = set()

	# Part 1 Solution
	with open("day08_input", 'r') as infile:
		for line in infile.readlines():
			line = line.strip().split()
			mem.append(tuple(line))
	
	while True:
		if ip in seen:
			print(regs["acc"])
			break
		ops[mem[ip][0]](int(mem[ip][1]))
		seen.add(ip)
		ip += 1

	# Part 2 Solution
	
	for z in range(len(mem)):
		trial_mem = mem.copy()
		delta = False
		if mem[z][0] == "nop" and int(mem[z][1]) != 0:
			trial_mem[z] = ("jmp", mem[z][1])
			delta = True
		elif mem[z][0] == "jmp":
			trial_mem[z] = ("nop","+0")
			delta = True
		if delta:
			seen = set()
			ip = 0
			regs["acc"] = 0
			running = True
			while running:
				if ip in seen:
					running = False
				seen.add(ip)
				if ip == len(mem) and running:
					print(regs["acc"])
					exit()
				ops[trial_mem[ip][0]](int(trial_mem[ip][1]))
				ip += 1


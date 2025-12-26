#!/usr/bin/python


and_mask = 0xFFFFFFFFF
or_mask  = 0x000000000
mem_mask = ''
mem = dict()

def set_mask(mask):
	global and_mask 
	global or_mask  
	and_mask = 0xFFFFFFFFF
	or_mask  = 0x000000000
	for i, char in enumerate(mask):
		if char == "0":
			and_mask -= 2 ** (36 - (i+1))
		elif char == "1":
			or_mask += 2 ** (36 - (i+1))

def apply_mask(value):
	value &= and_mask
	return value | or_mask

def parse(line):
	cmd, value = line.split(" = ")
	if "mask" in cmd:
		set_mask(value.strip())
	else:
		cmd = cmd.strip()
		cmd = cmd.replace("mem[",'').replace("]",'')
		value = int(value)
		mem[cmd] = apply_mask(value)

def mem_resolve(idx, base_addr, value):
	global mem_mask
	global mem
	if idx == 36:
		mem[base_addr] = value
		return
	if mem_mask[idx] == "0":
		mem_resolve(idx+1, base_addr, value)
	elif mem_mask[idx] == "1":
		base_addr |= 2 ** (36 - (idx+1))
		mem_resolve(idx+1, base_addr, value)
	elif mem_mask[idx] == "X":
		mem_resolve(idx+1, base_addr & ~(2 ** (36 - (idx+1))), value)
		mem_resolve(idx+1, base_addr | 2 ** (36 - (idx+1)), value)

def parse2(line):
	global mem_mask
	cmd, value = line.split(" = ")
	if "mask" in cmd:
		mem_mask = value.strip()
	else:
		cmd = cmd.strip()
		cmd = cmd.replace("mem[",'').replace("]",'')
		mem_resolve(0, int(cmd), int(value))

if __name__ == "__main__":

	# Part 1 Solution
	with open("day14_input", 'r') as infile:
		for line in infile.readlines():
			parse(line)
	total = 0
	for key in mem.keys():
		total += mem[key]
	print(total)

	# Part 2 Solution
	mem = dict()
	with open("day14_input", 'r') as infile:
		for line in infile.readlines():
			parse2(line)
	total = 0
	for key in mem.keys():
		total += mem[key]
	print(total)

#!/usr/bin/python


signals = {}

def emulate(instructions):
	global signals
	while len(instructions) > 0:
		for inst in instructions:
			if "AND" in inst[0]:
				a,b = inst[0].split(" AND ")
				if a in signals:
					a = signals[a]
				else:
					try:
						a = int(a)
					except:
						a = None
				if b in signals:
					b = signals[b]
				else:
					try:
						b = int(b)
					except:
						b = None				
				if a != None and b != None:
					signals[inst[1]] = a & b & 0xFFFF
					instructions.remove(inst)
			elif "OR" in inst[0]:
				a,b = inst[0].split(" OR ")
				if a in signals:
					a = signals[a]
				else:
					try:
						a = int(a)
					except:
						a = None
				if b in signals:
					b = signals[b]
				else:
					try:
						b = int(b)
					except:
						b = None				
				if a != None and b != None:
					signals[inst[1]] = (a | b) & 0xFFFF
					instructions.remove(inst)
			elif "LSHIFT" in inst[0]:
				a,b = inst[0].split(" LSHIFT ")
				if a in signals:
					signals[inst[1]] = (signals[a] << int(b)) & 0xFFFF
					instructions.remove(inst)
			elif "RSHIFT" in inst[0]:
				a,b = inst[0].split(" RSHIFT ")
				if a in signals:
					signals[inst[1]] = (signals[a] >> int(b)) & 0xFFFF
					instructions.remove(inst)
			elif "NOT" in inst[0]:
				a = inst[0].replace("NOT ", '')
				if a in signals:
					signals[inst[1]] = ~signals[a] & 0xFFFF
					instructions.remove(inst)
			else:
				a = inst[0]
				if a in signals:
					signals[inst[1]] = signals[a]	
					instructions.remove(inst)
				else:
					try:
						a = int(a)
						signals[inst[1]] = a
						instructions.remove(inst)
					except:
						continue

def emulate_ovr(instructions):
	global signals
	while len(instructions) > 0:
		for inst in instructions:
			signals['b'] = 3176
			if "AND" in inst[0]:
				a,b = inst[0].split(" AND ")
				if a in signals:
					a = signals[a]
				else:
					try:
						a = int(a)
					except:
						a = None
				if b in signals:
					b = signals[b]
				else:
					try:
						b = int(b)
					except:
						b = None				
				if a != None and b != None:
					signals[inst[1]] = a & b & 0xFFFF
					instructions.remove(inst)
			elif "OR" in inst[0]:
				a,b = inst[0].split(" OR ")
				if a in signals:
					a = signals[a]
				else:
					try:
						a = int(a)
					except:
						a = None
				if b in signals:
					b = signals[b]
				else:
					try:
						b = int(b)
					except:
						b = None				
				if a != None and b != None:
					signals[inst[1]] = (a | b) & 0xFFFF
					instructions.remove(inst)
			elif "LSHIFT" in inst[0]:
				a,b = inst[0].split(" LSHIFT ")
				if a in signals:
					signals[inst[1]] = (signals[a] << int(b)) & 0xFFFF
					instructions.remove(inst)
			elif "RSHIFT" in inst[0]:
				a,b = inst[0].split(" RSHIFT ")
				if a in signals:
					signals[inst[1]] = (signals[a] >> int(b)) & 0xFFFF
					instructions.remove(inst)
			elif "NOT" in inst[0]:
				a = inst[0].replace("NOT ", '')
				if a in signals:
					signals[inst[1]] = ~signals[a] & 0xFFFF
					instructions.remove(inst)
			else:
				a = inst[0]
				if a in signals:
					signals[inst[1]] = signals[a]	
					instructions.remove(inst)
				else:
					try:
						a = int(a)
						signals[inst[1]] = a
						instructions.remove(inst)
					except:
						continue

if __name__ == "__main__":

	# Part 1 Solution

	instructions = []	
	with open("day7_input", "r") as infile:
		for line in infile.readlines():
			instructions.append(line.strip().split(" -> "))	
	emulate(instructions)						
	print signals['a']
	
	# Part 2 Solution
	instructions = []	
	signals = {}
	with open("day7_input", "r") as infile:
		for line in infile.readlines():
			instructions.append(line.strip().split(" -> "))
	emulate_ovr(instructions)
	print signals['a']
	

	

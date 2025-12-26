#!/usr/bin/python


if __name__ == "__main__":

	candidate_min = float('inf')
	candidate_max = 0

	input_buffer = []

	regs = {'w' : 0,
		'x' : 0,
		'y' : 0,
		'z' : 0}
	
	def inp(x):
		regs[x] = input_buffer.pop(0)
	
	def add(x,y):
		if y in regs:
			regs[x] += regs[y]
		else:
			regs[x] += int(y)

	def mod(x,y):
		if y in regs:
			regs[x] %= regs[y]
		else:
			regs[x] %= int(y)	

	def div(x,y):
		if y in regs:
			regs[x] //= regs[y]
		else:
			regs[x] //= int(y)	

	def mul(x,y):
		if y in regs:
			regs[x] *= regs[y]
		else:
			regs[x] *= int(y)	

	def eql(x,y):
		if y in regs:
			regs[x] = 1 if regs[x] == regs[y] else 0
		else:
			regs[x] = 1 if regs[x] == int(y) else 0
	
	ops = {'inp':inp,'add':add,'mod':mod,'div':div,'mul':mul,'eql':eql}

	# Part 1 Solution
	digits = [1,2,3,4,5,6,7,8,9]
	for d1 in digits:
		for d2 in digits:
			for d3 in digits:
				for d4 in digits:
					for d5 in digits:
						if ((((((d1+15)*26+(d2+16))*26)+(d3+4))*26+(d4+14))%26)-8 == d5:
							for d6 in digits:
								if (((((d1+15)*26+(d2+16))*26+(d3+4))*26+(d4+14))//26)%26 - 10 == d6:
									for d7 in digits:
										for d8 in digits:
											if (((((d1+15)*26+(d2+16))*26+(d3+4))*26+(d4+14))//26//26*26 + (d7+1)) % 26 - 3 == d8:
												for d9 in digits:
													for d10 in digits:
														if (((((((d1+15)*26+(d2+16))*26+(d3+4))*26+(d4+14))//26//26*26+(d7+1))//26)*26+(d9+3))%26-4 == d10:
															for d11 in digits:
																for d12 in digits:
																	if ((((((((d1+15)*26+(d2+16))*26+(d3+4))*26+(d4+14))//26//26*26+(d7+1))//26)*26+(d9+3))//26*26+(d11+5))%26-5 == d12:
																		for d13 in digits:
																			if (((((((((d1+15)*26+(d2+16))*26+(d3+4))*26+(d4+14))//26//26*26+(d7+1))//26)*26+(d9+3))//26*26+(d11+5))//26)%26-8 == d13:
																				for d14 in digits:
																					if (((((((((d1+15)*26+(d2+16))*26+(d3+4))*26+(d4+14))//26//26*26+(d7+1))//26)*26+(d9+3))//26*26+(d11+5))//26//26) % 26 - 11 == d14:
															
														
																						regs = {'w' : 0,
																							'x' : 0,
																							'y' : 0,
																							'z' : 0}
																						input_buffer=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14]
																						txtnum = ''.join([str(x) for x in input_buffer])
																						cmds = []
																						with open("day24_input") as infile:
																							for line in infile.readlines():
																								if ";" in line:
																									cmd = line.strip().split(";")
																									cmds.append(cmd[0])
																								else:
																									cmds.append(line.strip())
																						for cmd in cmds:
																							cmd = cmd.split(' ')
																							if len(cmd) == 2:
																								ops[cmd[0]](cmd[1])
																							else:
																								ops[cmd[0]](cmd[1],cmd[2])
																						if regs['z'] == 0:
																							candidate_max = max(candidate_max,int(txtnum))
																							candidate_min = min(candidate_min,int(txtnum))
	print(candidate_max)
	print(candidate_min)																							
		
	
	# Part 2 Solution



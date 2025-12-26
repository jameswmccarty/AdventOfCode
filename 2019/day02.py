#!/usr/bin/python


def run(p):
	i = 0
	while True:
		op = p[i]
		if op == 99:
			return p
		elif op == 1:
			p[p[i+3]] = p[p[i+1]] + p[p[i+2]]
		elif op == 2:
			p[p[i+3]] = p[p[i+1]] * p[p[i+2]]
		i += 4			


if __name__ == "__main__":
	
	# Tests

	"""
	program = [1,9,10,3,2,3,11,0,99,30,40,50]
	program = run(program)
	print(program)
	"""

	# Part 1 Solution
	with open("day02_input", 'r') as infile:
		program = infile.readline().strip()
		program = program.split(',')
		program = [ int(x) for x in program ]
		program[1] = 12
		program[2] = 2
		program = run(program)
		print(program[0])

	# Part 2 Solution
	result = 0
	target = 19690720
	noun = 100
	verb = 99
	while result != target and verb > 0:
		noun = noun - 1
		if noun == 0:
			verb = verb - 1
			noun = 99
		with open("day02_input", 'r') as infile:
			program = infile.readline().strip()
			program = program.split(',')
			program = [ int(x) for x in program ]
			program[1] = noun
			program[2] = verb
			program = run(program)
			result = program[0]
	print(100 * noun + verb)


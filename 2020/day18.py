#!/usr/bin/python

numbers = [ chr(i) for i in range(48,58) ]

token_stack = []
P = []

def eqn_parse(line, idx):
	total = 0
	last_op = None
	current_num = None
	while idx < len(line):
		char = line[idx]
		if char == "*" or char == "+":
			last_op = char
		elif char in numbers:
			current_num = int(char)
		elif char == "(":
			current_num, offset = eqn_parse(line[idx+1:], 0)
			idx += offset
		elif char == ")":
			return (total, idx+1)
		if current_num != None and last_op == None:
			total = current_num
			current_num = None
		elif current_num != None and last_op != None:
			if last_op == "*":
				total *= current_num
			elif last_op == "+":
				total += current_num
			current_num = None
			last_op = None
		idx += 1
	return (total, idx)

def tokenize(line):
	for char in line:
		if char == "(" or char == ")":
			token_stack.append(char)
		elif char in numbers:
			token_stack.append(char)
		elif char == "+":
			token_stack.append(char)
		elif char == "*":
			token_stack.append(char)

def make_postfix():
	stack = []
	while len(token_stack) > 0:
		current = token_stack.pop(0)
		if current in numbers:
			P.append(current)
		elif current == "(":
			stack.append(current)
		elif current == ")":
			while len(stack) > 0 and stack[-1] != "(":
				P.append(stack.pop())
			if stack[-1] == "(":
				stack.pop()
		elif current ==  "+" or current == "*":
			prec = 0
			if current == "+":
				prec = 1
			if len(stack) == 0 or stack[-1] == "(":
				stack.append(current)
			else:
				while len(stack) > 0 and stack[-1] != "(" and (stack[-1] != "*" and prec == 0):
					P.append(stack.pop())
				stack.append(current)
	while len(stack) > 0:
		P.append(stack.pop())

def postfix_eval():
	stack = []
	while len(P) > 0:
		current = P.pop(0)
		if current in numbers:
			stack.append(int(current))
		else:
			a = stack.pop()
			b = stack.pop()
			if current == "+":
				stack.append(a+b)
			elif current == "*":
				stack.append(a*b)
	return stack.pop()

if __name__ == "__main__":


	# Part 1 Solution
	total = 0

	with open("day18_input", 'r') as infile:
		for line in infile.readlines():
			t, idx = eqn_parse(line.strip(),0)
			total += t
	print(total)


	# Part 2 Solution
	total = 0
	
	with open("day18_input", 'r') as infile:
		idx = 0
		for line in infile.readlines():
			if line.strip() != '':
				token_stack = []
				P = []
				tokenize(line.strip())
				make_postfix()
				total += postfix_eval()
	print(total)

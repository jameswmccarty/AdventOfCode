#!/usr/bin/python


import math

def concat_statements(s1,s2):
	return ['['] + s1 + s2 + [']']

def build_statement(string):
	statement = []
	for char in string:
		if char in "0123456789":
			statement.append(int(char))
		elif char in "[]":
			statement.append(char)
	return statement

def find_explodable_index(statement):
	l_count = 0
	for idx,char in enumerate(statement):
		if char == '[':
			l_count += 1
		elif char == ']':
			l_count -= 1
		if l_count >= 5 and isinstance(statement[idx+1],int):
			return idx+1
	return -1

def explode_at_index(statement,idx):
	l_value = statement[idx]
	r_value = statement[idx+1]
	out_statement = statement[0:idx-1] + [0] + statement[idx+3:]
	for l_idx in range(idx-2,-1,-1):
		if isinstance(out_statement[l_idx],int):
			out_statement[l_idx] += l_value
			break
	for r_idx in range(idx,len(out_statement)):
		if isinstance(out_statement[r_idx],int):
			out_statement[r_idx] += r_value
			break
	return out_statement

def find_splitable_index(statement):
	for idx,char in enumerate(statement):
		if isinstance(char,int) and char >= 10:
			return idx
	return -1

def split_at_index(statement,idx):
	l_value = statement[idx]//2
	r_value = math.ceil(statement[idx]/2)
	return statement[0:idx] + ['[',l_value,r_value,']'] + statement[idx+1:]

def solve_statement(statement):
	solved = False
	while not solved:
		solved = True
		idx = find_explodable_index(statement)
		if idx > -1:
			solved = False
			statement = explode_at_index(statement,idx)
		else:
			while True:
				idx = find_splitable_index(statement)
				if idx > -1:
					solved = False
					statement = split_at_index(statement,idx)
					break
				else:
					break
	return statement

def find_magnitude(s):
	while len(s) > 3:
		for idx in range(len(s)-3):
			if s[idx] == '[' and isinstance(s[idx+1],int) and isinstance(s[idx+2],int) and s[idx+3] == ']':
				new_val = s[idx+1]*3 + s[idx+2]*2
				s = s[0:idx] + [new_val] + s[idx+4:]
				break
	return s[0]

if __name__ == "__main__":

	# Part 1 Solution
	lines = []
	with open("day18_input","r") as infile:
		for line in infile.readlines():
			lines.append(build_statement(line.strip()))
	working_statement = lines.pop(0)

	while len(lines) > 0:
		working_statement = concat_statements(working_statement,lines[0])
		lines = lines[1:]
		working_statement = solve_statement(working_statement)
	print(find_magnitude(working_statement))

	# Part 2 Solution
	hw_max = 0
	lines = []
	with open("day18_input","r") as infile:
		for line in infile.readlines():
			lines.append(build_statement(line.strip()))
	for line1 in lines:
		for line2 in lines:
			if line1 != line2:
				working_statement = concat_statements(line1,line2)
				working_statement = solve_statement(working_statement)
				hw_max = max(find_magnitude(working_statement),hw_max)
				working_statement = concat_statements(line2,line1)
				working_statement = solve_statement(working_statement)
				hw_max = max(find_magnitude(working_statement),hw_max)
	print(hw_max)



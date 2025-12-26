#!/usr/bin/python


class Node:

	def __init__(self, name, weight):
		self.name = name
		self.parent = None
		self.children = []
		self.weight = weight
		
	def total_weight(self):
		total = self.weight
		for sub in self.children:
			total += sub.total_weight()
		return total
		
	def is_broken(self):
		subs = set()
		if len(self.children) == 0:
			return False
		for child in self.children:
			subs.add(child.total_weight())
		if len(subs) > 1:
			return True
		return False
		
	def oob_child(self):
		weights = []
		for child in self.children:
			weights.append(child.total_weight())
		unique = None
		for i in range(len(weights)):
			if weights[i] not in weights[i+1:]:
				unique = weights[i]
				break
		return self.children[i]	

if __name__ == "__main__":

	# Part 1 Solution

	programs = []
	with open("day7_input", "r") as infile:
		for line in infile.readlines():
			line = line.strip()
			if "->" in line:
				name_weight, subs = line.split(" -> ")
			else:
				name_weight = line
				subs = ''
			name, weight = name_weight.split(" ")
			weight = int(weight.replace("(", '').replace(")", ''))
			programs.append((Node(name, weight), subs.strip().split(", ")))
	
	for program in programs:
		if len(program[1]) != 0:
			for sub in program[1]:
				for p in programs:
					if p[0].name == sub:
						p[0].parent = program[0]
						program[0].children.append(p[0])
						
	root = None						
	for program in programs:
		if program[0].parent == None:
			root = program[0]
			print program[0].name
	
	# Part 2 Solution
	found = True
	while root.is_broken():
		root = root.oob_child()
	delta_set = set()
	for child in root.parent.children:
		delta_set.add(child.total_weight())
	m = delta_set.pop()
	n = delta_set.pop()
	delta = max(m,n) - min(m,n)
	if root.total_weight() == max(m,n):
		print root.weight - delta
	else:
		print root.weight + delta


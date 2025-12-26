#!/usr/bin/python


class Program:

	def __init__(self, name):
		self.name = name
		self.connected = []
	
	def connect(self, prog):
		self.connected.append(prog)
		
	def reachable(self, goal, visited):
		if self.name == goal:
			return True
		if self in visited:
			return False
		visited.add(self)
		for child in self.connected:
			if child.reachable(goal, visited):
				return True
		return False

	def group_members(self,seen):
		if self in seen:
			return None
		seen.add(self)
		for child in self.connected:
			ret = child.group_members(seen)
			if ret != None:
				seen = seen.union(ret)
		return seen

if __name__ == "__main__":

	# Part 1 Solution
	
	nodes = {}
	
	with open("day12_input", "r") as infile:
		for line in infile.readlines():
			id, paths = line.split("<->")
			p_node = Program(id.strip())
			nodes[id.strip()] = p_node
			
	with open("day12_input", "r") as infile:
		for line in infile.readlines():
			id, paths = line.split("<->")
			id = id.strip()
			for pipe in paths.strip().split(","):
				nodes[id].connect(nodes[pipe.strip()])
	
	connected = 0
	for prog in nodes.values():
		if prog.reachable("0", set()):
			connected += 1
	print connected
	
	# Part 2 Solution
	
	num_groups = 0
	while len(nodes) != 0:
		prog = nodes.values()[0]
		to_rmv = prog.group_members(set())
		num_groups += 1
		while len(to_rmv) != 0:
			nodes.pop(to_rmv.pop().name)
	print num_groups

	

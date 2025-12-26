#!/usr/bin/python


class Node:

	def __init__(self):
		self.m_size = 0
		self.c_size = 0
		self.metadata = []
		self.children = []
	
	def add_meta(self, data):
		self.metadata.append(data)
		self.m_size = len(self.metadata)
	
	def add_child(self, child):
		self.children.append(child)
		self.c_size = len(self.children)
	
	def sum_meta(self):
		sum = 0
		for child in self.children:
			sum += child.sum_meta();
		for entry in self.metadata:
			sum += entry
		return sum
		
	def sum_meta2(self):
		sum = 0
		# if no children, return sum of metadata entries
		if self.c_size == 0:
			for entry in self.metadata:
				sum += entry
			return sum
		# return sum of child node metadata.  
		# own metadata acts as index to child nodes to sum
		else:
			for idx in self.metadata:
				# exclude out of range nodes
				if(idx-1 < self.c_size):
					sum += self.children[idx-1].sum_meta2()
			return sum

def parse_node(root, stream):
	if len(stream) == 0:
		return stream
	num_nodes = stream[0]
	num_meta  = stream[1]
	stream    = stream[2:]
	
	for i in range(num_nodes):
		root.add_child(Node())
		stream = parse_node(root.children[i], stream)
	
	for i in range(num_meta):
		root.add_meta(stream[0])
		stream = stream[1:]
	
	return stream
	
	

if __name__ == "__main__":

	#Part 1 Solution
	
	stream = [] # in sequence list of numbers in input file
	root = Node()
	
	with open("day8_input", "r") as infile:
		stream = infile.read().strip().split(" ")
	stream = [ int(x) for x in stream ]
	parse_node(root, stream)
	print root.sum_meta()
	
	#Part 2 Solution
	
	print root.sum_meta2()
		
	
	

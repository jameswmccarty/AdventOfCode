#!/usr/bin/python


class inode:

	nodes_by_name = dict()

	def __init__(self,line):
		name, contents = line.split(':')
		self.name = name
		self.nodes_by_name[name] = self
		self.op = None
		self.left = None
		self.right = None
		self.contents = None
		if '+' in contents:
			self.op = '+'
		if '-' in contents:
			self.op = '-'
		if '*' in contents:
			self.op = '*'
		if '/' in contents:
			self.op = '/'
		if self.op != None:
			left,right = contents.split(self.op)
			self.left = left.strip()
			self.right = right.strip()
		if self.op == None:
			self.contents = int(contents.strip())

	def value(self):
		if self.op == None:
			return self.contents
		else:
			if self.op == '+':
				return self.nodes_by_name[self.left].value() + self.nodes_by_name[self.right].value()
			if self.op == '-':
				return self.nodes_by_name[self.left].value() - self.nodes_by_name[self.right].value()
			if self.op == '*':
				return self.nodes_by_name[self.left].value() * self.nodes_by_name[self.right].value()
			if self.op == '/':
				return self.nodes_by_name[self.left].value() // self.nodes_by_name[self.right].value()

	def eq(self):
		#print(self.nodes_by_name[self.left].value(),self.nodes_by_name[self.right].value())
		if self.nodes_by_name[self.left].value() == self.nodes_by_name[self.right].value():
			return True
		return False

if __name__ == "__main__":

	node_bin = dict()

	# Part 1 Solution
	with open('day21_input','r') as infile:
		for line in infile.readlines():
			a_node = inode(line.strip())
			node_bin[a_node.name] = a_node
	print(node_bin["root"].value())

	# Part 2 Solution

	is_left = False
	node_bin["humn"].contents = 0
	left_init  = node_bin[node_bin["root"].left].value()
	node_bin["humn"].contents = 1000
	if node_bin[node_bin["root"].left].value() != left_init:
		is_left = True

	l,r = 0,2**64
	while l <= r:
		mid = (l+r) // 2
		node_bin["humn"].contents = mid
		if node_bin["root"].eq():
			while node_bin["root"].eq():
				mid -= 1
				node_bin["humn"].contents = mid
			print(mid+1)
			break
		if is_left:
			if node_bin[node_bin["root"].left].value() > node_bin[node_bin["root"].right].value():
				l = mid
			else:
				r = mid
		elif not is_left:
			if node_bin[node_bin["root"].right].value() < node_bin[node_bin["root"].left].value():
				r = mid
			else:
				l = mid


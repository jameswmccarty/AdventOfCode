#!/usr/bin/python


class inode:

	def __init__(self, name, isDir, parent, size):
		self.name = name
		self.isDir = isDir
		self.size = size
		self.contents = []
		self.parent = parent
	
	def get_size(self):
		if not self.isDir:
			return self.size
		return sum( [ x.get_size() for x in self.contents ] )

	def traverse(self,lead=''):
		print(lead,self.name, self.size)
		if self.isDir:
			for entry in self.contents:
				entry.traverse(lead=lead+'  ')

head_node = None
all_dirs = []

def parse_line(line):
	global head_node
	if '$ cd' in line:
		command = line.split(' ')
		if head_node == None:
			head_node = inode(command[2], True, None, 0)
		elif command[2] == '..':
			head_node = head_node.parent
		elif command[2] == '/':
			while head_node.parent != None:
				head_node = head_node.parent
		else:
			for entry in head_node.contents:
				if command[2] == entry.name and entry.isDir:
					head_node = entry
					return
	elif 'dir' in line:
		line = line.split(' ')
		new_dir = inode(line[1], True, head_node, 0)
		head_node.contents.append(new_dir)
		all_dirs.append(new_dir)
	elif '$ ls' in line or '$ dir' in line:
		return
	else: # is a file and size
		line = line.split(' ')
		head_node.contents.append(inode(line[1], False, head_node, int(line[0])))

if __name__ == "__main__":

	# Part 1 Solution

	with open("day07_input","r") as infile:
		for line in infile.readlines():
			parse_line(line.strip())
	print(sum( [ x.get_size() if x.get_size() <= 100000 else 0 for x in all_dirs ]))

	# Part 2 Solution
	parse_line("$ cd /")
	used_space = head_node.get_size()
	current_free = 70000000 - used_space
	needed_space = 30000000 - current_free
	print(sorted([ x.get_size() if x.get_size() >= needed_space else float('inf') for x in all_dirs ])[0])

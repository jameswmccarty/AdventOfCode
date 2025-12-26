#!/usr/bin/python


from collections import deque

class inode:

	def __init__(self,value):
		self.value = value

if __name__ == "__main__":

	orig_orders = dict()
	coordinates = deque()
	base_value  = None

	# Part 1 Solution
	with open('day20_input','r') as infile:
		for idx,line in enumerate(infile.read().strip().split('\n')):
			node = inode(int(line))
			coordinates.append(node)
			orig_orders[idx] = node
			if node.value == 0:
				base_value = node

	for idx in range(len(coordinates)):
		to_move = orig_orders[idx]
		if to_move.value != 0:
			old_index = coordinates.index(to_move)
			next_value = inode(to_move.value)
			coordinates.remove(to_move)
			orig_orders[idx] = next_value
			new_index = (old_index + next_value.value) % len(coordinates)
			if new_index == 0:
				coordinates.append(next_value)
			else:
				coordinates.insert(new_index,next_value)

	base_idx = coordinates.index(base_value)
	print(sum([coordinates[(base_idx+1000)%len(coordinates)].value,coordinates[(base_idx+2000)%len(coordinates)].value,coordinates[(base_idx+3000)%len(coordinates)].value]))

	# Part 2 Solution

	orig_orders = dict()
	coordinates = deque()
	base_value  = None

	with open('day20_input','r') as infile:
		for idx,line in enumerate(infile.read().strip().split('\n')):
			node = inode(int(line)*811589153)
			coordinates.append(node)
			orig_orders[idx] = node
			if node.value == 0:
				base_value = node

	for _ in range(10):
		for idx in range(len(coordinates)):
			to_move = orig_orders[idx]
			if to_move.value != 0:
				old_index = coordinates.index(to_move)
				next_value = inode(to_move.value)
				coordinates.remove(to_move)
				orig_orders[idx] = next_value
				new_index = (old_index + next_value.value) % len(coordinates)
				if new_index == 0:
					coordinates.append(next_value)
				else:
					coordinates.insert(new_index,next_value)

	base_idx = coordinates.index(base_value)
	print(sum([coordinates[(base_idx+1000)%len(coordinates)].value,coordinates[(base_idx+2000)%len(coordinates)].value,coordinates[(base_idx+3000)%len(coordinates)].value]))

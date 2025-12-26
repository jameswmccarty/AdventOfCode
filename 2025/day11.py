#!/usr/bin/python

# Advent of Code 2025 Day 11

class Node:

	def __init__(self, label):
		self.label = label
		self.children = set()

	def link(self, a_node):
		self.children.add(a_node)

ways1_count = 0
def out_search(node, target="out"):
	global ways1_count
	if node.label == target:
		ways1_count += 1
		return
	for child in node.children:
		out_search(child)

if __name__ == "__main__":

	Nodes = dict()
	with open("day11_input", "r") as infile:
		for line in infile:
			parent, children = line.strip().split(':')
			children = children.strip().split()
			if parent not in Nodes:
				Nodes[parent] = Node(parent)
			for child in children:
				if child not in Nodes:
					Nodes[child] = Node(child)
				Nodes[parent].link(Nodes[child])

	out_search(Nodes["you"])
	print(ways1_count)


#!/usr/bin/python


import graphviz
from collections import deque

class Node:

	def __init__(self,name):
		self.name = name
		self.connections = set()


def bfs(node,nodes):
	seen = set()
	q = deque()
	q.append(node)
	seen.add(node)
	while q:
		current = q.popleft()
		for edge in nodes[current]:
			if edge not in seen:
				seen.add(edge)
				q.append(edge)
	return len(seen)

cut_candidates = set()
def bfs2(node,nodes):
	seen = set()
	dist_map = dict()
	q = deque()
	q.append((node,0))
	seen.add(node)
	while q:
		current,dist = q.popleft()
		for edge in nodes[current]:
			if dist not in dist_map:
				dist_map[dist] = list()
			if edge not in seen:
				seen.add(edge)
				q.append((edge,dist+1))
				t = (current,edge)
				dist_map[dist].append('-'.join(sorted(t)))
	for dist in dist_map:
		if len(dist_map[dist]) == 3:
			unique = set()
			for entry in dist_map[dist]:
				for item in entry.split('-'):
					unique.add(item)
			if len(unique) == 6:
				cut_candidates.add(','.join(sorted(dist_map[dist])))

if __name__ == "__main__":

	nodes = dict()
	connections = list()
	seen = set()

	f = graphviz.Digraph(filename = "day25_graph.gv")

	# Part 1 Solution
	with open("day25_input", "r") as infile:
		for line in infile:
			connections.append(line.strip())
			line = line.strip().replace(":",'')
			for item in line.split():
				if item not in seen:
					seen.add(item)
					f.node(item,item)
					nodes[item] = set()

	for line in connections:
		source,dests = line.split(":")
		for entry in dests.split():
			if not (entry in nodes[source] or source in nodes[entry]):
				f.edge(entry,source)
				nodes[source].add(entry)
				nodes[entry].add(source)


	# Manually determine the links to cut
	
	#f.view()
	
	#kbr-bbg	
	#fht-vtt
	#tdk-czs
	
	#nodes['hfx'].discard('pzl')
	#nodes['pzl'].discard('hfx')
	#nodes['bvb'].discard('cmg')
	#nodes['cmg'].discard('bvb')
	#nodes['nvd'].discard('jqt')
	#nodes['jqt'].discard('nvd')
	
	for node in nodes:
		bfs2(node,nodes)

	for trial in cut_candidates:
		nodes = dict()
		connections = list()
		seen = set()
		with open("day25_input", "r") as infile:
			for line in infile:
				connections.append(line.strip())
				line = line.strip().replace(":",'')
				for item in line.split():
					if item not in seen:
						seen.add(item)
						nodes[item] = set()

		for line in connections:
			source,dests = line.split(":")
			for entry in dests.split():
				if not (entry in nodes[source] or source in nodes[entry]):
					nodes[source].add(entry)
					nodes[entry].add(source)




		a,b,c = trial.split(',')
		a1,a2 = a.split('-')
		b1,b2 = b.split('-')
		c1,c2 = c.split('-')
		nodes[a1].discard(a2)
		nodes[a2].discard(a1)
		nodes[b1].discard(b2)
		nodes[b2].discard(b1)
		nodes[c1].discard(c2)
		nodes[c2].discard(c1)
	
		g1,g2 = bfs(a1,nodes),bfs(a2,nodes)
		if g1 != g2:
			print(g1*g2)
			exit()



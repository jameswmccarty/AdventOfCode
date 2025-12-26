#!/usr/bin/python

import math

class chem:

	def __init__(self, qty, name):
		self.qty = int(qty)
		self.name = name
		self.prereqs = []

	def add_prereq(self, qty, chem):
		self.prereqs.append((int(qty), chem))

def parse_line(line):
	pre, final = line.split(" => ")
	pre = pre.split(", ")
	qty, name = final.split(" ")
	out = chem(qty, name)
	for p in pre:
		qty, name = p.split(" ")
		out.add_prereq(qty, name)
	return out

surplus = dict()
def find_cost(c_name, ammount, chems):
	global surplus
	if c_name == "ORE":
		return ammount
	current_chem = None
	for chem in chems:
		if chem.name == c_name:
			current_chem = chem
			break		
	cost = 0
	scale = 1
	if current_chem.name in surplus:
		delta = min(surplus[current_chem.name], ammount)
		ammount -= delta
		surplus[current_chem.name] -= delta
	if ammount == 0:
		return 0
	if current_chem.qty <= ammount:
		scale = math.ceil(ammount / current_chem.qty)
	if ammount <= current_chem.qty:
		surplus[current_chem.name] = current_chem.qty - ammount
	elif scale * current_chem.qty >= ammount:
		surplus[current_chem.name] = scale * current_chem.qty - ammount
	if ammount > 0:
		for p in current_chem.prereqs:
			q, n = p
			cost += find_cost(n, q*scale, chems)
	return cost

# Was off by one on examples, works for input
def fuel_search(cap, target, chems):
	global surplus
	l = 0
	r = 1000000000000
	while l <= r:
		m = (l + r) // 2
		surplus = dict()
		cost = find_cost(target, m, chems)
		if cost <= cap:
			l = m + 1
		elif cost > cap:
			r = m - 1
		else:
			return m
	return m	

if __name__ == "__main__":

	# Part 1 Solution
	chems = []
	with open("day14_input", 'r') as infile:
		for line in infile.readlines():
			chems.append(parse_line(line.strip()))
	target = None	
	for t in chems:
		if t.name == "FUEL":
			target = t
			break
	cost = find_cost("FUEL", 1, chems)
	print(cost)

	# Part 2 Solution
	print(fuel_search(1000000000000, "FUEL", chems))

		


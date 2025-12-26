#!/usr/bin/python


def eq(x,y):
	return x == y

def gt(x,y):
	return x > y

def lt(x,y):
	return x < y


class Sue:

	options = { "children" : eq, "cats" : gt, "samoyeds" : eq, "pomeranians" : lt, "akitas" : eq, "vizslas" : eq, "goldfish" : lt, "trees" : gt, "cars" : eq, "perfumes" : eq }

	def __init__(self, *argv, **kwargs):
		for key, value in kwargs.iteritems():
			if key in self.options:
				setattr(self, key, int(value))
				
	def match(self, items):
		for item in items:
			if hasattr(self, item) and getattr(self, item) != items[item]:
				return False
		return True
		
	def match2(self, items):
		for item in items:
			if hasattr(self, item) and not self.options[item](getattr(self, item), items[item]):
				return False
		return True

if __name__ == "__main__":

	# Part 1 Solution

	all_sue = []

	unk_sue = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3,  "cars": 2, "perfumes": 1 }
	
	with open("day16_input", "r") as infile:
		for line in infile.readlines():
			line = line.split(",")
			first = line[0].split(":")
			second = line[1].split(":")
			third = line[2].split(":")
			kwargs = { first[1].strip():first[2].strip(), second[0].strip():second[1].strip(), third[0].strip():third[1].strip() }
			all_sue.append(Sue(**kwargs))
			
	for idx, sue in enumerate(all_sue):
		if sue.match(unk_sue):
			print idx + 1
			
	# Part 2 Solution

	for idx, sue in enumerate(all_sue):
		if sue.match2(unk_sue):
			print idx + 1

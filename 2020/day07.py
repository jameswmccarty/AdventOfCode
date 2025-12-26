#!/usr/bin/python


Bags = dict()

class Bag:

	def __init__(self, color, contents):
		self.color = color
		# contents is a list of (qty, color)
		self.contents = contents

	def can_hold(self, color):
		for item in self.contents:
			if item[1] == None:
				break
			if item[1] == color:
				return True
			if Bags[item[1]].can_hold(color):
				return True
		return False
		
	def hold_reqs(self):
		total = 0
		for item in self.contents:
			if item[1] != None:
				total += item[0] + item[0]*Bags[item[1]].hold_reqs()
			else:
				total += item[0]
		return total

def parse(line):
	color, contents = line.split("bags contain")
	color = color.strip()
	contents = contents.replace(".",'').strip()
	if "," in contents:
		contents = contents.split(",")
	else:
		contents = [contents]
	parsed_contents = []
	for item in contents:
		if item == "no other bags":
			parsed_contents.append((0, None))
		else:
			item = item.strip().split(" ")
			parsed_contents.append((int(item[0]), item[1]+" "+item[2]))
	Bags[color] = Bag(color, parsed_contents)

if __name__ == "__main__":

	# Part 1 Solution
	with open("day07_input", 'r') as infile:
		for line in infile.readlines():
			parse(line)

	print(sum(Bags[bag].can_hold("shiny gold") for bag in Bags.keys()))

	# Part 2 Solution
	print(Bags["shiny gold"].hold_reqs())


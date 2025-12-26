#!/usr/bin/python

# Advent of Code 2024 Day 03

import re

part_one_re = "mul\([0-9]{1,3},[0-9]{1,3}\)"
part_two_re = "mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"

if __name__ == "__main__":

	# Part 1 Solution
	with open("day03_input", "r") as infile:
		mem = infile.read()

	matches = re.findall(part_one_re, mem)
	total = 0
	for entry in matches:
		entry = entry[4:-1]
		a,b = entry.split(",")
		total += int(a) * int(b)
	print(total)

	# Part 2 Solution
	matches = re.findall(part_two_re, mem)
	total = 0
	doing = True
	for entry in matches:
		if entry == "do()":
			doing = True
		if entry == "don't()":
			doing = False
		if "mul" in entry and doing:
			entry = entry[4:-1]
			a,b = entry.split(",")
			total += int(a) * int(b)
	print(total)

	# Part 1 Solution (non-regex)
	with open("day03_input", "r") as infile:
		mem = infile.read()
	total = 0
	while mem:
		if mem.startswith("mul("):
			idx = 4
			while mem[idx] != ')':
				idx += 1
			statement = mem[4:idx]
			try:
				if any(x not in "0123456789," for x in statement):
					raise Exception()
				a,b = statement.split(",")
				if len(a) not in (1,2,3) or len(b) not in (1,2,3):
					raise Exception()
				total += int(a)*int(b)
			except:
				pass
		mem = mem[1:]
	#print(total)

	# Part 2 Solution (non-regex)
	with open("day03_input", "r") as infile:
		mem = infile.read()
	total = 0
	doing = True
	while mem:
		if mem.startswith("don't()"):
			doing = False
		if mem.startswith("do()"):
			doing = True
		if mem.startswith("mul("):
			idx = 4
			while mem[idx] != ')':
				idx += 1
			statement = mem[4:idx]
			try:
				if any(x not in "0123456789," for x in statement):
					raise Exception()
				a,b = statement.split(",")
				if len(a) not in (1,2,3) or len(b) not in (1,2,3):
					raise Exception()
				if doing:
					total += int(a)*int(b)
			except:
				pass
		mem = mem[1:]
	#print(total)

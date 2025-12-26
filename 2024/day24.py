#!/usr/bin/python

# Advent of Code 2024 Day 24

wires = dict()
rules = dict()


if __name__ == "__main__":

	# Part 1 Solution
	with open("day24_input", "r") as infile:
		for line in infile:
			if ':' in line:
				wire, val = line.strip().split(':')
				wires[wire.strip()] = True if val.strip() == '1' else False
			if '->' in line:
				rule_pair, target = line.strip().split('->')
				rule_pair = rule_pair.split()
				for v in [rule_pair[0], rule_pair[-1], target]:
					if v not in wires:
						wires[v.strip()] = None
				rules[target.strip()] = [ x.strip() for x in rule_pair ]

	while None in wires.values():
		for trial in [ entry for entry in rules if wires[entry] == None ]:
			left, op, right = rules[trial]
			if wires[left] != None and wires[right] != None:
				if op == 'XOR': wires[trial] = wires[left] ^ wires[right]
				if op == 'AND': wires[trial] = wires[left] and wires[right]
				if op == 'OR':  wires[trial] = wires[left] or wires[right]

	bit_array = [ '1' if wires[v] else '0' for v in sorted(k for k in wires.keys() if k[0] == 'z') ]
	print(int(''.join(bit_array)[::-1],2))

	# Part 2 Solution


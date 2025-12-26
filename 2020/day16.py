#!/usr/bin/python



def build_rule(line, idx):
	valid_set = set()
	departure_flag = False
	if "departure" in line:
		departure_flag = True
	line = line[line.index(":")+1:].strip()
	ranges = line.split(" or ")
	for r in ranges:
		lo, hi = r.split("-")
		for x in range(int(lo),int(hi)+1):
			valid_set.add(x)
	return (valid_set, departure_flag, idx)


if __name__ == "__main__":

	rules = []
	yours = []
	nearby = []
	
	seen_yours = False

	# Part 1 Solution
	with open("day16_input", 'r') as infile:
		idx = 0
		for line in infile.readlines():
			if line.strip() == '':
				continue
			elif ":" in line and "ticket" not in line:
				rules.append(build_rule(line.strip(), idx))
				idx += 1
			elif "ticket" in line:
				if "nearby" in line:
					seen_yours = True
			else:
				if not seen_yours:
					yours = [ int(x) for x in line.strip().split(",") ]
				else:
					nearby.append([int(x) for x in line.strip().split(",")])

	errors = 0
	for ticket in nearby:
		for value in ticket:
			valid = False
			for rule in rules:
				if value in rule[0]:
					valid = True
			if not valid:
				errors += value
	print(errors)

	
	# Part 2 Solution
	for ticket in nearby:
		for value in ticket:
			valid = False
			for rule in rules:
				if value in rule[0]:
					valid = True
			if not valid:
				nearby.remove(ticket)

	mapping = []
	for i in range(len(yours)):
		mapping.append({ x for x in range(len(yours)) })

	last = float('inf')
	
	while sum(len(x) for x in mapping) != last:
		last = sum(len(x) for x in mapping)
		for a, x in enumerate(mapping):
			if len(x) == 1:
				for b, y in enumerate(mapping):
					if a != b:
						mapping[b].discard(list(x)[0])
		for ticket in nearby:
			for i, value in enumerate(ticket):
				for rule in rules:
					if value not in rule[0]:
						mapping[i].discard(rule[2])
	
	depart_list = [ x[2] for x in rules if x[1] ]
	field_idx = [ x for x, a in enumerate(mapping) if len(list(a)) >= 1 and list(a)[0] in depart_list ]
	total = 1
	for idx in field_idx:
		total *= yours[idx]
	print(total)




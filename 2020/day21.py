#!/usr/bin/python

allergens = dict()
foods = dict()
foods_list = []

def parse(line):
	left, right = line.split("(contains ")
	right = right.strip(")").strip().split(", ")
	left  = left.strip().split(" ")
	
	for item in right:
		if item in allergens:
			allergens[item].append(set(left))
		else:
			allergens[item] = [ set(left) ]

	foods_list.append(set(left))
	
	for item in left:
		if item in foods:
			foods[item].update(set(right))
		else:
			foods[item] = set(right)


if __name__ == "__main__":

	# Part 1 Solution
	with open("day21_input", 'r') as infile:
		for line in infile.readlines():
			parse(line.strip())

	for item in allergens.keys():
		allergens[item] = set.intersection(*allergens[item])

	known_harmful = set()
	for item in allergens.keys():
		known_harmful.update(allergens[item])

	safe_foods = set(foods.keys())

	for bad in known_harmful:
		safe_foods.discard(bad)

	count = 0
	for item in foods_list:
		t = item.intersection(safe_foods)
		count += len(t)
	print(count)

	# Part 2 Solution
	for item in allergens.keys():
		for good in safe_foods:
			allergens[item].discard(good)

	done = False
	while not done:
		done = True
		for item in allergens.keys():
			if len(allergens[item]) == 1:
				for a in allergens.keys():
					if a != item:
						allergens[a].discard(list(allergens[item])[0])
		for item in allergens.keys():
			if len(allergens[item]) != 1:
				done = False
	
	alphabetical = [x for x in allergens.keys()]
	alphabetical.sort()
	out = ""
	for item in alphabetical:
		out += ''.join(allergens[item])+","
	print(out[:-1])

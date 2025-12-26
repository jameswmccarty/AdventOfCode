#!/usr/bin/python


replacements = dict()

def min_subs(chem):
	subs = 0
	while chem != "e":
		for rxn, rx in replacements:
			if rxn in chem:
				subs += 1
				chem = chem.replace(rxn, rx, 1)
				break
	return subs				
				
if __name__ == "__main__":

	mutations = set()

	start = ''

	# Part 1 Solution
	
	with open("day19_input", "r") as infile:
		for line in infile.readlines():
			if " => " in line:
				x, rxn = line.split(" => ")
				x = x.strip()
				rxn = rxn.strip()
				if x not in replacements:
					replacements[x] = set()
				replacements[x].add(rxn)
			elif len(line) > 1:
				start = line.strip()
	
	for idx, char in enumerate(start):
		if char in replacements:
			for rxn in replacements[char]:
				mutations.add(start[:idx] + rxn + start[idx+1:])
		if start[idx:idx+2] in replacements:
			for rxn in replacements[start[idx:idx+2]]:
				mutations.add(start[:idx] + rxn + start[idx+2:])
	
	print len(mutations)
	
	# Part 2 Solution
	replacements = []
	with open("day19_input", "r") as infile:
		for line in infile.readlines():
			if " => " in line:
				x, rxn = line.split(" => ")
				x = x.strip()
				rxn = rxn.strip()
				replacements.append((rxn, x))
	replacements.sort(key = lambda x : len(x[0]), reverse = True)
	print min_subs(start)

		

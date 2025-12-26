#!/usr/bin/python


orbits = dict()
seen = set()

def body_total(b):
	count = 0
	while True:
		if len(orbits[b]) > 0:
			b = orbits[b][0]
			count += 1
		else:
			break
	return count

def search(source, dest, step):
	if source == '' or orbits[source] == []:
		return float('inf')
	if source == dest:
		return step
	l = orbits[source][0]
	r = []
	for key, value in orbits.items():
		if source in value:
			r.append(key)
	seen.add(source)
	l_search = float('inf')
	r_search = [float('inf')]
	if r != []:
		for rr in r:
			if rr not in seen:
				r_search.append(search(rr, dest, step + 1))
	r_search = min(r_search)
	if l != '' and l not in seen:
		l_search = search(l, dest, step + 1)
	return min(l_search, r_search)
	

if __name__ == "__main__":
	
	# Part 1 Solution
	with open("day06_input", 'r') as infile:
		for line in infile.readlines():
			a,b = line.strip().split(')')
			orbits[a] = []
			orbits[b] = []
	with open("day06_input", 'r') as infile:
		for line in infile.readlines():
			a,b = line.strip().split(')')
			orbits[b].append(a)
		
	print(sum((body_total(x) for x in orbits.keys())))

	# Part 2 Solution
	print(search('YOU', 'SAN', 0)-2)

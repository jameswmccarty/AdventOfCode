#!/usr/bin/python

import itertools


def dp_tsp(cities, costs, opt):
	if opt == max:
		base = 0
	elif opt == min:
		base = float('inf')
	else:
		base = 0		
	best_path = base	
	# base cases
	for idx in range(len(cities)):
		# minimal path sets
		# ( 'start', {visited, nodes} ) : cost
		g = dict()
		for j in range(len(cities)): # direct path
			if j != idx:
				g[(cities[j], frozenset())] = 0 # costs[(cities[j], cities[idx])]
		for k in range(1,len(cities)): # k is set size
			for i in range(len(cities)):
				visit_list = itertools.combinations([x for x in cities if x != cities[i] and x != cities[idx]], k)
				for subset in visit_list:
					best = base
					for elem in subset:
						best = opt(best, costs[(cities[i], elem)] + g[(elem, frozenset(set(subset).difference({elem})))])
					g[(cities[i], frozenset(subset))] = best
		# find optimal tour
		best = base
		subset = frozenset(set(cities).difference({cities[idx]}))
		for elem in subset:
			best = opt(best, costs[(cities[idx], elem)] + g[(elem, frozenset(set(subset).difference({elem})))])
		g[(cities[idx], frozenset(subset))] = best
		best_path = opt(best_path, best)
	return best_path


if __name__ == "__main__":

	# Part 1 Solution
	
	# cost 'matrix' in form of
	# ('start', 'dest') : cost
	costs = dict()
	cities = set()
	
	with open("day9_input", "r") as infile:
		for line in infile.readlines():
			route, cost = line.strip().split(" = ")
			start, dest = route.split(" to ")
			cities.add(dest.strip())
			cities.add(start.strip())
			costs[(start.strip(), dest.strip())] = int(cost)
			costs[(dest.strip(), start.strip())] = int(cost) # symmetric costs

	cities = list(cities) # no more additions, allow for indexing
	
	print dp_tsp(cities, costs, min)
	
	# Part 2 Solution
	
	print dp_tsp(cities, costs, max)
	




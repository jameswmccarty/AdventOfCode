#!/usr/bin/python


import heapq
from itertools import combinations

tunnels = dict()
travel_cost = dict()
rates   = dict()

def dist_between(a,b):
	q = []
	q.append((0,a))
	seen = set()
	seen.add(a)
	while len(q) > 0:
		steps,pos = q.pop(0)
		if pos == b:
			return steps
		else:
			for c in tunnels[pos]:
				if c not in seen:
					q.append((steps+1,c))
					seen.add(c)
	return float('inf')

def parse_line(line):
	rate,connections = line.split(';')
	valve,rate = rate.split(' has flow rate=')
	valve = valve.replace("Valve ",'').strip()
	rate  = int(rate)
	junk,connections = connections.split(' valve')
	connections = connections.replace('s ','')
	connections = connections.split(',')
	tunnels[valve] = [ c.strip() for c in connections ]
	rates[valve] = rate

def search(targets):
	best = 0
	q = []
	heapq.heappush(q,(0,'AA',targets,30))
	while len(q) > 0:
		total,pos,targets,time = heapq.heappop(q)
		best = min(best,total)
		if len(targets) == 0 or time <= 0:
			best = min(best,total)
		elif time > 0:
			for t in targets:
				if time - travel_cost[(pos,t)] > 1:
					new_time = time - travel_cost[(pos,t)]
					heapq.heappush(q,(total-(new_time-1)*rates[t],t,[ x for x in targets if x != t],new_time-1))
	return -best

# This method works for the problem, but not the example, because all targets can be reached
# in the given time in the Example.  We can use a greedy combination of the best that one
# search can do, and then the best search on any targets that could not be reached in the
# first search.
def search2(targets):
	best = 0
	q = []
	left_targets = None
	heapq.heappush(q,(0,'AA',targets,26))
	while len(q) > 0:
		total,pos,targets,time = heapq.heappop(q)
		if total < best:
			best = min(best,total)
			left_targets = targets[:]
		if len(targets) == 0 or time <= 0:
			if total < best:
				best = min(best,total)
				left_targets = targets[:]
		elif time > 0:
			for t in targets:
				if time - travel_cost[(pos,t)] > 1:
					new_time = time - travel_cost[(pos,t)]
					heapq.heappush(q,(total-(new_time-1)*rates[t],t,[ x for x in targets if x != t],new_time-1))
	return -best,left_targets

def two_party_search(targets):
	best = 0
	q = []
	heapq.heappush(q,(0,'AA','AA',targets,26,26))
	while len(q) > 0:
		total,p1,p2,targets,t1,t2 = heapq.heappop(q)
		best = min(best,total)
		if len(targets) == 0 or (t1 <= 0 and t2 <= 0):
			best = min(best,total)
		elif (t1 > 0 or t2 > 0) and len(targets) > 0:
			if len(targets) >= 2 and t1 > 0 and t2 > 0:
				for combo in combinations(targets,2):
					a,b = combo
					if t1 - travel_cost[(p1,a)] > 1 and t2 - travel_cost[(p2,b)] > 1:
						new_t1 = t1 - travel_cost[(p1,a)]
						new_t2 = t2 - travel_cost[(p2,b)]
						heapq.heappush(q,(total-((new_t1-1)*rates[a]+(new_t2-1)*rates[b]),a,b,[ x for x in targets if x not in [a,b] ],new_t1-1,new_t2-1))
					if t1 - travel_cost[(p1,a)] > 1 and t2 - travel_cost[(p2,b)] < 1:
						new_t1 = t1 - travel_cost[(p1,a)]
						heapq.heappush(q,(total-(new_t1-1)*rates[a],a,'--',[ x for x in targets if x != a ],new_t1-1,0))
					if t1 - travel_cost[(p1,a)] < 1 and t2 - travel_cost[(p2,b)] > 1:
						new_t2 = t2 - travel_cost[(p2,b)]
						heapq.heappush(q,(total-(new_t2-1)*rates[b],'--',b,[ x for x in targets if x != b ],0,new_t2-1))
					b,a = combo
					if t1 - travel_cost[(p1,a)] > 1 and t2 - travel_cost[(p2,b)] > 1:
						new_t1 = t1 - travel_cost[(p1,a)]
						new_t2 = t2 - travel_cost[(p2,b)]
						heapq.heappush(q,(total-((new_t1-1)*rates[a]+(new_t2-1)*rates[b]),a,b,[ x for x in targets if x not in [a,b] ],new_t1-1,new_t2-1))
					if t1 - travel_cost[(p1,a)] > 1 and t2 - travel_cost[(p2,b)] < 1:
						new_t1 = t1 - travel_cost[(p1,a)]
						heapq.heappush(q,(total-(new_t1-1)*rates[a],a,'--',[ x for x in targets if x != a ],new_t1-1,0))
					if t1 - travel_cost[(p1,a)] < 1 and t2 - travel_cost[(p2,b)] > 1:
						new_t2 = t2 - travel_cost[(p2,b)]
						heapq.heappush(q,(total-(new_t2-1)*rates[b],'--',b,[ x for x in targets if x != b ],0,new_t2-1))
			elif p1 == '--' or p2 == '--':
				for a in targets:
					if p1 != '--' and t1 - travel_cost[(p1,a)] > 1:
						new_t1 = t1 - travel_cost[(p1,a)]
						heapq.heappush(q,(total-(new_t1-1)*rates[a],a,'--',[ x for x in targets if x != a],new_t1-1,t2))
					if p2 != '--' and t2 - travel_cost[(p2,a)] > 1:
						new_t2 = t2 - travel_cost[(p2,a)]
						heapq.heappush(q,(total-(new_t2-1)*rates[a],'--',a,[ x for x in targets if x != a],t1,new_t2-1))
	return -best

if __name__ == "__main__":

	# Part 1 Solution
	with open('day16_input','r') as infile:
		for line in infile.readlines():
			parse_line(line)
	for a in tunnels.keys():
		for b in tunnels.keys():
			travel_cost[(a,b)] = dist_between(a,b)
			travel_cost[(b,a)] = travel_cost[(a,b)]
			travel_cost[(a,'--')] = float('inf')
			travel_cost[(b,'--')] = float('inf')
			travel_cost[('--',a)] = float('inf')
			travel_cost[('--',b)] = float('inf')
	targets = [ k for k,v in rates.items() if v > 0 ]
	print(search(targets))

	# Part 2 Solution
	#print(two_party_search(targets)) # Works for Example -- very slow to check full problem
	points_so_far, left_to_search = search2(targets)
	final_points, junk = search2(left_to_search)
	print(points_so_far+final_points)


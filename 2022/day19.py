#!/usr/bin/python

blueprints = []

def parse_line(line):
	line = line.split('.')
	costs = []
	costs.append(int(line[0].split(' ')[-2])) # ore cost       | ore bot
	costs.append(int(line[1].split(' ')[-2])) # ore cost       | clay bot
	costs.append(int(line[2].split(' ')[-5])) # ore cost       | obsidian bot
	costs.append(int(line[2].split(' ')[-2])) # clay cost      | obsidian bot
	costs.append(int(line[3].split(' ')[-5])) # ore cost       | geode bot
	costs.append(int(line[3].split(' ')[-2])) # obsidian cost  | geode bot
	blueprints.append(tuple(costs))

max_geodes = 0

def dfs(blueprint,rb, cb, ob, gb, r, c, o, g, t):
	global max_geodes
	ore_max = max(blueprint[0],blueprint[1],blueprint[2],blueprint[4])
	if t == 0:
		max_geodes = max(max_geodes, g)
	# don't check the branch if the upper bound can't be broken
	elif g+(gb*t)+(t*(t-1))//2 > max_geodes:
		# evaluate building each type of robot, if we have resources
		# but only build a robot of that type if we are making less than the
		# purchase cost for resource production in a cycle
			# Geode Robot
		if r >= blueprint[4] and o >= blueprint[5]: # we can always use more geodes
			next_r,next_c,next_o,next_g = r,c,o,g
			next_r = r - blueprint[4]
			next_o = o - blueprint[5]
			# sum resources
			next_r += rb
			next_c += cb
			next_o += ob
			next_g += gb
			dfs(blueprint,rb,cb,ob,gb+1,next_r,next_c,next_o,next_g,t-1)
		else: # Assume it is always optimal to build a Geode bot
			# Obsidian Robot
			if r >= blueprint[2] and c >= blueprint[3] and ob < blueprint[5]: # Only geode bots need obsidian
				next_r,next_c,next_o,next_g = r,c,o,g
				next_r = r - blueprint[2]
				next_c = c - blueprint[3]
				# sum resources
				next_r += rb
				next_c += cb
				next_o += ob
				next_g += gb
				dfs(blueprint,rb,cb,ob+1,gb,next_r,next_c,next_o,next_g,t-1)
			# Clay Robot
			if r >= blueprint[1] and cb < blueprint[3]: # Only Obsidian bots need clay
				next_r,next_c,next_o,next_g = r,c,o,g
				next_r = r - blueprint[1]
				# sum resources
				next_r += rb
				next_c += cb
				next_o += ob
				next_g += gb
				dfs(blueprint,rb,cb+1,ob,gb,next_r,next_c,next_o,next_g,t-1)
			# Ore Robot
			if r >= blueprint[0] and rb < ore_max: # Can only make one bot per cycle
				next_r,next_c,next_o,next_g = r,c,o,g
				next_r = r - blueprint[0]
				# sum resources
				next_r += rb
				next_c += cb
				next_o += ob
				next_g += gb
				dfs(blueprint,rb+1,cb,ob,gb,next_r,next_c,next_o,next_g,t-1)
			# build nothing
			# sum resources
			next_r,next_c,next_o,next_g = r,c,o,g
			next_r += rb
			next_c += cb
			next_o += ob
			next_g += gb
			dfs(blueprint,rb,cb,ob,gb,next_r,next_c,next_o,next_g,t-1)

if __name__ == "__main__":

	# Part 1 Solution
	with open('day19_input','r') as infile:
		for line in infile.readlines():
			parse_line(line)
	sol = 0
	for i,e in enumerate(blueprints):
		max_geodes = 0
		dfs(e,1,0,0,0,0,0,0,0,24)
		sol += (i+1) * max_geodes
	print(sol)

	# Part 2 Solution
	sol = 1
	for i in range(3):
		max_geodes = 0
		dfs(blueprints[i],1,0,0,0,0,0,0,0,32)
		sol *= max_geodes
	print(sol)


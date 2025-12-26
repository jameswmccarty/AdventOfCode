#!/usr/bin/python


rules = []

def grow(prevgen):
	nextgen = ["."] * len(prevgen)
	for i in range(2, len(nextgen)-2):
		for rule in rules:
			if ''.join(prevgen[i-2:i+3]) == rule:
				nextgen[i] = "#"
	return nextgen
	
def score(gen):
	score = 0
	for i in range(len(gen)):
		if gen[i] == "#":
			score += (i-(len(gen)/2))
	return score	

if __name__ == "__main__":

	buffer = ["."] * 4000
	
	# Part 1 Solution

	with open("day12_input", "r") as infile:
		line = infile.readline()
		line = line.replace('initial state: ', '').strip()
		for i in range(len(line)):
			buffer[(len(buffer)/2) + i] = line[i]
		line = infile.readline()
		for line in infile.readlines():
			rule, result = line.split(" => ")
			if result.strip() == "#":
				rules.append(rule.strip())

	for i in range(1,21):
		buffer = grow(buffer)
	print score(buffer)
	
	# Part 2 Solution

	buffer = ["."] * 4000

	with open("day12_input", "r") as infile:
		line = infile.readline()
		line = line.replace('initial state: ', '').strip()
		for i in range(len(line)):
			buffer[(len(buffer)/2) + i] = line[i]
		line = infile.readline()
		for line in infile.readlines():
			rule, result = line.split(" => ")
			if result.strip() == "#":
				rules.append(rule.strip())

	generation = 0
	t_gen = 50000000000
	current_score = 0
	rpt_gen = 0
	base_score = 0
	delta = 0
	last_score = score(buffer)
	
	while True:
		last_score = score(buffer)
		last_config = ''.join(buffer[:]).strip(".")
		buffer = grow(buffer)
		generation += 1
		current_score = score(buffer)
		if last_config == ''.join(buffer[:]).strip("."):
			rpt_gen = generation-1
			base_score = last_score
			delta = current_score - base_score
			break
			
			

	#print rpt_gen
	#print delta
	#print base_score
	
	print ( t_gen - rpt_gen ) * delta + base_score
		

	
	

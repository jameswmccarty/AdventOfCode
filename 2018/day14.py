#!/usr/bin/python

class Elf:

	def __init__(self, idx, current):
		self.current = current
		self.idx = idx
	

if __name__ == "__main__":

	# Part 1 Solution
	
	elves = []
	scores = []
	
	#with open("day14_input_test", "r") as infile:
	#	line = infile.readline()
	line = "3 7"
	line = list(line.strip().split(" "))
	start_len = 77201
	for i in range(2):
		elves.append(Elf(i, int(line[i])))
		scores.append(int(line[i]))
	
	while True:
		#print scores
		comb = list(str(sum(x.current for x in elves)))
		comblist = [ int(x) for x in comb ]
		for item in comblist:
			scores.append(item)
		for elf in elves:
			elf.idx = (1 + elf.current + elf.idx) % len(scores)
			elf.current = scores[elf.idx]
		if len(scores) >= start_len + 10:
			result = scores[start_len:start_len + 11]
			result = [ str(x) for x in result ]
			print ''.join(result)
			break
	
	# Part 2 Solution
	
	elves = []
	scores = []

	line = "37"
	line = line.strip()
	goal_str = "077201"
	for i in range(2):
		elves.append(Elf(i, int(line[i])))
	
	scores = line
	while True:
		comb = list(str(sum(x.current for x in elves)))
		for item in comb:
			scores += item
		for elf in elves:
			elf.idx = (1 + elf.current + elf.idx) % len(scores)
			elf.current = int(scores[elf.idx])
		if goal_str in scores[-len(goal_str)*2:]:
			offset = scores[-len(goal_str)*2:].index(goal_str)
			term = len(scores) - len(goal_str)*2 + offset
			print term
			break

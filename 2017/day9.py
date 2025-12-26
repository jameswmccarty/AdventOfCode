#!/usr/bin/python


def process(stream, lvl):
	score = 0
	garbage = 0
	while len(stream) != 0:
		if stream[0] == '{':
			sub_score, stream, t_garbage = process(stream[1:],lvl+1)
			score += sub_score
			garbage += t_garbage
		elif stream[0] == '!':
			stream = stream[2:]
		elif stream[0] == '}':
			return score+lvl, stream[1:], garbage
		elif stream[0] == '<':
			stream = stream[1:]
			while stream[0] != '>':
				if stream[0] == '!':
					stream = stream[2:]
				else:
					garbage += 1
					stream = stream[1:]
			
		else:
			stream = stream[1:]
	return score, stream, garbage			

if __name__ == "__main__":

	# Part 1 and 2 Solution
	
	with open("day9_input", "r") as infile:
		result = process(infile.read(),0)
	print result[0]
	print result[2]
	
	

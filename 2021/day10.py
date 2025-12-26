#!/usr/bin/python


if __name__ == "__main__":

	opens = ["(","{","<","["]
	closes =[")","}",">","]"]

	def parse1(line):
		scores = [3,1197,25137,57]
		stack = []
		for char in line:
			if char in opens:
				stack.append(char)
			elif char in closes:
				if stack[-1] != opens[closes.index(char)]:
					return scores[closes.index(char)]
				else:
					stack.pop()
		return 0

	def parse2(line):
		scores = [1,3,4,2]
		stack = []
		for char in line:
			if char in opens:
				stack.append(char)
			elif char in closes:
				if stack[-1] != opens[closes.index(char)]:
					return 0
				else:
					stack.pop()
		if len(stack) > 0:
			stack = stack[::-1]
			score = 0
			for char in stack:
				score *= 5
				score += scores[opens.index(char)]	
		return score
				

	# Part 1 Solution

	with open("day10_input","r") as infile:
		lines = infile.read().strip().split('\n')
	print(sum([ parse1(line) for line in lines ]))


	# Part 2 Solution
	scores = [ parse2(line) for line in lines if parse2(line) > 0 ]
	print(sorted(scores)[len(scores)//2])

	

#!/usr/bin/python

if __name__ == "__main__":

	def part1_game(line):
		if 'X' in line:
			score = 1
		elif 'Y' in line:
			score = 2
		else:
			score = 3
		if line in ['A Y','B Z','C X']: # wins
			return score+6
		if line in ['A X','B Y','C Z']: # ties
			return score+3
		return score # loss

	def part2_game(line):
		if 'X' in line: # lose
			if 'A' in line:
				return 3
			if 'B' in line:
				return 1
			return 2
		if 'Y' in line: # tie
			score = 3
			if 'A' in line:
				return 1+score
			if 'B' in line:
				return 2+score
			return 3+score
		score = 6 # win
		if 'A' in line:
			return score+2
		if 'B' in line:
			return score+3
		return score+1

	# Part 1 Solution
	with open("day02_input", "r") as infile:
		score1 = 0
		score2 = 0
		for line in infile.readlines():
			score1 += part1_game(line.strip())
			score2 += part2_game(line.strip())
	print(score1)

	# Part 2 Solution
	print(score2)
